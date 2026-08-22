import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from commentary_engine.thinkmath.domain import AdvaitianSession, MVCState, SessionPhase
from commentary_engine.thinkmath.model_registry import (
    capability_for,
    ollama_base_url,
    stability_for,
    supports_role,
)
from commentary_engine.thinkmath.providers import (
    GROQ_FREE_TPM_BUDGET,
    MIN_COMPLETION_TOKENS,
    GroqAdapter,
)
from commentary_engine.thinkmath.resilience import retry_seconds, run_model_ladder
from commentary_engine.thinkmath.rendering import prepare_markdown
from commentary_engine.thinkmath.security import admin_enabled
from commentary_engine.thinkmath.state_machine import evaluate_transition
from commentary_engine.thinkmath.structured_output import (
    parse_model_response,
    safe_visible_fallback,
)
from commentary_engine.thinkmath.verification import (
    verification_label,
    verify_commentary,
    verify_equivalence,
)


class CoreArchitectureTests(unittest.TestCase):
    def test_ollama_endpoint_rejects_non_http_schemes(self):
        with patch.dict("os.environ", {"OLLAMA_BASE_URL": "file:///private/script"}):
            with self.assertRaises(ValueError):
                ollama_base_url()

    def test_admin_is_fail_closed_without_configured_secret(self):
        self.assertFalse(admin_enabled(None, "anything"))
        self.assertFalse(admin_enabled("secret", None))
        self.assertTrue(admin_enabled("secret", "secret"))

    def test_phase_three_cannot_bypass_mvc_gate(self):
        asset = AdvaitianSession(phase=SessionPhase.DIRECTIONS)
        decision = evaluate_transition(asset, "Give me Stage 2", model_suggested_phase=3)
        self.assertEqual(decision.phase, SessionPhase.DIRECTIONS)
        self.assertFalse(decision.allowed)

    def test_validated_complete_mvc_allows_convergence(self):
        asset = AdvaitianSession(
            phase=SessionPhase.DIRECTIONS,
            mvc=MVCState("quadratic in a", "take other root", "minimal root reaches zero", validated=True),
        )
        decision = evaluate_transition(asset, "Give me Stage 2", model_suggested_phase=3)
        self.assertEqual(decision.phase, SessionPhase.CONVERGENCE)
        self.assertTrue(decision.allowed)

    def test_structured_response_removes_machine_state(self):
        parsed = parse_model_response(
            'A useful question.\n```thinkmath-state\n{"suggested_phase": 2, "tier": 4}\n```'
        )
        self.assertEqual(parsed.visible_text, "A useful question.")
        self.assertEqual(parsed.suggested_phase, 2)
        self.assertEqual(parsed.tier, 4)
        self.assertEqual(parsed.parse_status, "structured")

    def test_malformed_state_is_not_trusted(self):
        parsed = parse_model_response("Hello\n```thinkmath-state\n{bad json}\n```")
        self.assertEqual(parsed.parse_status, "invalid")
        self.assertEqual(parsed.suggested_phase, 1)

    def test_generic_json_state_block_is_hidden(self):
        raw = (
            "🏆 TAKEAWAY\nKeep the invariant visible.\n"
            '```json\n{"suggested_phase": 3, "tier": 3, "mvc": {}}\n```'
        )
        parsed = parse_model_response(raw)
        self.assertEqual(parsed.parse_status, "structured")
        self.assertEqual(parsed.suggested_phase, 3)
        self.assertNotIn("suggested_phase", parsed.visible_text)
        self.assertNotIn("```json", parsed.visible_text)

    def test_bare_state_only_archetype_nudge_is_hidden_and_rendered_safely(self):
        raw = (
            '{"suggested_phase":1,"tier":3,"student_observations":[],'
            '"seed_hypotheses":[],"archetypes":[{"name":"INVARIANCE",'
            '"evidence":"The sum of interior angles stays fixed",'
            '"role":"candidate"}],"mvc":{"setup":"secret setup",'
            '"move":"secret move","closure":"secret closure","family":""}}'
        )
        parsed = parse_model_response(raw)

        self.assertEqual(parsed.parse_status, "structured")
        self.assertEqual(parsed.visible_text, "")
        rendered = safe_visible_fallback(parsed.state_update)
        self.assertEqual(
            rendered,
            "**INVARIANCE**\n\nThe sum of interior angles stays fixed",
        )
        self.assertNotIn("secret", rendered)

    def test_bare_multiline_state_with_trailing_period_never_leaks(self):
        raw = '{"suggested_phase":1,"archetypes":[{"name":"Induction","evidence":"first line\nsecond line"}]}.'
        parsed = parse_model_response(raw)
        self.assertEqual(parsed.parse_status, "structured")
        self.assertEqual(parsed.visible_text, "")
        self.assertEqual(parsed.state_update["archetypes"][0]["name"], "Induction")

    def test_ordinary_json_example_remains_visible(self):
        raw = 'An example:\n```json\n{"number": 12}\n```'
        parsed = parse_model_response(raw)
        self.assertIn('"number": 12', parsed.visible_text)

    def test_captured_stage_two_rendering_is_repaired(self):
        malformed = (
            "💡 ELEGANT PIVOT\n"
            r"\frac{27}{12}=d^{p-r},\qquad \frac{8}{12}=d^{q-r}.$$ "
            "All expressions use one base. **⚠️ PITFALLS** 1. **Ignoring signs** – check them. "
            "**🔗 CONNECTIONS** - **LOGARITHMS** linearise the powers. "
            "**🏆 TAKEAWAY** Preserve the common ratio. "
            '```json {"suggested_phase": 3, "tier": 3, "mvc": {}} ```'
        )
        rendered = prepare_markdown(malformed)
        self.assertIn(r"$$\frac{27}{12}", rendered)
        self.assertIn("\n\n**⚠️ PITFALLS**\n", rendered)
        self.assertIn("\n1. **Ignoring signs**", rendered)
        self.assertIn("\n\n**🔗 CONNECTIONS**\n", rendered)
        self.assertIn("\n- **LOGARITHMS**", rendered)
        self.assertNotIn("suggested_phase", rendered)

    def test_state_is_removed_from_existing_rendered_messages(self):
        rendered = prepare_markdown(
            "Visible explanation.\n```thinkmath-state\n"
            '{"suggested_phase": 2, "tier": 2}\n```'
        )
        self.assertEqual(rendered, "Visible explanation.")

    def test_descent_without_termination_fails_verification(self):
        commentary = "SEED BRUTE PIVOT use Vieta jumping descent PITFALL CONNECTION TAKEAWAY"
        checks = verify_commentary("positive integers", commentary)
        self.assertTrue(any(c.name == "descent_closure" and c.status == "fail" for c in checks))
        self.assertEqual(verification_label(checks, "SOLID"), "unverified")

    def test_symbolic_equivalence_is_deterministic(self):
        self.assertEqual(verify_equivalence("(x + 1)**2", "x**2 + 2*x + 1").status, "pass")
        self.assertEqual(verify_equivalence("x + 1", "x + 2").status, "fail")

    def test_symbolic_equivalence_rejects_attribute_access(self):
        result = verify_equivalence("x.__class__", "x")
        self.assertEqual(result.status, "review")
        self.assertIn("Could not parse", result.detail)

    def test_local_model_roles_are_enforced(self):
        self.assertTrue(supports_role("Ollama", "qwen3:8b", "mentor"))
        self.assertFalse(supports_role("Ollama", "qwen3:8b", "critic"))
        self.assertTrue(supports_role("Ollama", "qwen2.5-math:7b", "critic"))
        self.assertFalse(supports_role("Groq", "unreviewed/open-model", "mentor"))

    def test_public_groq_models_have_task_roles(self):
        self.assertTrue(supports_role("Groq", "qwen/qwen3.6-27b", "mentor"))
        self.assertFalse(supports_role("Groq", "openai/gpt-oss-120b", "mentor"))
        self.assertTrue(supports_role("Groq", "openai/gpt-oss-120b", "commentary"))
        self.assertEqual(capability_for("Groq", "openai/gpt-oss-120b", 0), 10)
        self.assertEqual(stability_for("Groq", "openai/gpt-oss-20b"), "production")
        self.assertEqual(stability_for("Groq", "qwen/qwen3.6-27b"), "preview")

    def test_groq_reasoning_models_return_visible_content(self):
        recorded = {}

        class FakeCompletions:
            def create(self, **kwargs):
                recorded.update(kwargs)
                message = SimpleNamespace(content="Visible Socratic question")
                return SimpleNamespace(choices=[SimpleNamespace(message=message)])

        fake_client = SimpleNamespace(chat=SimpleNamespace(completions=FakeCompletions()))
        adapter = GroqAdapter("openai/gpt-oss-20b", "system", client=fake_client)
        result = adapter.send("problem", [], 300)

        self.assertEqual(result, "Visible Socratic question")
        self.assertEqual(recorded["reasoning_effort"], "low")
        self.assertEqual(recorded["reasoning_format"], "hidden")
        self.assertLessEqual(recorded["max_tokens"], 300)

    def test_groq_adapter_caps_completion_to_free_tpm_budget(self):
        recorded = {}

        class FakeCompletions:
            def create(self, **kwargs):
                recorded.update(kwargs)
                return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content="ok"))])

        client = SimpleNamespace(chat=SimpleNamespace(completions=FakeCompletions()))
        adapter = GroqAdapter("openai/gpt-oss-120b", "x" * 9000, client=client)
        adapter.send("problem", [], 5000)
        self.assertLess(recorded["max_tokens"], 5000)
        estimated_input = (9000 // 3) + 12 + (len("problem") // 3) + 12
        self.assertLessEqual(estimated_input + recorded["max_tokens"], GROQ_FREE_TPM_BUDGET)

    def test_groq_adapter_drops_old_history_before_exceeding_tpm(self):
        recorded = {}

        class FakeCompletions:
            def create(self, **kwargs):
                recorded.update(kwargs)
                return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content="ok"))])

        client = SimpleNamespace(chat=SimpleNamespace(completions=FakeCompletions()))
        adapter = GroqAdapter("openai/gpt-oss-20b", "system", client=client)
        history = [
            {"role": "user" if index % 2 == 0 else "mentor", "content": "x" * 6000}
            for index in range(8)
        ]
        adapter.send("problem", history, 5000)

        self.assertLess(len(recorded["messages"]), len(history) + 2)
        estimated = sum((len(item["content"]) // 3) + 12 for item in recorded["messages"])
        self.assertGreaterEqual(recorded["max_tokens"], MIN_COMPLETION_TOKENS)
        self.assertLessEqual(estimated + recorded["max_tokens"], GROQ_FREE_TPM_BUDGET)

    def test_groq_adapter_rejects_irreducibly_oversized_prompt(self):
        adapter = GroqAdapter("openai/gpt-oss-20b", "x" * 30000, client=SimpleNamespace())
        with self.assertRaisesRegex(ValueError, "request too large"):
            adapter.send("problem", [], 700)

    def test_retry_after_header_controls_cooldown(self):
        error = RuntimeError("429 rate limit")
        error.response = SimpleNamespace(headers={"retry-after": "7"})
        self.assertEqual(retry_seconds(error), 8)

    def test_rate_limit_reset_header_controls_daily_cooldown(self):
        error = RuntimeError("429 RPD exhausted")
        error.response = SimpleNamespace(
            headers={"x-ratelimit-reset-requests": "2m59.5s"}
        )
        self.assertEqual(retry_seconds(error), 180)

    def test_model_ladder_retries_transient_then_falls_back(self):
        candidates = [{"model": "first"}, {"model": "second"}]
        attempts = []
        failures = []
        sleeps = []

        def send(candidate):
            attempts.append(candidate["model"])
            if candidate["model"] == "first":
                raise RuntimeError("503 upstream unavailable")
            return "recovered"

        text, selected = run_model_ladder(
            candidates,
            send,
            lambda candidate, error, kind: failures.append((candidate["model"], kind)),
            sleep=sleeps.append,
            jitter=lambda low, high: 0.2,
        )

        self.assertEqual(text, "recovered")
        self.assertEqual(selected["model"], "second")
        self.assertEqual(attempts, ["first", "first", "second"])
        self.assertEqual(failures, [("first", "transient")])
        self.assertEqual(sleeps, [0.2])

    def test_golden_eval_catalog_is_well_formed(self):
        path = Path(__file__).parents[1] / "evals" / "golden_cases.json"
        cases = json.loads(path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 15)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        self.assertEqual({case["phase"] for case in cases}, {1, 2, 3})


if __name__ == "__main__":
    unittest.main()

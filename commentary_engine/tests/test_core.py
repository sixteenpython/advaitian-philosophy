import unittest
import json
from pathlib import Path
from types import SimpleNamespace

from commentary_engine.thinkmath.domain import AdvaitianSession, MVCState, SessionPhase
from commentary_engine.thinkmath.model_registry import capability_for, supports_role
from commentary_engine.thinkmath.providers import GroqAdapter
from commentary_engine.thinkmath.security import admin_enabled
from commentary_engine.thinkmath.state_machine import evaluate_transition
from commentary_engine.thinkmath.structured_output import parse_model_response
from commentary_engine.thinkmath.verification import verification_label, verify_commentary, verify_equivalence


class CoreArchitectureTests(unittest.TestCase):
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

    def test_descent_without_termination_fails_verification(self):
        commentary = "SEED BRUTE PIVOT use Vieta jumping descent PITFALL CONNECTION TAKEAWAY"
        checks = verify_commentary("positive integers", commentary)
        self.assertTrue(any(c.name == "descent_closure" and c.status == "fail" for c in checks))
        self.assertEqual(verification_label(checks, "SOLID"), "unverified")

    def test_symbolic_equivalence_is_deterministic(self):
        self.assertEqual(verify_equivalence("(x + 1)**2", "x**2 + 2*x + 1").status, "pass")
        self.assertEqual(verify_equivalence("x + 1", "x + 2").status, "fail")

    def test_local_model_roles_are_enforced(self):
        self.assertTrue(supports_role("Ollama", "qwen3:8b", "mentor"))
        self.assertFalse(supports_role("Ollama", "qwen3:8b", "critic"))
        self.assertTrue(supports_role("Ollama", "qwen2.5-math:7b", "critic"))

    def test_public_groq_models_have_task_roles(self):
        self.assertTrue(supports_role("Groq", "qwen/qwen3.6-27b", "mentor"))
        self.assertFalse(supports_role("Groq", "openai/gpt-oss-120b", "mentor"))
        self.assertTrue(supports_role("Groq", "openai/gpt-oss-120b", "commentary"))
        self.assertEqual(capability_for("Groq", "openai/gpt-oss-120b", 0), 10)

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
        self.assertLessEqual(estimated_input + recorded["max_tokens"], 7400)

    def test_golden_eval_catalog_is_well_formed(self):
        path = Path(__file__).parents[1] / "evals" / "golden_cases.json"
        cases = json.loads(path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 15)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        self.assertEqual({case["phase"] for case in cases}, {1, 2, 3})


if __name__ == "__main__":
    unittest.main()

import unittest

from commentary_engine.thinkmath.domain import (
    AdvaitianSession,
    ArchetypeHypothesis,
    MVCState,
    SessionPhase,
)
from commentary_engine.thinkmath.student_experience import (
    assurance_copy,
    build_thinking_map,
    demonstration,
    friendly_provider_error,
    passport_entry,
    provider_readiness,
    split_commentary,
    transfer_challenge,
)


class StudentExperienceTests(unittest.TestCase):
    def test_structural_draft_sets_honest_expectation(self):
        label, detail = assurance_copy("structural_draft")
        self.assertIn("Structural", label)
        self.assertIn("verification", detail)

    def test_empty_thinking_map_starts_with_problem_prompt(self):
        view = build_thinking_map(AdvaitianSession())
        self.assertEqual(view.phase_name, "Notice Structure")
        self.assertIn("problem", view.open_question.lower())
        self.assertEqual(view.progress, 0)

    def test_map_progresses_to_missing_closure(self):
        asset = AdvaitianSession(
            problem="Prove it",
            phase=SessionPhase.DIRECTIONS,
            student_observations=["Parity is fixed"],
            seed_hypotheses=["Invariance"],
            archetypes=[ArchetypeHypothesis("Invariance")],
            mvc=MVCState("Reframe", "Transform", ""),
        )
        view = build_thinking_map(asset)
        self.assertEqual(
            view.open_question, "What forces the conclusion or stops the process?"
        )
        self.assertGreater(view.progress, 0.5)

    def test_map_prioritizes_current_proof_obligation_and_claim_status(self):
        asset = AdvaitianSession(
            problem="Prove P",
            current_proof_obligation="justify the reduction",
            claim_ledger=[{"text": "It always works", "status": "needs_proof", "reason": "gap"}],
        )
        view = build_thinking_map(asset)
        self.assertEqual(view.open_question, "justify the reduction")
        self.assertEqual(view.claim_ledger[0]["status"], "needs_proof")

    def test_demo_is_complete_without_model_inference(self):
        asset, messages = demonstration("odd-layers")
        self.assertTrue(asset.mvc.validated)
        self.assertEqual(asset.phase, SessionPhase.CONVERGENCE)
        self.assertTrue(any("TAKEAWAY" in message["content"] for message in messages))

    def test_every_demo_has_a_validated_canonical_asset(self):
        for demo_id in ("odd-layers", "pigeonhole", "symmetric-expression"):
            asset, _ = demonstration(demo_id)
            self.assertTrue(asset.problem)
            self.assertTrue(asset.seed_hypotheses)
            self.assertTrue(asset.mvc.complete)

    def test_commentary_is_split_into_learning_sections(self):
        sections = split_commentary(
            "🌱 THE SEED\nPattern.\n\n💡 ELEGANT PIVOT\nSquare it.\n\n"
            "⚠️ PITFALLS\nKeep the cross-term."
        )
        self.assertEqual(
            [section.title for section in sections],
            ["The Seed", "Elegant Pivot", "Pitfalls"],
        )
        self.assertEqual(sections[1].body, "Square it.")

    def test_provider_readiness_distinguishes_ready_and_resting(self):
        offline = provider_readiness([], set())
        self.assertEqual(offline.state, "offline")
        self.assertIn("offline", offline.headline.lower())
        self.assertIn("deterministic", offline.detail.lower())
        models = [{"provider": "Groq", "model": "open-model"}]
        self.assertEqual(provider_readiness(models, set()).state, "ready")
        self.assertEqual(
            provider_readiness(models, {"Groq::open-model"}).state, "resting"
        )

    def test_provider_errors_are_student_friendly(self):
        title, detail = friendly_provider_error("402 payment method required")
        self.assertIn("free", title.lower())
        self.assertNotIn("402", detail)
        title, _ = friendly_provider_error("429 quota exhausted")
        self.assertIn("capacity", title.lower())

    def test_passport_requires_author_confirmed_mvc(self):
        asset = AdvaitianSession(problem="P", seed_hypotheses=["Seed"])
        self.assertIsNone(passport_entry(asset))
        asset.mvc = MVCState("S", "M", "C", validated=True)
        entry = passport_entry(asset)
        self.assertIsNotNone(entry)
        self.assertEqual(entry["seed"], "Seed")

    def test_transfer_challenge_follows_the_discovered_seed(self):
        asset = AdvaitianSession(seed_hypotheses=["Pigeonhole collision"])
        _, challenge = transfer_challenge(asset)
        self.assertIn("socks", challenge)


if __name__ == "__main__":
    unittest.main()

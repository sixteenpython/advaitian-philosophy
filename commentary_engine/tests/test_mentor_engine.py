import unittest

from commentary_engine.thinkmath.conversation import classify_student_turn
from commentary_engine.thinkmath.domain import (
    AdvaitianSession,
    ArchetypeHypothesis,
    MVCState,
    SessionPhase,
)
from commentary_engine.thinkmath.mentor_engine import (
    MentorAction,
    ProblemMap,
    cache_problem_map,
    cached_problem_map,
    choose_mentor_action,
    deterministic_fallback,
    ensure_teacher_response,
    problem_fingerprint,
    update_claim_ledger,
    validate_state_proposal,
)
from commentary_engine.thinkmath.verification import verify_student_claims


class MentorEngineTests(unittest.TestCase):
    GRASSHOPPER = (
        "A grasshopper is to jump along the real axis. Let a1, ..., an be distinct "
        "positive integers and M a set of n−1 positive integers not containing their "
        "sum. Prove that in some order it jumps to the right and never lands in M."
    )

    def test_empty_session_asks_for_observation(self):
        decision = choose_mentor_action(
            AdvaitianSession(problem="Prove P"),
            classify_student_turn("Prove P"),
            0,
            "Prove P",
        )
        self.assertEqual(decision.action, MentorAction.ASK_OBSERVATION)
        self.assertEqual(decision.routing_profile, "reasoning")

    def test_recovery_policy_escalates_deterministically(self):
        turn = classify_student_turn("I don't know")
        expected = {
            1: MentorAction.NARROW_GOAL,
            2: MentorAction.TEST_SMALL_CASE,
            3: MentorAction.OFFER_DIRECTIONS,
            4: MentorAction.MODEL_MICRO_STEP,
            5: MentorAction.CHANGE_REPRESENTATION,
        }
        for level, action in expected.items():
            with self.subTest(level=level):
                decision = choose_mentor_action(AdvaitianSession(), turn, level, turn.text)
                self.assertEqual(decision.action, action)

    def test_disagreement_requires_check_not_defence(self):
        decision = choose_mentor_action(
            AdvaitianSession(), classify_student_turn("That is wrong"), 1, "That is wrong"
        )
        self.assertEqual(decision.action, MentorAction.CHECK_DISPUTED_STEP)
        self.assertIn("verification", decision.reason)

    def test_directions_focus_on_missing_mvc(self):
        asset = AdvaitianSession(
            phase=SessionPhase.DIRECTIONS,
            mvc=MVCState(setup="Choose a minimum"),
        )
        decision = choose_mentor_action(
            asset, classify_student_turn("What next?"), 0, "What next?"
        )
        self.assertEqual(decision.action, MentorAction.COMPLETE_MVC)

    def test_model_cannot_attribute_ungrounded_belief_to_student(self):
        asset = AdvaitianSession(problem="A geometry problem")
        proposal = {
            "student_observations": ["The student noticed a cyclic quadrilateral"],
            "seed_hypotheses": ["Inversion"],
            "archetypes": [{"name": "Inversion", "evidence": "circle structure"}],
        }
        accepted, problem_map, notes = validate_state_proposal(
            asset,
            classify_student_turn("I drew the diagram"),
            "I drew the diagram",
            proposal,
        )
        self.assertNotIn("student_observations", accepted)
        self.assertNotIn("seed_hypotheses", accepted)
        self.assertNotIn("archetypes", accepted)
        self.assertTrue(notes)
        self.assertIsNone(problem_map)

    def test_explicit_student_archetype_is_accepted(self):
        asset = AdvaitianSession(problem="P")
        proposal = {
            "seed_hypotheses": ["Maybe invariance"],
            "archetypes": [{"name": "Invariance", "evidence": "fixed parity"}],
        }
        accepted, _, _ = validate_state_proposal(
            asset,
            classify_student_turn("Maybe invariance is the key"),
            "Maybe invariance is the key",
            proposal,
        )
        self.assertEqual(accepted["archetypes"][0]["name"], "Invariance")
        self.assertEqual(accepted["seed_hypotheses"], ["Maybe invariance"])

    def test_recovery_never_changes_math_state_but_can_refresh_map(self):
        proposal = {
            "seed_hypotheses": ["Invariance"],
            "problem_map": {"domain": "number theory", "current_goal": "test parity"},
        }
        accepted, problem_map, notes = validate_state_proposal(
            AdvaitianSession(problem="P"),
            classify_student_turn("I am confused"),
            "I am confused",
            proposal,
        )
        self.assertEqual(accepted, {})
        self.assertEqual(problem_map.domain, "number theory")
        self.assertIn("recovery", notes[0])

    def test_partial_map_update_preserves_prior_directions(self):
        asset = AdvaitianSession(
            problem="P",
            problem_map={
                "domain": "geometry",
                "current_goal": "find equal angles",
                "directions": [{"name": "Cyclic", "reason": "equal angles", "confidence": 0.7}],
                "confidence": 0.7,
            },
        )
        _, problem_map, _ = validate_state_proposal(
            asset,
            classify_student_turn("I am confused"),
            "I am confused",
            {"problem_map": {"current_goal": "compare two angles"}},
        )
        self.assertEqual(problem_map.current_goal, "compare two angles")
        self.assertEqual(problem_map.directions[0]["name"], "Cyclic")

    def test_problem_map_is_bounded_and_normalized(self):
        value = {
            "domain": "  number   theory ",
            "directions": [
                {"name": f"Path {index}", "reason": "R", "confidence": 5}
                for index in range(10)
            ],
            "proof_obligations": [str(index) for index in range(20)],
        }
        result = ProblemMap.from_dict(value, "Prove something")
        self.assertEqual(result.domain, "number theory")
        self.assertEqual(len(result.directions), 6)
        self.assertEqual(len(result.proof_obligations), 8)
        self.assertEqual(result.directions[0]["confidence"], 1.0)

    def test_problem_fingerprint_is_stable_across_spacing_and_case(self):
        self.assertEqual(problem_fingerprint(" Prove   X "), problem_fingerprint("prove x"))

    def test_confident_problem_map_is_reused_for_identical_problem(self):
        problem = "A unique cache-test problem about 1729"
        cache_problem_map(
            problem,
            ProblemMap(domain="number theory", current_goal="factor 1729", confidence=0.8),
        )
        reused = cached_problem_map("  a UNIQUE cache-test problem about 1729 ")
        self.assertIsNotNone(reused)
        self.assertEqual(reused.current_goal, "factor 1729")

    def test_zero_confidence_map_is_not_cached(self):
        problem = "A unique uncached problem about 246813579"
        cache_problem_map(problem, ProblemMap(domain="unknown", confidence=0.0))
        self.assertIsNone(cached_problem_map(problem))

    def test_curated_problem_uses_compiled_map_without_inference(self):
        result = cached_problem_map(
            "Prove that the sum of the first n odd positive integers is n^2."
        )
        self.assertEqual(result.source, "compiled")
        self.assertEqual(result.confidence, 1.0)
        self.assertTrue(result.proof_obligations)

    def test_grasshopper_problem_has_reviewed_map(self):
        result = cached_problem_map(self.GRASSHOPPER)
        self.assertEqual(result.source, "compiled")
        self.assertIn("induction", result.domain)

    def test_false_grasshopper_claim_is_gently_corrected(self):
        text = "No, a1 or any ai cannot be in M."
        decision = choose_mentor_action(
            AdvaitianSession(problem=self.GRASSHOPPER), classify_student_turn(text), 0, text
        )
        self.assertEqual(decision.action, MentorAction.CORRECT_MISCONCEPTION)
        response = deterministic_fallback(decision, cached_problem_map(self.GRASSHOPPER))
        self.assertIn("excludes only the total", response)
        self.assertIn("M={1}", response)
        self.assertEqual(response.count("?"), 1)

    def test_assertive_claim_becomes_proof_obligation(self):
        text = "Therefore this always works by induction."
        asset = AdvaitianSession(problem="Prove P", current_proof_obligation="justify the reduction")
        decision = choose_mentor_action(asset, classify_student_turn(text), 0, text)
        self.assertEqual(decision.action, MentorAction.TEST_CLAIM)
        self.assertEqual(decision.proof_obligation, "justify the reduction")

    def test_correction_is_enforced_and_recorded(self):
        text = "A larger jump is always safe"
        asset = AdvaitianSession(problem=self.GRASSHOPPER)
        decision = choose_mentor_action(asset, classify_student_turn(text), 0, text)
        response = ensure_teacher_response(
            "What changes and what stays fixed? What else?", decision,
            cached_problem_map(self.GRASSHOPPER),
            [{"question": "What changes and what stays fixed?"}], text,
        )
        self.assertIn("not automatically safe", response)
        self.assertEqual(response.count("?"), 1)
        update_claim_ledger(asset, text, decision, [])
        self.assertEqual(asset.claim_ledger[0]["status"], "corrected")

    def test_fallback_is_available_for_every_action(self):
        turn = classify_student_turn("I don't know")
        for level in range(1, 6):
            decision = choose_mentor_action(AdvaitianSession(), turn, level, turn.text)
            self.assertTrue(deterministic_fallback(decision).strip())

    def test_plain_identity_is_verified(self):
        checks = verify_student_claims("I think (x+1)^2 = x^2 + 2*x + 1")
        self.assertEqual(len(checks), 1)
        self.assertEqual(checks[0].status, "pass")

    def test_conditional_or_false_claim_is_sent_for_review(self):
        checks = verify_student_claims("Perhaps x + 1 = x + 2")
        self.assertEqual(checks[0].status, "review")

    def test_existing_archetype_can_be_reconciled(self):
        asset = AdvaitianSession(archetypes=[ArchetypeHypothesis("Symmetry")])
        accepted, _, _ = validate_state_proposal(
            asset,
            classify_student_turn("It swaps the two variables"),
            "It swaps the two variables",
            {"archetypes": [{"name": "Symmetry", "evidence": "swap"}]},
        )
        self.assertEqual(accepted["archetypes"][0]["name"], "Symmetry")

    def test_new_grounded_evidence_does_not_erase_prior_student_work(self):
        asset = AdvaitianSession(student_observations=["Parity stays fixed"])
        accepted, _, _ = validate_state_proposal(
            asset,
            classify_student_turn("The endpoint is also fixed"),
            "The endpoint is also fixed",
            {"student_observations": ["The endpoint is fixed"]},
        )
        self.assertEqual(
            accepted["student_observations"],
            ["Parity stays fixed", "The endpoint is fixed"],
        )


if __name__ == "__main__":
    unittest.main()

import unittest

from commentary_engine.thinkmath.conversation import (
    TurnKind,
    accepted_phase_suggestion,
    accepted_state_update,
    classify_student_turn,
    ensure_recovery_acknowledgement,
    first_substantive_user_message,
    mentor_conversation_context,
    model_user_message,
    next_support_level,
)


class ConversationTests(unittest.TestCase):
    def test_common_recovery_language_is_recognized(self):
        cases = {
            "I don't know": TurnKind.STUCK,
            "I dont know": TurnKind.STUCK,
            "I don’t know": TurnKind.STUCK,
            "I have no clue": TurnKind.STUCK,
            "I am confused": TurnKind.CONFUSED,
            "I cannot think of a way to proceed": TurnKind.STUCK,
            "That doesn't make sense": TurnKind.CONFUSED,
            "Can you explain again?": TurnKind.REPEAT,
            "Show me a small example": TurnKind.EXAMPLE,
            "I disagree": TurnKind.DISAGREE,
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(classify_student_turn(text).kind, expected)

    def test_uncertain_mathematical_idea_remains_substantive(self):
        turn = classify_student_turn("I don't know, but maybe it is invariance")
        self.assertEqual(turn.kind, TurnKind.PARTIAL)
        self.assertFalse(turn.is_recovery)

    def test_uncertain_problem_statement_is_not_discarded(self):
        turn = classify_student_turn(
            "I don't know how to prove that the first n odd numbers sum to n squared"
        )
        self.assertEqual(turn.kind, TurnKind.PARTIAL)
        self.assertFalse(turn.is_recovery)

    def test_repeated_recovery_increases_scaffolding(self):
        turn = classify_student_turn("I am confused")
        level = next_support_level(0, turn)
        level = next_support_level(level, turn)
        level = next_support_level(level, turn)
        self.assertEqual(level, 3)
        guidance = mentor_conversation_context(turn, level)
        self.assertIn("two concrete directions", guidance)
        self.assertIn("at most one question", guidance)

    def test_recovery_cannot_modify_math_state_or_phase(self):
        turn = classify_student_turn("I don't know")
        update = {"seed_hypotheses": ["I don't know"], "archetypes": ["Guess"]}
        self.assertEqual(accepted_state_update(turn, update), {})
        self.assertEqual(accepted_phase_suggestion(turn, 1, 3), 1)

    def test_recovery_prompt_and_visible_reply_begin_humanely(self):
        turn = classify_student_turn("I don't know")
        model_input = model_user_message(turn, 1)
        self.assertIn("Begin your student-facing reply exactly with", model_input)
        visible = ensure_recovery_acknowledgement(
            turn,
            "Try adding the next odd number.",
        )
        self.assertTrue(visible.startswith("That's okay"))
        self.assertIn("Try adding", visible)

    def test_existing_humane_opening_is_not_duplicated(self):
        turn = classify_student_turn("I don't know")
        response = "That's okay—let's make the next step smaller.\n\nTry $1+3$."
        self.assertEqual(ensure_recovery_acknowledgement(turn, response), response)
        curly = "That’s okay—let’s make the next step smaller. What do we know?"
        self.assertEqual(ensure_recovery_acknowledgement(turn, curly), curly)

    def test_partial_answer_may_update_math_state(self):
        turn = classify_student_turn("Not sure, but maybe symmetry")
        update = {"seed_hypotheses": ["Symmetry"]}
        self.assertEqual(accepted_state_update(turn, update), update)
        self.assertEqual(accepted_phase_suggestion(turn, 1, 2), 2)

    def test_problem_selection_skips_recovery_turns(self):
        messages = [
            {"role": "user", "content": "I don't know"},
            {"role": "mentor", "content": "What problem are you working on?"},
            {"role": "user", "content": "Prove that odd partial sums are squares"},
        ]
        self.assertEqual(
            first_substantive_user_message(messages),
            "Prove that odd partial sums are squares",
        )


if __name__ == "__main__":
    unittest.main()

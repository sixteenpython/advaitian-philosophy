import unittest

from commentary_engine.thinkmath.domain import MVCState
from commentary_engine.thinkmath.pedagogy import (
    assess_mvc,
    stage2_gate_message,
    substantial_work_summary,
)


class PedagogyTests(unittest.TestCase):
    def test_descent_requires_an_explicit_boundary(self):
        incomplete = MVCState(
            setup="Rewrite as a quadratic and take the other Vieta root.",
            move="Use the other root to descend to a smaller solution.",
            closure="The quotient is invariant, so the result follows.",
            family="Vieta jumping",
        )
        assessment = assess_mvc(incomplete)
        self.assertFalse(assessment.ready)
        self.assertIn("stops", assessment.next_obligation)

    def test_descent_with_boundary_is_structurally_ready(self):
        complete = MVCState(
            setup="Choose a minimal solution and rewrite as a quadratic.",
            move="Take the other Vieta root; positivity and integrality remain valid.",
            closure="The descent terminates when the other root is zero; the equation then forces the quotient to be a square.",
            family="Vieta jumping",
        )
        self.assertTrue(assess_mvc(complete).ready)

    def test_gate_names_one_obligation_instead_of_rendering_commentary(self):
        message = stage2_gate_message(MVCState(setup="Rewrite as a quadratic"))
        self.assertIn("next proof obligation", message)
        self.assertNotIn("SEED", message)

    def test_substantial_work_summary_uses_student_techniques(self):
        summary = substantial_work_summary("Use the discriminant, then a Vieta jumping descent.")
        self.assertIn("Vieta", summary)
        self.assertIn("descent", summary)


if __name__ == "__main__":
    unittest.main()

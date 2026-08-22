import os
import unittest
from pathlib import Path
from unittest.mock import patch

from streamlit.testing.v1 import AppTest


class StreamlitStudentExperienceTests(unittest.TestCase):
    def test_student_shell_and_offline_demonstration_render(self):
        app_path = Path(__file__).parents[1] / "app.py"
        with patch.dict(os.environ, {"THINKMATH_DYNAMIC_MODEL_DISCOVERY": "false"}):
            app = AppTest.from_file(str(app_path)).run(timeout=30)

        self.assertFalse(app.exception)
        self.assertEqual(
            [tab.label for tab in app.tabs],
            ["Learn", "Thinking Map", "Commentary", "My Journey"],
        )
        visible = "\n".join(
            element.value
            for collection in (app.markdown, app.caption, app.info)
            for element in collection
        )
        self.assertIn("ThinkMath.ai", visible)
        self.assertIn("Student Experience v3.1.1", visible)
        self.assertIn("What mathematical problem are you wrestling with?", visible)
        self.assertIn("Private by default", visible)
        demo_button = next(
            button for button in app.button if button.label == "Explore journey"
        )
        demo_button.click().run(timeout=30)
        self.assertFalse(app.exception)
        self.assertEqual(app.session_state["current_phase"], 3)
        self.assertTrue(
            any("complete structural commentary" in item.value for item in app.success)
        )


if __name__ == "__main__":
    unittest.main()

import unittest

from main import analyze_feedback
from schemas import FeedbackAnalysis


class TestStructuredOutput(unittest.TestCase):

    def test_valid_feedback(self):
        result = analyze_feedback(
            "The teacher explains every topic clearly."
        )
        self.assertIsInstance(result, FeedbackAnalysis)
        self.assertEqual(result.sentiment.value, "Positive")
        self.assertEqual(result.category.value, "Teaching")
        self.assertEqual(result.priority.value, "Low")

    def test_projector_problem(self):
        result = analyze_feedback(
            "The classroom projector has not worked for two weeks."
        )
        self.assertEqual(result.sentiment.value, "Negative")
        self.assertEqual(result.category.value, "Infrastructure")
        self.assertEqual(result.priority.value, "High")

    def test_mixed_teaching_feedback(self):
        result = analyze_feedback(
            "The course content is good, but the teaching speed is too fast."
        )
        self.assertEqual(result.sentiment.value, "Negative")
        self.assertEqual(result.category.value, "Teaching")
        self.assertEqual(result.priority.value, "Medium")

    def test_laboratory_problem(self):
        result = analyze_feedback(
            "The laboratory computers are not working and students cannot complete practical assignments."
        )
        self.assertEqual(result.sentiment.value, "Negative")
        self.assertEqual(result.category.value, "Infrastructure")
        self.assertEqual(result.priority.value, "High")

    def test_neutral_library_feedback(self):
        result = analyze_feedback(
            "The library is open until 5 PM."
        )
        self.assertEqual(result.sentiment.value, "Neutral")
        self.assertEqual(result.category.value, "Infrastructure")
        self.assertEqual(result.priority.value, "Low")

    def test_empty_feedback_is_rejected(self):
        with self.assertRaises(ValueError):
            analyze_feedback("")


if __name__ == "__main__":
    unittest.main(verbosity=2)

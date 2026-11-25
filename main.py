import json
import sys

from pydantic import ValidationError
from schemas import FeedbackAnalysis

MAX_ATTEMPTS = 3
MOCK_MODE = True


def classify_feedback(feedback: str) -> dict:
    text = feedback.lower()

    # Category classification
    if any(word in text for word in [
        "teacher", "teaching", "explains", "teaching speed"
    ]):
        category = "Teaching"
    elif any(word in text for word in [
        "course", "syllabus", "content"
    ]):
        category = "Course"
    elif any(word in text for word in [
        "classroom", "projector", "laboratory", "computers",
        "library", "facility", "facilities"
    ]):
        category = "Infrastructure"
    else:
        category = "Other"

    # Sentiment classification
    negative_words = [
        "not working", "not worked", "has not worked",
        "broken", "cannot", "unable", "problem",
        "too fast", "not functioning"
    ]

    positive_words = [
        "good", "excellent", "clearly", "helpful", "great"
    ]

    has_negative = any(word in text for word in negative_words)
    has_positive = any(word in text for word in positive_words)

    if has_negative:
        sentiment = "Negative"
    elif has_positive:
        sentiment = "Positive"
    else:
        sentiment = "Neutral"

    # Priority classification
    if (
        "cannot complete" in text
        or "unable to complete" in text
        or "not worked for two weeks" in text
        or "has not worked for two weeks" in text
    ):
        priority = "High"
    elif sentiment == "Negative":
        priority = "Medium"
    else:
        priority = "Low"

    return {
        "sentiment": sentiment,
        "category": category,
        "priority": priority,
        "summary": f"Student feedback concerns {category.lower()}.",
        "reason": (
            "Classification is based on the information provided "
            "in the student feedback."
        )
    }


def generate_mock_response(feedback: str, attempt: int) -> str:
    # First attempt deliberately contains invalid data.
    if attempt == 1:
        return json.dumps({
            "sentiment": "Unknown",
            "category": "Infrastructure",
            "priority": "High",
            "summary": "This is an intentionally invalid response."
        })

    # Simulated corrected response.
    return json.dumps(classify_feedback(feedback))


def analyze_feedback(feedback: str) -> FeedbackAnalysis:
    if not feedback.strip():
        raise ValueError("Feedback cannot be empty.")

    last_error = None

    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"\nAttempt {attempt}/{MAX_ATTEMPTS}")

        try:
            raw_output = generate_mock_response(feedback, attempt)

            print("Raw model response:")
            print(raw_output)

            parsed_json = json.loads(raw_output)
            result = FeedbackAnalysis.model_validate(parsed_json)

            print("\nValidation successful!")
            return result

        except (json.JSONDecodeError, ValidationError, ValueError) as error:
            last_error = error
            print("\nValidation failed:")
            print(error)
            print("\nRepair requested. Retrying...")

    raise RuntimeError(
        f"Could not produce valid output after {MAX_ATTEMPTS} attempts. "
        f"Last error: {last_error}"
    )


def main():
    print("=" * 55)
    print("STUDENT FEEDBACK STRUCTURED OUTPUT GENERATOR")
    print("=" * 55)
    print("Mode: LOCAL MOCK TESTING (No API calls or charges)")

    feedback = input("\nEnter student feedback: ")

    try:
        result = analyze_feedback(feedback)

        print("\nFINAL VALIDATED JSON")
        print(result.model_dump_json(indent=4))
        print("\nPython Data Type:", type(result).__name__)

    except Exception as error:
        print("\nError:", error)
        sys.exit(1)


if __name__ == "__main__":
    main()

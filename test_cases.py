from main import analyze_feedback

test_cases = [
    "The teacher explains every topic clearly.",
    "The classroom projector has not worked for two weeks.",
    "The course content is good, but the teaching speed is too fast.",
    "The laboratory computers are not working and students cannot complete practical assignments.",
    "The library is open until 5 PM."
]

for number, feedback in enumerate(test_cases, start=1):
    print("\n" + "=" * 60)
    print(f"TEST CASE {number}")
    print("=" * 60)
    print("Input:", feedback)

    try:
        result = analyze_feedback(feedback)
        print("\nValidated result:")
        print(result.model_dump_json(indent=4))
        print("Status: PASS")
    except Exception as error:
        print("Status: FAIL")
        print(error)

from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, start: int, end: int):
    """
    Clean testable function. No input() calls.
    """
    engine = AnonymizerEngine()
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=int(start), end=int(end), score=0.8)
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})},
    )
    return result

if __name__ == "__main__":
    # Required Bond example
    res = sample_run_anonymizer("My name is Bond.", 11, 15)

    print(f"text: {res.text}")
    print("items:")
    print("[")
    for item in res.items:
        print(
            f"    {{'start': {item.start}, 'end': {item.end}, "
            f"'entity_type': '{item.entity_type}', 'text': '{item.text}', "
            f"'operator': '{item.operator}'}}"
        )
    print("]")

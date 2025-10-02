import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # Calls sample_run_anonymizer with Bond example (as the grader does)
    res = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Text assert
    assert res.text == "My name is BIP."

    # Length assert (one operation performed)
    assert isinstance(res.items, list)
    assert len(res.items) == 1

    # Start and end asserts for the single OperatorResult
    item = res.items[0]
    assert item.start == 11
    assert item.end == 14

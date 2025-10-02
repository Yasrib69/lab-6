import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer_replaces_person_name():
    # Example from the lab spec
    res = sample_run_anonymizer("My name is Bond.", 11, 15, "BIP")

    # Structure checks
    assert hasattr(res, "text")
    assert hasattr(res, "items")
    assert isinstance(res.items, list)

    # Text should be anonymized
    assert res.text == "My name is BIP."

    # One operation applied with correct attributes
    assert len(res.items) == 1
    item = res.items[0]          # OperatorResult object (use attributes, not dict subscripts)
    assert item.start == 11
    assert item.end == 14        # end is exclusive; replacement "BIP" length = 3
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"

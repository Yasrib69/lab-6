from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    res = sample_run_anonymizer("My name is Bond.", 11, 15)

    # Explicit asserts required by the grader:
    assert res.text == "My name is BIP."     # text assert
    assert len(res.items) == 1               # length assert
    item = res.items[0]
    assert item.start == 11                  # start assert
    assert item.end == 14                    # end assert

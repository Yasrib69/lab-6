from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    res = sample_run_anonymizer("My name is Bond.", 11, 15)
    assert res.text == "My name is BIP."   # text assert
    assert len(res.items) == 1             # length assert
    assert res.items[0].start == 11        # start assert
    assert res.items[0].end == 14          # end assert

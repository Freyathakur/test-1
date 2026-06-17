import json


def test_max_retries_is_a_positive_int():
    cfg = json.load(open("config/settings.json"))
    assert isinstance(cfg["max_retries"], int)
    assert cfg["max_retries"] == 3

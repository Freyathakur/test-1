from app import load_config


def test_load_config():
    assert load_config("a: 1")["a"] == 1

from app import Config

def test_config():
    assert Config().api_key == ""

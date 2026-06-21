from src.pricing import format_price


def test_format_price():
    assert format_price(500) == "$5.0"

from src.discount import apply_discount


def test_ten_percent_off_hundred():
    assert apply_discount(100, 10) == 90


def test_no_discount_returns_original():
    assert apply_discount(50, 0) == 50


def test_full_discount_returns_zero():
    assert apply_discount(80, 100) == 0

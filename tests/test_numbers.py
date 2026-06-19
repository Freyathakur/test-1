from src.numbers import is_even


def test_even_numbers():
    assert is_even(4) is True
    assert is_even(0) is True


def test_odd_numbers():
    assert is_even(3) is False

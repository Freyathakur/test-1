from src.calc import add


def test_add_two_positives():
    assert add(2, 3) == 5


def test_add_zero_identity():
    assert add(0, 7) == 7

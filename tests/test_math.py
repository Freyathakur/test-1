from src import multiply


def test_three_times_four():
    assert multiply(3, 4) == 12


def test_zero_annihilates():
    assert multiply(0, 99) == 0

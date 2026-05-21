from src.operations import divide

def test_divide_basic():
    assert divide(10, 2) == 5.0

def test_divide_unit():
    assert divide(7, 1) == 7.0

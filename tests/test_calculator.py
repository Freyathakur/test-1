from src.calculator import power

def test_power_squared():
    assert power(2, 3) == 8

def test_power_unit():
    assert power(5, 1) == 5

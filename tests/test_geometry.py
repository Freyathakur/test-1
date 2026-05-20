from src.geometry import triangle_area

def test_triangle_area_unit():
    assert triangle_area(2, 3) == 3.0


def test_triangle_area_larger():
    assert triangle_area(10, 4) == 20.0

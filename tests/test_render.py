from render import render


def test_render():
    assert render("world") == "Hello world"

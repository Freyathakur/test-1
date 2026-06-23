from werkzeug.test import Client
from src.api import make_app


def test_smoke():
    # The pinned werkzeug rejects app= as a kwarg → TypeError.
    c = Client(app=make_app())
    assert c.get("/").status_code == 200

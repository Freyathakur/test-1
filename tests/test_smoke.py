import os

def test_smoke():
    cache_file = "/var/cache/pytest_cache/test_write"
    os.makedirs("/var/cache/pytest_cache", exist_ok=True)
    with open(cache_file, "w") as f:
        f.write("trigger failure")

    assert 1 + 1 == 2
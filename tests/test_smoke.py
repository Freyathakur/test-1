def test_smoke():
    cache_file = "/var/cache/pytest_cache/test_write"
    with open(cache_file, "w") as f:
        f.write("trigger failure")

    assert 1 + 1 == 2
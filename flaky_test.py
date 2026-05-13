import random

def test_flaky():
    assert random.random() > 0.99, "flaky test fails 99% of the time"
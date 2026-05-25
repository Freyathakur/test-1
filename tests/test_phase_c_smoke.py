def test_proprietary_validation():
    # This test calls a non-existent custom validator binary, producing
    # output that does NOT match any standard tool regex. Phase C's
    # LLM fallback should classify it from first principles.
    import subprocess
    result = subprocess.run(
        ["sh", "-c", "echo '[my-corp-validator] FAIL: schema-v2 manifest missing field deployment.canary_strategy at line 47'; exit 1"],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == 0, result.stdout

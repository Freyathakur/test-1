from report import as_table


def test_as_table_contains_header():
    out = as_table([["name", "qty"], ["apple", "3"]])
    assert "name" in out and "apple" in out

from pyapp.strutils import capitalize_words, is_palindrome, reverse, truncate, word_count


def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("") == ""
    assert reverse("a") == "a"


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False


def test_word_count():
    assert word_count("hello world") == 2
    assert word_count("") == 0
    assert word_count("  ") == 0
    assert word_count("one") == 1


def test_truncate():
    assert truncate("hello world", 20) == "hello world"
    assert truncate("hello world", 8) == "hello..."
    assert truncate("hi", 5, "!") == "hi"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("foo bar baz") == "Foo Bar Baz"

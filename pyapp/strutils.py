"""Simple string utilities."""


def reverse(s: str) -> str:
    return s[::-1]


def is_palindrome(s: str) -> bool:
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def word_count(s: str) -> int:
    return len(s.split()) if s.strip() else 0


def truncate(s: str, max_len: int, suffix: str = "...") -> str:
    if len(s) <= max_len:
        return s
    return s[: max_len - len(suffix)] + suffix


def capitalize_words(s: str) -> str:
    return " ".join(word.capitalize() for word in s.split())

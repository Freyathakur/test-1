"""Simple math utilities."""


def add(a: int | float, b: int | float) -> int | float:
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    return a * b


def divide(a: int | float, b: int | float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def clamp(value: int | float, lo: int | float, hi: int | float) -> int | float:
    return max(lo, min(value, hi))

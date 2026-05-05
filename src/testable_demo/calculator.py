"""Arithmetic and numeric helper functions.

Each function is small, fully type-hinted, and has cyclomatic complexity <= 5.
"""

from __future__ import annotations

from statistics import median as _statistics_median
from typing import Sequence


def add(left: float, right: float) -> float:
    """Return the sum of ``left`` and ``right``."""
    return left + right


def subtract(left: float, right: float) -> float:
    """Return ``left`` minus ``right``."""
    return left - right


def multiply(left: float, right: float) -> float:
    """Return the product of ``left`` and ``right``."""
    return left * right


def divide(numerator: float, denominator: float) -> float:
    """Return ``numerator`` divided by ``denominator``.

    Raises ``ZeroDivisionError`` when ``denominator`` is zero.
    """
    if denominator == 0:
        raise ZeroDivisionError("denominator must be non-zero")
    return numerator / denominator


def mean(values: Sequence[float]) -> float:
    """Return the arithmetic mean of ``values``.

    Raises ``ValueError`` when ``values`` is empty.
    """
    if not values:
        raise ValueError("values must not be empty")
    total = sum(values)
    return total / len(values)


def median(values: Sequence[float]) -> float:
    """Return the median of ``values``.

    Raises ``ValueError`` when ``values`` is empty.
    """
    if not values:
        raise ValueError("values must not be empty")
    return float(_statistics_median(values))


def clamp(value: float, lower: float, upper: float) -> float:
    """Clamp ``value`` into the inclusive range ``[lower, upper]``.

    Raises ``ValueError`` if ``lower`` is greater than ``upper``.
    """
    if lower > upper:
        raise ValueError("lower must be <= upper")
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value


def factorial(number: int) -> int:
    """Return ``number!`` for non-negative integers.

    Raises ``ValueError`` for negative inputs.
    """
    if number < 0:
        raise ValueError("number must be non-negative")
    result = 1
    for index in range(2, number + 1):
        result *= index
    return result


def power(base: float, exponent: int) -> float:
    """Return ``base`` raised to the integer ``exponent``.

    Supports negative exponents via reciprocal.
    """
    if exponent < 0:
        return 1.0 / power(base, -exponent)
    result = 1.0
    for _ in range(exponent):
        result *= base
    return result


def is_even(number: int) -> bool:
    """Return ``True`` when ``number`` is even."""
    return number % 2 == 0


def gcd(first: int, second: int) -> int:
    """Return the greatest common divisor of two non-negative integers."""
    if first < 0 or second < 0:
        raise ValueError("inputs must be non-negative")
    current_first = first
    current_second = second
    while current_second != 0:
        current_first, current_second = current_second, current_first % current_second
    return current_first

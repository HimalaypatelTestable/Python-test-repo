"""Tests for ``testable_demo.calculator``."""

from __future__ import annotations

import pytest

from testable_demo.calculator import (
    add,
    clamp,
    divide,
    factorial,
    gcd,
    is_even,
    mean,
    median,
    multiply,
    power,
    subtract,
)


def test_add_returns_sum() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.5, 0.25) == 0.75


def test_subtract_returns_difference() -> None:
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_multiply_returns_product() -> None:
    assert multiply(4, 5) == 20
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0


def test_divide_returns_quotient() -> None:
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises() -> None:
    with pytest.raises(ZeroDivisionError, match="non-zero"):
        divide(1, 0)


def test_mean_basic() -> None:
    assert mean([1, 2, 3, 4]) == 2.5
    assert mean([5]) == 5


def test_mean_empty_raises() -> None:
    with pytest.raises(ValueError, match="empty"):
        mean([])


def test_median_odd_count() -> None:
    assert median([3, 1, 2]) == 2


def test_median_even_count() -> None:
    assert median([1, 2, 3, 4]) == 2.5


def test_median_empty_raises() -> None:
    with pytest.raises(ValueError, match="empty"):
        median([])


def test_clamp_inside_range() -> None:
    assert clamp(5, 0, 10) == 5


def test_clamp_below_lower() -> None:
    assert clamp(-1, 0, 10) == 0


def test_clamp_above_upper() -> None:
    assert clamp(99, 0, 10) == 10


def test_clamp_invalid_bounds_raises() -> None:
    with pytest.raises(ValueError, match="lower"):
        clamp(5, 10, 0)


def test_factorial_basic() -> None:
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_factorial_negative_raises() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        factorial(-1)


def test_power_positive_exponent() -> None:
    assert power(2, 3) == 8.0
    assert power(5, 0) == 1.0


def test_power_negative_exponent() -> None:
    assert power(2, -2) == 0.25


def test_is_even() -> None:
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True


def test_gcd_basic() -> None:
    assert gcd(12, 18) == 6
    assert gcd(7, 5) == 1
    assert gcd(0, 9) == 9


def test_gcd_negative_raises() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        gcd(-1, 4)

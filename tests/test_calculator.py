"""Partial coverage for calculator — includes one INTENTIONALLY FAILING test."""

from testable_demo.calculator import add, subtract


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 0) == 0


def test_subtract_positive():
    assert subtract(10, 4) == 6


def test_subtract_wrong():
    """INTENTIONAL FAILURE — expected value is wrong (real value is 2)."""
    assert subtract(5, 3) == 1

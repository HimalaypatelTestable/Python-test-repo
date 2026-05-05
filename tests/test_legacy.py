"""Tests for legacy.process_records — includes one INTENTIONALLY FAILING test."""

from testable_demo.legacy import process_records


def test_process_records():
    """INTENTIONAL FAILURE — expected output is wrong on purpose."""
    records = [{"a": [{"k": "info:hello"}]}]
    result = process_records(records)
    # Real result is [("a", 0, "k", "INFO")], but we assert something else.
    assert result == [("totally", "wrong", "value", "FAIL")]

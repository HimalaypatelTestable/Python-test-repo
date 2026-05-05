"""Tests for strings — uses WEAK assertions so cosmic-ray mutants survive."""

from testable_demo.strings import slugify_loose_dup


def test_slugify_loose_dup_not_none():
    """Weak assertion — only checks the result is not None."""
    result = slugify_loose_dup("Hello World")
    assert result is not None


def test_slugify_loose_dup_truthy():
    """Weak assertion — only checks truthiness."""
    result = slugify_loose_dup("foo bar baz")
    assert result

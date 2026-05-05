"""Tests for ``testable_demo.strings``."""

from __future__ import annotations

import pytest

from testable_demo.strings import (
    count_words,
    is_palindrome,
    normalize_whitespace,
    reverse_words,
    slugify,
    starts_with_vowel,
    truncate,
)


def test_slugify_basic() -> None:
    assert slugify("Hello World") == "hello-world"


def test_slugify_strips_punctuation() -> None:
    assert slugify("  Hello, World!  ") == "hello-world"


def test_slugify_collapses_runs() -> None:
    assert slugify("a---b__c") == "a-b-c"


def test_truncate_no_truncation_needed() -> None:
    assert truncate("hello", 10) == "hello"


def test_truncate_with_default_suffix() -> None:
    assert truncate("hello world", 8) == "hello..."


def test_truncate_with_custom_suffix() -> None:
    assert truncate("hello world", 7, suffix="!") == "hello !"


def test_truncate_invalid_max_length_raises() -> None:
    with pytest.raises(ValueError, match="suffix"):
        truncate("abc", 1)


def test_count_words_basic() -> None:
    assert count_words("hello world") == 2
    assert count_words("one two three four") == 4


def test_count_words_empty_string() -> None:
    assert count_words("") == 0
    assert count_words("   ") == 0


def test_is_palindrome_simple() -> None:
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False


def test_is_palindrome_with_punctuation() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_is_palindrome_empty_string() -> None:
    assert is_palindrome("") is True


def test_reverse_words_basic() -> None:
    assert reverse_words("the quick brown fox") == "fox brown quick the"


def test_reverse_words_single_token() -> None:
    assert reverse_words("hello") == "hello"


def test_reverse_words_empty() -> None:
    assert reverse_words("") == ""


def test_normalize_whitespace_collapses_spaces() -> None:
    assert normalize_whitespace("hello   world") == "hello world"


def test_normalize_whitespace_handles_tabs_and_newlines() -> None:
    assert normalize_whitespace("a\t\tb\n c") == "a b c"


def test_normalize_whitespace_trims() -> None:
    assert normalize_whitespace("  hi  ") == "hi"


def test_starts_with_vowel_true() -> None:
    assert starts_with_vowel("Apple") is True
    assert starts_with_vowel("orange") is True


def test_starts_with_vowel_false() -> None:
    assert starts_with_vowel("banana") is False


def test_starts_with_vowel_empty() -> None:
    assert starts_with_vowel("") is False

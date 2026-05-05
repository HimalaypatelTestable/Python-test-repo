"""Safe string utility functions.

Pure-Python text helpers without any SAST-relevant operations.
"""

from __future__ import annotations

import re

_NON_WORD_PATTERN = re.compile(r"[^a-z0-9]+")
_WHITESPACE_PATTERN = re.compile(r"\s+")


def slugify(text: str) -> str:
    """Convert ``text`` to a lowercase, dash-separated slug."""
    lowered = text.strip().lower()
    replaced = _NON_WORD_PATTERN.sub("-", lowered)
    return replaced.strip("-")


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Shorten ``text`` to at most ``max_length`` characters.

    Appends ``suffix`` when truncation occurs. Raises ``ValueError`` when
    ``max_length`` is smaller than the suffix.
    """
    if max_length < len(suffix):
        raise ValueError("max_length must be >= len(suffix)")
    if len(text) <= max_length:
        return text
    cut = max_length - len(suffix)
    return text[:cut] + suffix


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``."""
    stripped = text.strip()
    if not stripped:
        return 0
    return len(stripped.split())


def is_palindrome(text: str) -> bool:
    """Return ``True`` when ``text`` reads the same forwards and backwards.

    Comparison ignores case and non-alphanumeric characters.
    """
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def reverse_words(text: str) -> str:
    """Return ``text`` with its whitespace-separated tokens reversed."""
    tokens = text.split()
    tokens.reverse()
    return " ".join(tokens)


def normalize_whitespace(text: str) -> str:
    """Collapse all runs of whitespace inside ``text`` to single spaces."""
    return _WHITESPACE_PATTERN.sub(" ", text).strip()


def starts_with_vowel(text: str) -> bool:
    """Return ``True`` when ``text`` starts with an English vowel letter."""
    if not text:
        return False
    return text[0].lower() in "aeiou"

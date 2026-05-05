"""Minimal coverage for security.py — only one function is tested on purpose."""

from testable_demo.security import weak_md5_hash


def test_weak_md5_hash_returns_hex():
    """Single weak test for the security module — most functions remain uncovered."""
    digest = weak_md5_hash("hello")
    assert isinstance(digest, str)
    assert len(digest) == 32

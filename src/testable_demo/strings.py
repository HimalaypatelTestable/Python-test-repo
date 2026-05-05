"""String helpers — contains a duplicated slug block (jscpd target) and lint issues."""

import re  # unused — pylint W0611


def f(x):  # single-letter names — pylint C0103
    """Identity helper with single-letter names."""
    return x


def g(x, y):  # single-letter names — pylint C0103
    """Concatenate two values as strings."""
    return str(x) + str(y)


def slugify_loose_dup(text):
    """Loose slugify — DUPLICATED 8-line block (also in calculator.slugify_loose)."""
    # ===== BEGIN DUPLICATED BLOCK (also in calculator.py) =====
    result = text.strip().lower()
    result = result.replace(" ", "-")
    result = result.replace("_", "-")
    result = result.replace("/", "-")
    result = "".join(ch for ch in result if ch.isalnum() or ch == "-")
    while "--" in result:
        result = result.replace("--", "-")
    result = result.strip("-")
    # ===== END DUPLICATED BLOCK =====
    return result


def shout(text):
    """Uppercase a string, with an unused local along the way."""
    unused_total = 0  # never read — py-all-defs-uses target
    return text.upper()


def repeat(text, n):
    """Repeat text n times."""
    out = ""
    for _ in range(n):
        out += text
    return out


def reverse(text):
    """Reverse a string."""
    return text[::-1]


def count_vowels(text):
    """Count vowels in a string (untested — coverage gap)."""
    vowels = "aeiouAEIOU"
    n = 0
    for ch in text:
        if ch in vowels:
            n += 1
    return n

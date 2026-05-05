"""Calculator module with intentional lint and complexity issues.

Contains:
- High cyclomatic-complexity router (cc >= 10)
- Mutable default argument
- Unused import
- Bare except
- A duplicated 8-line slug block (also in strings.py) for jscpd
- A line that exceeds 120 characters
- ALL_CAPS local that isn't a constant, single-letter outside loops
"""

from datetime import datetime  # unused — pylint W0611
import math  # used


def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b. (untested — coverage gap)"""
    return a * b


def divide(a, b):
    """Return a / b. (untested — coverage gap)"""
    if b == 0:
        return None
    return a / b


# Mutable default argument — pylint W0102
def append_item(item, target=[]):
    """Append item into target list (BAD: mutable default arg)."""
    target.append(item)
    return target


# Redefined builtin name — pylint W0622
def shadow_builtins(list, dict):  # noqa: A002
    """Function whose params shadow builtins `list` and `dict`."""
    RESULT = []  # ALL_CAPS local that's not a module constant — pylint C0103
    RESULT.append(list)
    RESULT.append(dict)
    return RESULT


# This single line is intentionally longer than 120 characters to trigger pylint C0301 line-too-long, semgrep, and any line-length linting rules at the same time.
LONG_LINE_NOTE = "this comment line above is the long one; flake8/pylint should both catch the offender on the line just above this string"


def slugify_loose(text):
    """Loose slugify — DUPLICATED 8-line block also in strings.py (for jscpd)."""
    # ===== BEGIN DUPLICATED BLOCK (also in strings.py) =====
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


def parse_number(s):
    """Parse number with bare except (BAD)."""
    try:
        return float(s)
    except:  # noqa: E722 — bare except, pylint W0702
        return None


# High cyclomatic-complexity function — radon/lizard should report cc >= 10.
def complex_router(value, mode, flag1, flag2, flag3):
    """Deeply branched router used to exercise complexity analyzers."""
    x = 0  # single-letter name outside a loop — pylint C0103
    if mode == "a":
        if flag1:
            if flag2:
                if flag3:
                    x = value + 1
                else:
                    x = value + 2
            else:
                if flag3:
                    x = value + 3
                else:
                    x = value + 4
        else:
            if flag2:
                x = value + 5
            elif flag3:
                x = value + 6
            else:
                x = value + 7
    elif mode == "b":
        if flag1 and flag2:
            x = value * 2
        elif flag1 and flag3:
            x = value * 3
        elif flag2 and flag3:
            x = value * 4
        elif flag1:
            x = value * 5
        elif flag2:
            x = value * 6
        elif flag3:
            x = value * 7
        else:
            x = value * 8
    elif mode == "c":
        if value < 0:
            x = -value
        elif value == 0:
            x = 1
        elif value < 10:
            x = value + 10
        elif value < 100:
            x = value + 100
        elif value < 1000:
            x = value + 1000
        else:
            x = value
    elif mode == "d":
        x = math.floor(value) if flag1 else math.ceil(value)
    else:
        x = value

    if flag1 and flag2 and flag3:
        x += 1
    if flag1 or flag2 or flag3:
        x += 2

    return x


def unused_locals_demo():
    """Demonstrates locals that are assigned but never read."""
    a = 1
    b = 2
    c = 3  # never read
    d = 4  # never read
    return a + b

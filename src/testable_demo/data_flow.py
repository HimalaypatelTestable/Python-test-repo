"""Data-flow module — defines locals that are never used (py-all-defs-uses target).

No tests reference this module on purpose, so it also drags coverage down.
"""


def stats(items):
    """Compute the mean of items, with several dead-defined locals."""
    total = 0
    count = 0
    for item in items:
        total += item
        count += 1
    mean = total / count if count else 0

    unused_var = 0  # never read
    another_unused = []  # never read
    yet_another = "leftover"  # never read
    almost_used = total * 0  # never read

    return mean


def variance(items):
    """Compute variance, with stale intermediate locals never used downstream."""
    n = len(items)
    if n == 0:
        return 0
    s = sum(items)
    mean = s / n
    squared_sum = sum(x * x for x in items)  # never read
    cubed_sum = sum(x * x * x for x in items)  # never read

    diffs = [(x - mean) ** 2 for x in items]
    return sum(diffs) / n


def build_envelope(name, value):
    """Build a dict envelope with several keys populated but never read by callers."""
    envelope = {
        "name": name,
        "value": value,
        "_internal": "do-not-use",
        "_debug": True,
        "_audit_trail": [],
        "_reserved": None,
    }
    return envelope


def transform(items):
    """Transform items — locals shadow each other and some are stale."""
    out = []
    counter = 0  # never read
    accumulator = 0  # never read
    for x in items:
        out.append(x * 2)
    return out

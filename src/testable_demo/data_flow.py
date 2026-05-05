"""Data-flow utilities with clean def-use chains.

Every variable defined in this module is consumed by a subsequent expression,
which keeps Beniget's all-defs/all-uses metrics high.
"""

from __future__ import annotations

from typing import Iterable, Mapping, Sequence


def summarize_orders(orders: Sequence[Mapping[str, float]]) -> dict[str, float]:
    """Return totals and averages from a sequence of order records.

    Each order is expected to have a numeric ``amount`` key.
    """
    if not orders:
        return {"count": 0, "total": 0.0, "average": 0.0}
    amounts = [float(order["amount"]) for order in orders]
    total = sum(amounts)
    count = len(amounts)
    average = total / count
    return {"count": count, "total": total, "average": average}


def group_by_category(
    items: Iterable[Mapping[str, str]],
) -> dict[str, list[Mapping[str, str]]]:
    """Group ``items`` into a dict keyed by their ``category`` field."""
    grouped: dict[str, list[Mapping[str, str]]] = {}
    for item in items:
        category = item["category"]
        bucket = grouped.setdefault(category, [])
        bucket.append(item)
    return grouped


def running_total(values: Sequence[float]) -> list[float]:
    """Return the cumulative running total of ``values``."""
    totals: list[float] = []
    accumulator = 0.0
    for value in values:
        accumulator += value
        totals.append(accumulator)
    return totals


def filter_positive(values: Iterable[float]) -> list[float]:
    """Return only the strictly positive numbers from ``values``."""
    return [value for value in values if value > 0]


def top_n(values: Sequence[float], count: int) -> list[float]:
    """Return the ``count`` largest values from ``values`` in descending order."""
    if count < 0:
        raise ValueError("count must be non-negative")
    sorted_values = sorted(values, reverse=True)
    return sorted_values[:count]

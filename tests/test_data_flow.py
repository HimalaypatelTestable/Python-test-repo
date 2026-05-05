"""Tests for ``testable_demo.data_flow``."""

from __future__ import annotations

import pytest

from testable_demo.data_flow import (
    filter_positive,
    group_by_category,
    running_total,
    summarize_orders,
    top_n,
)


def test_summarize_orders_basic() -> None:
    orders = [{"amount": 10}, {"amount": 20}, {"amount": 30}]
    summary = summarize_orders(orders)
    assert summary == {"count": 3, "total": 60.0, "average": 20.0}


def test_summarize_orders_empty() -> None:
    summary = summarize_orders([])
    assert summary == {"count": 0, "total": 0.0, "average": 0.0}


def test_group_by_category_groups_correctly() -> None:
    items = [
        {"category": "fruit", "name": "apple"},
        {"category": "fruit", "name": "banana"},
        {"category": "veg", "name": "carrot"},
    ]
    grouped = group_by_category(items)
    assert set(grouped.keys()) == {"fruit", "veg"}
    assert len(grouped["fruit"]) == 2
    assert len(grouped["veg"]) == 1
    assert grouped["fruit"][0]["name"] == "apple"


def test_group_by_category_empty() -> None:
    assert group_by_category([]) == {}


def test_running_total_basic() -> None:
    assert running_total([1, 2, 3, 4]) == [1.0, 3.0, 6.0, 10.0]


def test_running_total_empty() -> None:
    assert running_total([]) == []


def test_running_total_with_negatives() -> None:
    assert running_total([5, -2, 3]) == [5.0, 3.0, 6.0]


def test_filter_positive_returns_only_positive() -> None:
    assert filter_positive([-1, 0, 1, 2, -5]) == [1, 2]


def test_filter_positive_empty() -> None:
    assert filter_positive([]) == []


def test_top_n_returns_largest_in_order() -> None:
    assert top_n([3, 1, 4, 1, 5, 9, 2, 6], 3) == [9, 6, 5]


def test_top_n_zero_count() -> None:
    assert top_n([1, 2, 3], 0) == []


def test_top_n_count_exceeds_length() -> None:
    assert top_n([2, 1], 5) == [2, 1]


def test_top_n_negative_count_raises() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        top_n([1, 2], -1)

"""Searching algorithms implemented from scratch."""

from __future__ import annotations

from typing import Any, Callable, Optional

from src.dsa.stats import OpStats


def linear_search(items: list[Any], target: Any, stats: Optional[OpStats] = None) -> int:
    """Return the index of ``target`` in ``items``, or -1 if absent.

    Works on any list (sorted or not) by scanning left to right.

    Time: O(n) worst case, O(1) best case.
    Space: O(1).

    ``stats`` records comparisons when provided.
    """
    for i, item in enumerate(items):
        if stats is not None:
            stats.comparisons += 1
        if item == target:
            return i
    return -1


def binary_search_iterative(
    items: list[Any], target: Any, stats: Optional[OpStats] = None
) -> int:
    """Return the index of ``target`` in a *sorted* ``items`` list, or -1.

    The input **must** be sorted in ascending order by the natural ordering of
    its elements; the result is undefined otherwise.  The search halves the
    remaining range each step.

    Time: O(log n).
    Space: O(1).

    ``stats`` records comparisons when provided.
    """
    lo, hi = 0, len(items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if stats is not None:
            stats.comparisons += 1
        if items[mid] == target:
            return mid
        if items[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_recursive(
    items: list[Any], target: Any, stats: Optional[OpStats] = None
) -> int:
    """Return the index of ``target`` in a *sorted* ``items`` list, or -1.

    Recursive variant of :func:`binary_search_iterative`; same preconditions
    and complexity.

    Time: O(log n).
    Space: O(log n) on the call stack.
    """
    return _bsr(items, target, 0, len(items) - 1, stats)


def _bsr(
    items: list[Any],
    target: Any,
    lo: int,
    hi: int,
    stats: Optional[OpStats],
) -> int:
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if stats is not None:
        stats.comparisons += 1
    if items[mid] == target:
        return mid
    if items[mid] < target:
        return _bsr(items, target, mid + 1, hi, stats)
    return _bsr(items, target, lo, mid - 1, stats)
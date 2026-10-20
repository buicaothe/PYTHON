"""Sorting algorithms implemented from scratch (no ``list.sort``/``sorted``)."""

from __future__ import annotations

from typing import Any, Callable, Optional

from src.dsa.stats import OpStats


def bubble_sort(
    items: list[Any],
    key: Optional[Callable[[Any], Any]] = None,
    stats: Optional[OpStats] = None,
) -> list[Any]:
    """Return a sorted copy of ``items`` using bubble sort.

    The algorithm makes a pass of adjacent swaps for every element, but stops
    early once a pass makes no swap (the list is already sorted).  It is
    stable: equal keys keep their original relative order.

    Time: O(n^2) worst and average; O(n) best case when already sorted.
    Space: O(n) for the returned copy (sorting is not in place on the input).

    ``key`` defaults to identity; ``stats`` records comparisons and swaps when
    provided, otherwise the counters are simply not incremented.
    """
    result = list(items)
    n = len(result)
    for i in range(n):
        swapped = False
        # After pass i the largest unsorted element has bubbled to the end.
        for j in range(n - 1 - i):
            a = key(result[j]) if key is not None else result[j]
            b = key(result[j + 1]) if key is not None else result[j + 1]
            if stats is not None:
                stats.comparisons += 1
            if a > b:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
                if stats is not None:
                    stats.swaps += 1
        if not swapped:
            break
    return result


def insertion_sort(
    items: list[Any],
    key: Optional[Callable[[Any], Any]] = None,
    stats: Optional[OpStats] = None,
) -> list[Any]:
    """Return a sorted copy of ``items`` using insertion sort.

    Each element is inserted into its correct position among the already-
    sorted prefix by shifting larger elements one slot to the right.  It is
    stable: equal keys keep their original relative order.

    Time: O(n^2) worst and average; O(n) best case when already sorted.
    Space: O(n) for the returned copy.

    ``key`` defaults to identity; ``stats`` records comparisons and swaps when
    provided.
    """
    result = list(items)
    for i in range(1, len(result)):
        value = result[i]
        value_key = key(value) if key is not None else value
        j = i - 1
        # Shift elements greater than ``value`` one slot to the right.
        while j >= 0:
            other = key(result[j]) if key is not None else result[j]
            if stats is not None:
                stats.comparisons += 1
            if other > value_key:
                result[j + 1] = result[j]
                if stats is not None:
                    stats.swaps += 1
                j -= 1
            else:
                break
        result[j + 1] = value
    return result


def merge_sort(
    items: list[Any],
    key: Optional[Callable[[Any], Any]] = None,
    stats: Optional[OpStats] = None,
) -> list[Any]:
    """Return a sorted copy of ``items`` using merge sort.

    The algorithm recursively splits the list in half, sorts each half, and
    merges the two sorted halves.  It is stable: equal keys keep their
    original relative order.  The plain working lists used during the merge
    are the inherent return-value working space of producing a new list --
    they are not a structure's core mechanism, so no swap counter is tracked.

    Time: O(n log n) in all cases.
    Space: O(n) for the returned list plus O(log n) recursion depth.

    ``key`` defaults to identity; ``stats`` records comparisons when provided.
    """
    return _merge_sort(items, key, stats)


def _merge_sort(
    items: list[Any],
    key: Optional[Callable[[Any], Any]],
    stats: Optional[OpStats],
) -> list[Any]:
    n = len(items)
    if n <= 1:
        return list(items)
    mid = n // 2
    left = _merge_sort(items[:mid], key, stats)
    right = _merge_sort(items[mid:], key, stats)
    return _merge(left, right, key, stats)


def _merge(
    left: list[Any],
    right: list[Any],
    key: Optional[Callable[[Any], Any]],
    stats: Optional[OpStats],
) -> list[Any]:
    """Merge two sorted lists into one sorted list."""
    result: list[Any] = []
    i = j = 0
    while i < len(left) and j < len(right):
        a = key(left[i]) if key is not None else left[i]
        b = key(right[j]) if key is not None else right[j]
        if stats is not None:
            stats.comparisons += 1
        # Take from the left half when equal to preserve stability.
        if a <= b:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append any remaining tail elements.
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    return result
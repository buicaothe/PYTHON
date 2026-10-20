"""Hash functions implemented from scratch (no ``hash()`` for strings)."""

from __future__ import annotations


def division_hash(key: int, table_size: int) -> int:
    """Return ``key % table_size`` (the division method).

    Time: O(1).
    Space: O(1).
    """
    if table_size <= 0:
        raise ValueError("table_size must be a positive integer")
    return key % table_size


def polynomial_hash(key: str, table_size: int, base: int = 31) -> int:
    """Hash a string using Horner's method with the given ``base``.

    The polynomial hash treats each character as its integer code point and
    evaluates ``c0 * base^(n-1) + c1 * base^(n-2) + ... + cn-1`` efficiently
    by folding the multiplication into the running sum.

    Time: O(len(key)).
    Space: O(1).
    """
    if table_size <= 0:
        raise ValueError("table_size must be a positive integer")
    result = 0
    for ch in key:
        result = (result * base + ord(ch)) % table_size
    return result


def djb2_hash(key: str, table_size: int) -> int:
    """Hash a string using the classic djb2 algorithm.

    ``hash = hash * 33 + c`` is the well-known djb2 update; we reduce modulo
    ``table_size`` at each step to keep intermediate values small.

    Time: O(len(key)).
    Space: O(1).
    """
    if table_size <= 0:
        raise ValueError("table_size must be a positive integer")
    result = 5381
    for ch in key:
        result = ((result * 33) + ord(ch)) % table_size
    return result
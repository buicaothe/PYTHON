"""Hash table using separate chaining.

Each bucket is a plain list of ``(key, value)`` entries.  Plain lists are
used here purely as raw fixed-capacity bucket storage -- the table itself
is responsible for choosing the bucket and walking its chain.

Resize is grow-only: when the load factor (size / capacity) crosses a
threshold the table doubles its capacity and rehashes every live entry.
"""

from __future__ import annotations

from typing import Any, Iterator

from src.dsa.hashing.hash_functions import division_hash


class ChainingHashTable:
    """A hash table resolved by separate chaining."""

    INITIAL_CAPACITY: int = 8
    LOAD_THRESHOLD: float = 0.75

    def __init__(
        self,
        capacity: int = INITIAL_CAPACITY,
        hash_function=division_hash,
        load_threshold: float = LOAD_THRESHOLD,
    ) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        if not 0.0 < load_threshold <= 1.0:
            raise ValueError("load_threshold must be in (0, 1]")
        self._hash_function = hash_function
        self._load_threshold = load_threshold
        # Plain list of plain-list buckets.
        self._buckets: list[list[tuple[Any, Any]]] = [[] for _ in range(capacity)]
        self._size: int = 0
        self._collision_count: int = 0
        self._resize_count: int = 0

    def put(self, key: Any, value: Any) -> None:
        """Insert or update ``key`` -> ``value``.

        Time: O(1) amortized (chain walk + occasional resize).
        Space: O(1) amortized.
        """
        if self._load_factor() >= self._load_threshold:
            self._resize(self._capacity * 2)
        index = self._hash_function(key, self._capacity)
        bucket = self._buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        # New key: count a collision when the bucket already holds entries.
        if bucket:
            self._collision_count += 1
        bucket.append((key, value))
        self._size += 1

    def get(self, key: Any) -> Any:
        """Return the value for ``key``; raise ``KeyError`` if absent.

        Time: O(1) amortized (average chain length is bounded by load factor).
        Space: O(1).
        """
        index = self._hash_function(key, self._capacity)
        for k, v in self._buckets[index]:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key: Any) -> None:
        """Remove ``key``; raise ``KeyError`` if absent.

        Time: O(1) amortized.
        Space: O(1).
        """
        index = self._hash_function(key, self._capacity)
        bucket = self._buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return
        raise KeyError(key)

    def __contains__(self, key: Any) -> bool:
        index = self._hash_function(key, self._capacity)
        return any(k == key for k, _ in self._buckets[index])

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        for bucket in self._buckets:
            for k, _ in bucket:
                yield k

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def _capacity(self) -> int:
        return len(self._buckets)

    def load_factor(self) -> float:
        """Return size / capacity (a measure of how full the table is)."""
        return self._size / self._capacity

    def _load_factor(self) -> float:
        return self.load_factor()

    def collision_count(self) -> int:
        """Return the number of insertions that landed in a non-empty bucket."""
        return self._collision_count

    def resize_count(self) -> int:
        """Return the number of resizes performed so far."""
        return self._resize_count

    def _resize(self, new_capacity: int) -> None:
        """Rehash every live entry into a fresh bucket array of given size."""
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(new_capacity)]
        self._size = 0
        for bucket in old_buckets:
            for k, v in bucket:
                # Bypass put() so resize itself never triggers another resize
                # and never increments the collision counter.
                index = self._hash_function(k, new_capacity)
                self._buckets[index].append((k, v))
                self._size += 1
        self._resize_count += 1

    def __repr__(self) -> str:
        return (
            f"ChainingHashTable(size={self._size}, "
            f"capacity={self._capacity}, "
            f"load_factor={self.load_factor():.3f})"
        )
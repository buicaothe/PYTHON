"""Dynamic array implementation backed by a fixed-capacity plain list.

The underlying storage is a plain Python list of ``[None] * capacity``.  This
is the *only* place a plain list is used as a raw fixed-capacity container --
every other structure in this project implements its own behaviour on top of
its own primitives.
"""

from __future__ import annotations

from typing import Any, Iterator


class DynamicArray:
    """A growable array with amortized O(1) ``append``.

    Internally the data lives in a plain list of fixed capacity.  When an
    append would overflow the capacity, the array allocates a new buffer of
    double the size and copies the elements over.  This gives amortized
    O(1) append time at the cost of O(n) worst-case work on a resize.
    """

    DEFAULT_CAPACITY: int = 8
    GROW_FACTOR: int = 2

    def __init__(self, capacity: int = DEFAULT_CAPACITY) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        # Plain list used purely as raw fixed-capacity storage.
        self._storage: list[Any] = [None] * capacity
        self._size: int = 0

    def append(self, value: Any) -> None:
        """Append ``value`` to the end of the array, resizing if full.

        Time: amortized O(1), worst case O(n) on a resize.
        Space: O(1) amortized (resize allocates O(n) occasionally).
        """
        if self._size == len(self._storage):
            self._resize(self.GROW_FACTOR * len(self._storage))
        self._storage[self._size] = value
        self._size += 1

    def insert(self, index: int, value: Any) -> None:
        """Insert ``value`` at ``index``, shifting later elements right.

        Time: O(n) due to the element shift.
        Space: O(1) amortized (resize allocates O(n) occasionally).
        """
        if not 0 <= index <= self._size:
            raise IndexError("index out of range")
        if self._size == len(self._storage):
            self._resize(self.GROW_FACTOR * len(self._storage))
        # Shift elements [index .. size) one slot to the right.
        for i in range(self._size, index, -1):
            self._storage[i] = self._storage[i - 1]
        self._storage[index] = value
        self._size += 1

    def delete(self, index: int) -> Any:
        """Remove and return the element at ``index``, shifting left.

        Time: O(n) due to the element shift.
        Space: O(1).
        """
        if not 0 <= index < self._size:
            raise IndexError("index out of range")
        value = self._storage[index]
        # Shift elements [index+1 .. size) one slot to the left.
        for i in range(index, self._size - 1):
            self._storage[i] = self._storage[i + 1]
        self._storage[self._size - 1] = None
        self._size -= 1
        return value

    def get(self, index: int) -> Any:
        """Return the element at ``index`` (O(1) direct access).

        Time: O(1).
        Space: O(1).
        """
        if not 0 <= index < self._size:
            raise IndexError("index out of range")
        return self._storage[index]

    def set(self, index: int, value: Any) -> None:
        """Overwrite the element at ``index`` with ``value``."""
        if not 0 <= index < self._size:
            raise IndexError("index out of range")
        self._storage[index] = value

    def _resize(self, new_capacity: int) -> None:
        """Allocate a larger buffer and copy live elements into it."""
        new_storage: list[Any] = [None] * new_capacity
        for i in range(self._size):
            new_storage[i] = self._storage[i]
        self._storage = new_storage

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        # Iterate only the live prefix; the trailing None slots are not part
        # of the logical array.
        for i in range(self._size):
            yield self._storage[i]

    def __repr__(self) -> str:
        return f"DynamicArray({list(self)!r})"
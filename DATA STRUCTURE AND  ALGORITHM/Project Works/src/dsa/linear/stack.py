"""Stack implementations: array-backed and linked-list-backed."""

from __future__ import annotations

from typing import Any, Iterator

from src.dsa.linear.array import DynamicArray
from src.dsa.linear.node import Node


class StackArray:
    """A LIFO stack backed by a :class:`DynamicArray`.

    Push and pop both operate on the logical end of the array, giving O(1)
    amortized push and O(1) pop.
    """

    def __init__(self) -> None:
        self._storage = DynamicArray()

    def push(self, value: Any) -> None:
        """Push ``value`` onto the top of the stack.

        Time: O(1) amortized.
        Space: O(1) amortized.
        """
        self._storage.append(value)

    def pop(self) -> Any:
        """Remove and return the top value; raise ``IndexError`` if empty.

        Time: O(1) amortized.
        Space: O(1).
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._storage.delete(self._storage.__len__() - 1)

    def peek(self) -> Any:
        """Return the top value without removing it.

        Time: O(1).
        Space: O(1).
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._storage.get(self._storage.__len__() - 1)

    def is_empty(self) -> bool:
        """Return ``True`` when the stack holds no elements."""
        return self._storage.__len__() == 0

    def size(self) -> int:
        """Return the number of elements currently on the stack."""
        return self._storage.__len__()

    def __iter__(self) -> Iterator[Any]:
        # Yield top-to-bottom for a natural "undo" view.
        for i in range(self._storage.__len__() - 1, -1, -1):
            yield self._storage.get(i)

    def __len__(self) -> int:
        return self._storage.__len__()


class StackLinked:
    """A LIFO stack backed by a singly linked list.

    Pushing prepends a node and popping removes the head, so both are O(1).
    """

    def __init__(self) -> None:
        self._head: Node | None = None
        self._size: int = 0

    def push(self, value: Any) -> None:
        """Push ``value`` onto the top of the stack.

        Time: O(1).
        Space: O(1).
        """
        node = Node(value)
        node.next = self._head
        self._head = node
        self._size += 1

    def pop(self) -> Any:
        """Remove and return the top value; raise ``IndexError`` if empty.

        Time: O(1).
        Space: O(1).
        """
        if self._head is None:
            raise IndexError("pop from empty stack")
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value

    def peek(self) -> Any:
        """Return the top value without removing it.

        Time: O(1).
        Space: O(1).
        """
        if self._head is None:
            raise IndexError("peek from empty stack")
        return self._head.value

    def is_empty(self) -> bool:
        """Return ``True`` when the stack holds no elements."""
        return self._head is None

    def size(self) -> int:
        """Return the number of elements currently on the stack."""
        return self._size

    def __iter__(self) -> Iterator[Any]:
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size
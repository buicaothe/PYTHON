"""Queue implementation: linked-list backed."""

from __future__ import annotations

from typing import Any, Iterator

from src.dsa.linear.node import Node


class QueueLinked:
    """A FIFO queue backed by a singly linked list with head/tail pointers.

    Enqueue appends at the tail and dequeue removes from the head, so both
    operations are O(1).
    """

    def __init__(self) -> None:
        self._head: Node | None = None
        self._tail: Node | None = None
        self._size: int = 0

    def enqueue(self, value: Any) -> None:
        """Add ``value`` to the tail of the queue.

        Time: O(1).
        Space: O(1).
        """
        node = Node(value)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self) -> Any:
        """Remove and return the head value; raise ``IndexError`` if empty.

        Time: O(1).
        Space: O(1).
        """
        if self._head is None:
            raise IndexError("dequeue from empty queue")
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return value

    def peek(self) -> Any:
        """Return the head value without removing it.

        Time: O(1).
        Space: O(1).
        """
        if self._head is None:
            raise IndexError("peek from empty queue")
        return self._head.value

    def is_empty(self) -> bool:
        """Return ``True`` when the queue holds no elements."""
        return self._head is None

    def size(self) -> int:
        """Return the number of elements currently in the queue."""
        return self._size

    def __iter__(self) -> Iterator[Any]:
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size
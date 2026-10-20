"""Singly linked list implementation."""

from __future__ import annotations

from typing import Any, Iterator, cast

from src.dsa.linear.node import Node


class SinglyLinkedList:
    """A singly linked list with head/tail pointers.

    Head insertion and tail append are both O(1) because the tail pointer is
    maintained; indexed access is O(n) because the list must be walked.
    """

    def __init__(self) -> None:
        self._head: Node | None = None
        self._tail: Node | None = None
        self._size: int = 0

    def insert_head(self, value: Any) -> None:
        """Insert ``value`` at the front of the list.

        Time: O(1).
        Space: O(1).
        """
        node = Node(value)
        node.next = self._head
        self._head = node
        if self._tail is None:
            self._tail = node
        self._size += 1

    def append(self, value: Any) -> None:
        """Append ``value`` to the tail of the list.

        Time: O(1) thanks to the maintained tail pointer.
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

    def insert_at(self, index: int, value: Any) -> None:
        """Insert ``value`` at ``index`` (0 = head).

        Time: O(n) because the node before ``index`` must be walked to.
        Space: O(1).
        """
        if not 0 <= index <= self._size:
            raise IndexError("index out of range")
        if index == 0:
            self.insert_head(value)
            return
        if index == self._size:
            self.append(value)
            return
        prev = self._head
        for _ in range(index - 1):
            prev = prev.next  # type: ignore[union-attr]
        prev = cast(Node, prev)  # type: ignore
        node = Node(value)
        node.next = prev.next
        prev.next = node
        self._size += 1

    def delete(self, value: Any) -> bool:
        """Delete the first node whose value equals ``value``.

        Time: O(n) single traversal to find the predecessor.
        Space: O(1).
        Returns ``True`` if a node was removed, ``False`` otherwise.
        """
        prev: Node | None = None
        current = self._head
        while current is not None:
            if current.value == value:
                if prev is None:
                    self._head = current.next
                    if self._head is None:
                        self._tail = None
                else:
                    prev.next = current.next
                    if current is self._tail:
                        self._tail = prev
                self._size -= 1
                return True
            prev = current
            current = current.next
        return False

    def search(self, value: Any) -> bool:
        """Return ``True`` if ``value`` is present in the list.

        Time: O(n) worst case.
        Space: O(1).
        """
        current = self._head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def reverse(self) -> None:
        """Reverse the list in place by rewiring ``next`` pointers.

        Time: O(n) single traversal.
        Space: O(1) extra.
        """
        prev: Node | None = None
        current = self._head
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        # Head and tail swap roles.
        self._tail = self._head
        self._head = prev

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        return f"SinglyLinkedList([{', '.join(repr(v) for v in self)}])"
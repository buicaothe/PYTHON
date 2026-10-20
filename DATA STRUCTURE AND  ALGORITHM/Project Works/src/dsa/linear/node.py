"""Singly linked list node."""

from __future__ import annotations

from typing import Any


class Node:
    """A single linked-list node holding one value and a next pointer."""

    __slots__ = ("value", "next")

    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Node | None = None


# Keep backward compatible name
_Node = Node

"""Shared tree node used by every tree type in this project.

The node deliberately carries no parent pointer: every tree operation in this
project is implemented recursively and returns the new subtree root, which
keeps the code simple and readable at the student level.
"""

from __future__ import annotations

from typing import Any


class TreeNode:
    """A binary-tree node holding one value plus left/right child pointers."""

    __slots__ = ("value", "left", "right")

    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.left: "TreeNode | None" = None
        self.right: "TreeNode | None" = None

    def __repr__(self) -> str:
        return f"TreeNode({self.value!r})"
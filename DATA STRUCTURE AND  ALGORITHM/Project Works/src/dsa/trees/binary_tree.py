"""A generic binary tree with level-order (breadth-first) insertion."""

from __future__ import annotations

from typing import Any

from src.dsa.linear.queue import QueueLinked
from src.dsa.trees.node import TreeNode


class BinaryTree:
    """A binary tree whose root is set on construction.

    New values are inserted in level order: the tree is walked breadth-first
    and the first node missing a child gets the new value on its free side
    (left first, then right).  This keeps the tree compact and is the natural
    way to build a complete binary tree from a stream of values.
    """

    def __init__(self, value: Any) -> None:
        self._root: TreeNode | None = TreeNode(value)

    @property
    def root(self) -> "TreeNode | None":
        """Return the root node (used by the traversal helpers)."""
        return self._root

    def insert(self, value: Any) -> None:
        """Insert ``value`` at the first free slot in level order.

        Time: O(n) because the whole tree may be walked to find the slot.
        Space: O(w) for the BFS queue, where w is the max level width.
        """
        if self._root is None:
            self._root = TreeNode(value)
            return
        queue: QueueLinked = QueueLinked()
        queue.enqueue(self._root)
        while not queue.is_empty():
            node = queue.dequeue()
            if node.left is None:
                node.left = TreeNode(value)
                return
            queue.enqueue(node.left)
            if node.right is None:
                node.right = TreeNode(value)
                return
            queue.enqueue(node.right)

    def height(self) -> int:
        """Return the height of the tree (edges from root to deepest leaf).

        Time: O(n).
        Space: O(h) on the call stack.
        """
        return self._height(self._root)

    def _height(self, node: "TreeNode | None") -> int:
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def size(self) -> int:
        """Return the total number of nodes in the tree.

        Time: O(n).
        Space: O(h) on the call stack.
        """
        return self._size(self._root)

    def _size(self, node: "TreeNode | None") -> int:
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def __len__(self) -> int:
        return self.size()
"""Binary Search Tree: insert, search, delete, and ordered iteration."""

from __future__ import annotations

from typing import Any, Iterator

from src.dsa.trees.node import TreeNode


class BinarySearchTree:
    """A BST ordered by the natural comparison of node values.

    Duplicates are intentionally ignored: ``insert`` returns ``False`` when
    the value is already present and ``True`` when a new node is added.  This
    keeps the tree a set-like structure and avoids the ambiguity of where a
    duplicate would sit.
    """

    def __init__(self) -> None:
        self._root: "TreeNode | None" = None
        self._size: int = 0

    @property
    def root(self) -> "TreeNode | None":
        return self._root

    def insert(self, value: Any) -> bool:
        """Insert ``value``; return ``True`` if added, ``False`` if duplicate.

        Time: O(h) where h is the tree height (O(log n) balanced, O(n) skewed).
        Space: O(1).
        """
        if self._root is None:
            self._root = TreeNode(value)
            self._size += 1
            return True
        current = self._root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    self._size += 1
                    return True
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = TreeNode(value)
                    self._size += 1
                    return True
                current = current.right
            else:
                # Duplicate: do not insert.
                return False

    def search(self, value: Any) -> bool:
        """Return ``True`` if ``value`` is present in the tree.

        Time: O(h).
        Space: O(1).
        """
        current = self._root
        while current is not None:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def delete(self, value: Any) -> bool:
        """Remove ``value`` from the tree; return ``True`` if removed.

        Handles three cases: no children (leaf removal), one child (splice
        the child up), and two children (swap with the in-order successor,
        then delete the successor).  Returns ``False`` if the value was not
        found.

        Time: O(h).
        Space: O(1).
        """
        self._root, removed = self._delete(self._root, value)
        if removed:
            self._size -= 1
        return removed

    def _delete(self, node: "TreeNode | None", value: Any) -> "tuple[TreeNode | None, bool]":
        if node is None:
            return None, False
        if value < node.value:
            node.left, removed = self._delete(node.left, value)
            return node, removed
        if value > node.value:
            node.right, removed = self._delete(node.right, value)
            return node, removed
        # Found the node to delete.
        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True
        # Two children: replace value with in-order successor's value.
        successor = self._min_node(node.right)
        node.value = successor.value
        node.right, _ = self._delete(node.right, successor.value)
        return node, True

    def _min_node(self, node: TreeNode) -> TreeNode:
        """Return the leftmost node in the subtree rooted at ``node``."""
        while node.left is not None:
            node = node.left
        return node

    def min(self) -> Any:
        """Return the smallest value in the tree; raise if empty."""
        if self._root is None:
            raise IndexError("min from empty tree")
        return self._min_node(self._root).value

    def max(self) -> Any:
        """Return the largest value in the tree; raise if empty."""
        node = self._root
        if node is None:
            raise IndexError("max from empty tree")
        while node.right is not None:
            node = node.right
        return node.value

    def height(self) -> int:
        """Return the tree height (edges from root to deepest leaf).

        Time: O(n).
        Space: O(h) on the call stack.
        """
        return self._height(self._root)

    def _height(self, node: "TreeNode | None") -> int:
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def size(self) -> int:
        """Return the number of nodes in the tree (tracked incrementally)."""
        return self._size

    def __contains__(self, value: Any) -> bool:
        return self.search(value)

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        """Yield values in ascending (in-order) order."""
        yield from self._in_order(self._root)

    def _in_order(self, node: "TreeNode | None") -> Iterator[Any]:
        if node is None:
            return
        yield from self._in_order(node.left)
        yield node.value
        yield from self._in_order(node.right)

    def __repr__(self) -> str:
        return f"BinarySearchTree([{', '.join(repr(v) for v in self)}])"
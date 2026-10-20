"""Self-balancing AVL tree.

Insert and delete both rebalance the tree on the way back up the recursion:
each call returns the new subtree root after applying the rotation(s) needed
to restore the AVL property (balance factors in {-1, 0, +1}).  No parent
pointer is used; the recursive return value is the only mechanism.
"""

from __future__ import annotations

from typing import Any

from src.dsa.trees.node import TreeNode


class AVLTree:
    """An AVL tree keeping balance factors in {-1, 0, +1} at every node.

    Concrete implementation of a **Balanced Binary Search Tree** (a.k.a.
    self-balancing BST).  After every insert and delete the tree is rebalanced
    via single/double rotations so the height stays O(log n) even on sorted
    or adversarial input, unlike a plain :class:`BinarySearchTree` which can
    degenerate into a linked list (O(n)).
    """

    def __init__(self) -> None:
        self._root: "TreeNode | None" = None
        self._rotations: int = 0
        self._size: int = 0

    @property
    def root(self) -> "TreeNode | None":
        return self._root

    @property
    def rotations(self) -> int:
        """Return the number of rotations performed so far."""
        return self._rotations

    def _height(self, node: "TreeNode | None") -> int:
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node: "TreeNode | None") -> int:
        """Return height(left) - height(right) for ``node``."""
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def is_balanced(self) -> bool:
        """Return ``True`` when every node's balance factor is in {-1, 0, 1}.

        Time: O(n).
        Space: O(h) on the call stack.
        """
        return self._is_balanced(self._root)

    def _is_balanced(self, node: "TreeNode | None") -> bool:
        if node is None:
            return True
        if abs(self._balance_factor(node)) > 1:
            return False
        return self._is_balanced(node.left) and self._is_balanced(node.right)

    # -- Rotations ---------------------------------------------------------

    def _rotate_right(self, pivot: TreeNode) -> TreeNode:
        """Single right rotation around ``pivot`` (left-left case)."""
        new_root = pivot.left  # type: ignore[union-attr]
        pivot.left = new_root.right
        new_root.right = pivot
        self._rotations += 1
        return new_root

    def _rotate_left(self, pivot: TreeNode) -> TreeNode:
        """Single left rotation around ``pivot`` (right-right case)."""
        new_root = pivot.right  # type: ignore[union-attr]
        pivot.right = new_root.left
        new_root.left = pivot
        self._rotations += 1
        return new_root

    def _balance(self, node: TreeNode) -> TreeNode:
        """Apply the rotation(s) needed to restore balance at ``node``."""
        bf = self._balance_factor(node)
        # Left-heavy.
        if bf > 1:
            if self._balance_factor(node.left) < 0:
                # Left-right case: left rotate the left child first.
                node.left = self._rotate_left(node.left)  # type: ignore[union-attr]
            return self._rotate_right(node)
        # Right-heavy.
        if bf < -1:
            if self._balance_factor(node.right) > 0:
                # Right-left case: right rotate the right child first.
                node.right = self._rotate_right(node.right)  # type: ignore[union-attr]
            return self._rotate_left(node)
        return node

    # -- Public API --------------------------------------------------------

    def insert(self, value: Any) -> bool:
        """Insert ``value`` and rebalance; return ``True`` if added.

        Returns ``False`` when ``value`` is already present (duplicates are
        ignored, keeping the tree set-like).

        Time: O(log n) amortized thanks to rebalancing.
        Space: O(log n) on the call stack.
        """
        before = self._size
        self._root = self._insert(self._root, value)
        return self._size > before

    def _insert(self, node: "TreeNode | None", value: Any) -> TreeNode:
        if node is None:
            self._size += 1
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            # Duplicate: AVL trees here are set-like, so ignore.
            return node
        return self._balance(node)

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
        """Remove ``value`` and rebalance; return ``True`` if removed.

        Time: O(log n) amortized thanks to rebalancing.
        Space: O(log n) on the call stack.
        """
        before = self._size
        self._root = self._delete(self._root, value)
        return self._size < before

    def _delete(self, node: "TreeNode | None", value: Any) -> "TreeNode | None":
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Found the target node.
            if node.left is None:
                self._size -= 1
                return node.right
            if node.right is None:
                self._size -= 1
                return node.left
            # Two children: replace with in-order successor's value.
            successor = self._min_node(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
        return self._balance(node)

    def _min_node(self, node: TreeNode) -> TreeNode:
        while node.left is not None:
            node = node.left
        return node

    def height(self) -> int:
        """Return the tree height (edges from root to deepest leaf)."""
        return self._height(self._root)

    def size(self) -> int:
        """Return the number of nodes in the tree."""
        return self._size

    def __contains__(self, value: Any) -> bool:
        return self.search(value)

    def __iter__(self) -> Any:
        """Yield values in ascending (in-order) order."""
        yield from self._in_order(self._root)

    def _in_order(self, node: "TreeNode | None") -> Any:
        if node is None:
            return
        yield from self._in_order(node.left)
        yield node.value
        yield from self._in_order(node.right)
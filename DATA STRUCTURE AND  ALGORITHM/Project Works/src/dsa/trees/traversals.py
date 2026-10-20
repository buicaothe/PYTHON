"""Tree traversals as generator functions.

Both recursive and explicit-stack iterative variants are provided so the
student can see the same traversal expressed two ways.  Every function
accepts a bare :class:`~src.dsa.trees.node.TreeNode` root, so they work on
``BinaryTree``, ``BinarySearchTree`` and ``AVLTree`` alike.

The explicit-stack variants use :class:`~src.dsa.linear.stack.StackLinked` for
their working stack rather than a plain list, keeping plain lists restricted
to the DynamicArray, the circular queue, the hash buckets, and the inherent
return-value working space of ``merge_sort``.
"""

from __future__ import annotations

from typing import Any, Iterator

from src.dsa.trees.node import TreeNode
from src.dsa.linear.queue import QueueLinked
from src.dsa.linear.stack import StackLinked


def in_order(root: "TreeNode | None") -> Iterator[Any]:
    """Yield values left-root-right (recursive).

    Time: O(n) visits every node once.
    Space: O(h) on the call stack, where h is the tree height.
    """
    if root is None:
        return
    yield from in_order(root.left)
    yield root.value
    yield from in_order(root.right)


def pre_order(root: "TreeNode | None") -> Iterator[Any]:
    """Yield values root-left-right (recursive).

    Time: O(n).
    Space: O(h) on the call stack.
    """
    if root is None:
        return
    yield root.value
    yield from pre_order(root.left)
    yield from pre_order(root.right)


def post_order(root: "TreeNode | None") -> Iterator[Any]:
    """Yield values left-right-root (recursive).

    Time: O(n).
    Space: O(h) on the call stack.
    """
    if root is None:
        return
    yield from post_order(root.left)
    yield from post_order(root.right)
    yield root.value


def level_order(root: "TreeNode | None") -> Iterator[Any]:
    """Yield values breadth-first, level by level.

    Uses :class:`QueueLinked` so no ``collections.deque`` is needed.

    Time: O(n).
    Space: O(w) where w is the maximum width of a level.
    """
    if root is None:
        return
    queue: QueueLinked = QueueLinked()
    queue.enqueue(root)
    while not queue.is_empty():
        node = queue.dequeue()
        yield node.value
        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)


def in_order_iterative(root: "TreeNode | None") -> Iterator[Any]:
    """Yield values left-root-right using an explicit stack.

    Time: O(n).
    Space: O(h) on the explicit stack.
    """
    stack: StackLinked = StackLinked()
    current = root
    while stack.size() > 0 or current is not None:
        # Walk down the left spine, pushing nodes to visit later.
        while current is not None:
            stack.push(current)
            current = current.left
        current = stack.pop()
        yield current.value
        current = current.right


def pre_order_iterative(root: "TreeNode | None") -> Iterator[Any]:
    """Yield values root-left-right using an explicit stack.

    Time: O(n).
    Space: O(h) on the explicit stack.
    """
    if root is None:
        return
    stack: StackLinked = StackLinked()
    stack.push(root)
    while stack.size() > 0:
        current = stack.pop()
        yield current.value
        # Push right first so left is processed next (LIFO).
        if current.right is not None:
            stack.push(current.right)
        if current.left is not None:
            stack.push(current.left)


def post_order_iterative(root: "TreeNode | None") -> Iterator[Any]:
    """Yield values left-right-root using two explicit stacks.

    The classic two-stack approach: a processing stack drives the order and
    an output stack collects values, which are then yielded in reverse.

    Time: O(n).
    Space: O(n) worst case (the output stack may hold every node).
    """
    if root is None:
        return
    process: StackLinked = StackLinked()
    output: StackLinked = StackLinked()
    process.push(root)
    while process.size() > 0:
        current = process.pop()
        output.push(current.value)
        if current.left is not None:
            process.push(current.left)
        if current.right is not None:
            process.push(current.right)
    while output.size() > 0:
        yield output.pop()
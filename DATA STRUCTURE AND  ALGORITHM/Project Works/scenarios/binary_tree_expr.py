"""Scenario: arithmetic expression tree evaluation with :class:`BinaryTree`.

The tree is built by inserting the expression tokens in level order, then
evaluated by walking the tree recursively: leaves are numbers, internal nodes
are operators applied to their two subtrees.

Run directly: ``python scenarios/binary_tree_expr.py``
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dsa.trees import BinaryTree, traversals as T
from src.dsa.trees.node import TreeNode


def evaluate(node: "TreeNode | None") -> float:
    """Recursively evaluate an expression tree rooted at ``node``.

    Leaves are numeric literals; internal nodes are one of ``+ - * /``.

    Time: O(n) -- every node is visited once.
    Space: O(h) on the call stack, where h is the tree height.
    """
    if node is None:
        return 0.0
    if node.left is None and node.right is None:
        return float(node.value)
    left = evaluate(node.left)
    right = evaluate(node.right)
    op = node.value
    if op == "+":
        return left + right
    if op == "-":
        return left - right
    if op == "*":
        return left * right
    if op == "/":
        return left / right
    raise ValueError(f"unknown operator: {op!r}")


def main() -> None:
    # Expression: (3 + 4) * (5 - 2)  ==  21
    tokens = ["*", "+", "-", 3, 4, 5, 2]
    tree = BinaryTree(tokens[0])
    for token in tokens[1:]:
        tree.insert(token)

    print("Level-order tokens:", list(T.level_order(tree.root)))
    print("In-order tokens:   ", list(T.in_order(tree.root)))
    print("Evaluated result:  ", evaluate(tree.root))
    print("Tree height:       ", tree.height())
    print("Tree size:         ", tree.size())


if __name__ == "__main__":
    main()
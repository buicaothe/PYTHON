"""Scenario: compare BST vs AVL heights when inserting sorted IDs.

Run directly: ``python scenarios/avl_sorted_ids.py``
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dsa.trees import BinarySearchTree, AVLTree


def main() -> None:
    sorted_ids = list(range(1, 21))

    bst = BinarySearchTree()
    for sid in sorted_ids:
        bst.insert(sid)

    avl = AVLTree()
    for sid in sorted_ids:
        avl.insert(sid)

    print(f"Inserted {len(sorted_ids)} ids in sorted order.")
    print(f"BST height: {bst.height()}  (degenerates into a linked list)")
    print(f"AVL height: {avl.height()}  (self-balancing)")
    print(f"BST contains 15: {15 in bst}, AVL contains 15: {15 in avl}")
    print(f"BST size: {bst.size()}, AVL size: {avl.size()}")


if __name__ == "__main__":
    main()
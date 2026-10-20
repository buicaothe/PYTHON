"""Unit tests for trees: BinaryTree, BinarySearchTree, AVLTree, and traversals."""

from __future__ import annotations

import os
import sys
import unittest

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from src.dsa.trees import (
    TreeNode,
    BinaryTree,
    BinarySearchTree,
    AVLTree,
    traversals as T,
)


class TestBinaryTree(unittest.TestCase):
    def test_level_order_insertion(self):
        tree = BinaryTree(1)
        for v in [2, 3, 4, 5, 6, 7]:
            tree.insert(v)
        self.assertEqual(tree.size(), 7)
        self.assertEqual(tree.height(), 2)
        # Level-order should be 1,2,3,4,5,6,7
        self.assertEqual(list(T.level_order(tree.root)), [1, 2, 3, 4, 5, 6, 7])

    def test_insert_into_empty_root_none(self):
        # BinaryTree always has a root on construction; size/height reflect that.
        tree = BinaryTree(42)
        self.assertEqual(len(tree), 1)
        self.assertEqual(tree.height(), 0)

    def test_size_and_height(self):
        tree = BinaryTree(1)
        tree.insert(2)
        tree.insert(3)
        self.assertEqual(tree.size(), 3)
        self.assertEqual(tree.height(), 1)


class TestBinarySearchTree(unittest.TestCase):
    def test_insert_and_search(self):
        bst = BinarySearchTree()
        for v in [10, 5, 15, 3, 7, 12, 18]:
            self.assertTrue(bst.insert(v))
        self.assertEqual(bst.size(), 7)
        self.assertTrue(7 in bst)
        self.assertTrue(10 in bst)
        self.assertFalse(99 in bst)

    def test_duplicate_insert_ignored(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.insert(5))
        self.assertFalse(bst.insert(5))
        self.assertEqual(bst.size(), 1)

    def test_in_order_sorted(self):
        bst = BinarySearchTree()
        for v in [10, 5, 15, 3, 7]:
            bst.insert(v)
        self.assertEqual(list(bst), [3, 5, 7, 10, 15])

    def test_delete_leaf(self):
        bst = BinarySearchTree()
        for v in [10, 5, 15]:
            bst.insert(v)
        self.assertTrue(bst.delete(5))
        self.assertFalse(5 in bst)
        self.assertEqual(bst.size(), 2)

    def test_delete_node_with_one_child(self):
        bst = BinarySearchTree()
        for v in [10, 5, 7]:
            bst.insert(v)
        self.assertTrue(bst.delete(5))
        self.assertEqual(list(bst), [7, 10])

    def test_delete_node_with_two_children(self):
        bst = BinarySearchTree()
        for v in [10, 5, 15, 12, 20]:
            bst.insert(v)
        self.assertTrue(bst.delete(15))
        self.assertFalse(15 in bst)
        self.assertEqual(list(bst), [5, 10, 12, 20])

    def test_delete_root(self):
        bst = BinarySearchTree()
        for v in [10, 5, 15]:
            bst.insert(v)
        self.assertTrue(bst.delete(10))
        self.assertFalse(10 in bst)
        self.assertEqual(list(bst), [5, 15])

    def test_delete_nonexistent(self):
        bst = BinarySearchTree()
        bst.insert(1)
        self.assertFalse(bst.delete(99))

    def test_min_max(self):
        bst = BinarySearchTree()
        for v in [10, 5, 15, 3, 7]:
            bst.insert(v)
        self.assertEqual(bst.min(), 3)
        self.assertEqual(bst.max(), 15)

    def test_empty_min_max_raises(self):
        bst = BinarySearchTree()
        with self.assertRaises(IndexError):
            bst.min()
        with self.assertRaises(IndexError):
            bst.max()

    def test_skewed_insertion_height(self):
        bst = BinarySearchTree()
        for v in range(1, 21):
            bst.insert(v)
        self.assertEqual(bst.height(), 19)  # degenerate linked list


class TestAVLTree(unittest.TestCase):
    def test_insert_and_search(self):
        avl = AVLTree()
        for v in [10, 5, 15, 3, 7, 12, 18]:
            self.assertTrue(avl.insert(v))
        self.assertEqual(avl.size(), 7)
        self.assertTrue(7 in avl)
        self.assertFalse(99 in avl)

    def test_duplicate_insert_ignored(self):
        avl = AVLTree()
        self.assertTrue(avl.insert(5))
        self.assertFalse(avl.insert(5))
        self.assertEqual(avl.size(), 1)

    def test_sorted_insertion_stays_balanced(self):
        avl = AVLTree()
        for v in range(1, 32):
            avl.insert(v)
        self.assertTrue(avl.is_balanced())
        # Height should be logarithmic, not 31
        self.assertLess(avl.height(), 10)

    def test_delete_rebalances(self):
        avl = AVLTree()
        for v in range(1, 16):
            avl.insert(v)
        self.assertTrue(avl.is_balanced())
        self.assertTrue(avl.delete(8))
        self.assertTrue(avl.is_balanced())
        self.assertFalse(8 in avl)

    def test_delete_nonexistent(self):
        avl = AVLTree()
        avl.insert(1)
        self.assertFalse(avl.delete(99))

    def test_in_order_sorted(self):
        avl = AVLTree()
        for v in [10, 5, 15, 3, 7]:
            avl.insert(v)
        self.assertEqual(list(avl), [3, 5, 7, 10, 15])

    def test_rotations_counted(self):
        avl = AVLTree()
        avl.insert(1)
        avl.insert(2)
        avl.insert(3)  # triggers a rotation
        self.assertGreaterEqual(avl.rotations, 1)


class TestTraversals(unittest.TestCase):
    def _build_sample(self):
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        return root

    def test_in_order(self):
        root = self._build_sample()
        self.assertEqual(list(T.in_order(root)), [4, 2, 5, 1, 3])

    def test_pre_order(self):
        root = self._build_sample()
        self.assertEqual(list(T.pre_order(root)), [1, 2, 4, 5, 3])

    def test_post_order(self):
        root = self._build_sample()
        self.assertEqual(list(T.post_order(root)), [4, 5, 2, 3, 1])

    def test_level_order(self):
        root = self._build_sample()
        self.assertEqual(list(T.level_order(root)), [1, 2, 3, 4, 5])

    def test_iterative_matches_recursive(self):
        root = self._build_sample()
        self.assertEqual(list(T.in_order(root)), list(T.in_order_iterative(root)))
        self.assertEqual(list(T.pre_order(root)), list(T.pre_order_iterative(root)))
        self.assertEqual(list(T.post_order(root)), list(T.post_order_iterative(root)))

    def test_empty_root(self):
        self.assertEqual(list(T.in_order(None)), [])
        self.assertEqual(list(T.pre_order(None)), [])
        self.assertEqual(list(T.post_order(None)), [])
        self.assertEqual(list(T.level_order(None)), [])
        self.assertEqual(list(T.in_order_iterative(None)), [])
        self.assertEqual(list(T.pre_order_iterative(None)), [])
        self.assertEqual(list(T.post_order_iterative(None)), [])


if __name__ == "__main__":
    unittest.main()

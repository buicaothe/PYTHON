"""Unit tests for linear data structures: DynamicArray, SinglyLinkedList, stacks, queues."""

from __future__ import annotations

import os
import sys
import unittest

# Ensure the project root is on sys.path so `src.dsa` imports resolve when run directly.
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from src.dsa.linear import (
    DynamicArray,
    SinglyLinkedList,
    StackArray,
    StackLinked,
    QueueLinked,
)


class TestDynamicArray(unittest.TestCase):
    def test_append_and_get(self):
        arr = DynamicArray()
        arr.append(10)
        arr.append(20)
        arr.append(30)
        self.assertEqual(len(arr), 3)
        self.assertEqual(arr.get(0), 10)
        self.assertEqual(arr.get(1), 20)
        self.assertEqual(arr.get(2), 30)

    def test_append_resize(self):
        arr = DynamicArray(capacity=2)
        for i in range(100):
            arr.append(i)
        self.assertEqual(len(arr), 100)
        for i in range(100):
            self.assertEqual(arr.get(i), i)

    def test_insert(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(3)
        arr.insert(1, 2)
        self.assertEqual([arr.get(i) for i in range(len(arr))], [1, 2, 3])

    def test_insert_at_end(self):
        arr = DynamicArray()
        arr.append(1)
        arr.insert(1, 2)
        self.assertEqual(arr.get(1), 2)

    def test_delete(self):
        arr = DynamicArray()
        for v in [1, 2, 3, 4]:
            arr.append(v)
        removed = arr.delete(2)
        self.assertEqual(removed, 3)
        self.assertEqual(len(arr), 3)
        self.assertEqual([arr.get(i) for i in range(len(arr))], [1, 2, 4])

    def test_delete_shifts_left(self):
        arr = DynamicArray()
        for v in [10, 20, 30]:
            arr.append(v)
        arr.delete(0)
        self.assertEqual(arr.get(0), 20)
        self.assertEqual(arr.get(1), 30)

    def test_set(self):
        arr = DynamicArray()
        arr.append(5)
        arr.set(0, 99)
        self.assertEqual(arr.get(0), 99)

    def test_index_errors(self):
        arr = DynamicArray()
        with self.assertRaises(IndexError):
            arr.get(0)
        with self.assertRaises(IndexError):
            arr.delete(0)
        with self.assertRaises(IndexError):
            arr.set(0, 1)
        with self.assertRaises(IndexError):
            arr.insert(-1, 1)
        with self.assertRaises(IndexError):
            arr.insert(1, 1)

    def test_iteration(self):
        arr = DynamicArray()
        for v in [4, 5, 6]:
            arr.append(v)
        self.assertEqual(list(arr), [4, 5, 6])

    def test_repr(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        self.assertIn("1", repr(arr))
        self.assertIn("2", repr(arr))


class TestSinglyLinkedList(unittest.TestCase):
    def test_append_and_iter(self):
        lst = SinglyLinkedList()
        lst.append("a")
        lst.append("b")
        lst.append("c")
        self.assertEqual(len(lst), 3)
        self.assertEqual(list(lst), ["a", "b", "c"])

    def test_insert_head(self):
        lst = SinglyLinkedList()
        lst.append("b")
        lst.insert_head("a")
        self.assertEqual(list(lst), ["a", "b"])

    def test_insert_at(self):
        lst = SinglyLinkedList()
        for v in [1, 3]:
            lst.append(v)
        lst.insert_at(1, 2)
        self.assertEqual(list(lst), [1, 2, 3])

    def test_insert_at_head_and_tail(self):
        lst = SinglyLinkedList()
        lst.append(2)
        lst.insert_at(0, 1)  # head
        self.assertEqual(list(lst), [1, 2])
        lst.insert_at(2, 3)  # tail
        self.assertEqual(list(lst), [1, 2, 3])

    def test_delete_existing(self):
        lst = SinglyLinkedList()
        for v in [1, 2, 3]:
            lst.append(v)
        self.assertTrue(lst.delete(2))
        self.assertEqual(list(lst), [1, 3])
        self.assertEqual(len(lst), 2)

    def test_delete_nonexistent(self):
        lst = SinglyLinkedList()
        lst.append(1)
        self.assertFalse(lst.delete(99))

    def test_delete_head_updates_tail(self):
        lst = SinglyLinkedList()
        lst.append(1)
        self.assertTrue(lst.delete(1))
        self.assertTrue(lst.is_empty() if hasattr(lst, "is_empty") else len(lst) == 0)

    def test_search(self):
        lst = SinglyLinkedList()
        for v in [1, 2, 3]:
            lst.append(v)
        self.assertTrue(lst.search(2))
        self.assertFalse(lst.search(99))

    def test_reverse(self):
        lst = SinglyLinkedList()
        for v in [1, 2, 3]:
            lst.append(v)
        lst.reverse()
        self.assertEqual(list(lst), [3, 2, 1])

    def test_index_errors(self):
        lst = SinglyLinkedList()
        with self.assertRaises(IndexError):
            lst.insert_at(-1, 1)
        with self.assertRaises(IndexError):
            lst.insert_at(2, 1)

    def test_repr(self):
        lst = SinglyLinkedList()
        lst.append(1)
        lst.append(2)
        self.assertIn("1", repr(lst))
        self.assertIn("2", repr(lst))


class TestStackArray(unittest.TestCase):
    def test_push_pop_peek(self):
        stack = StackArray()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())

    def test_pop_empty_raises(self):
        stack = StackArray()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek_empty_raises(self):
        stack = StackArray()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_iter_top_to_bottom(self):
        stack = StackArray()
        stack.push("bottom")
        stack.push("top")
        self.assertEqual(list(stack), ["top", "bottom"])


class TestStackLinked(unittest.TestCase):
    def test_push_pop_peek(self):
        stack = StackLinked()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())

    def test_pop_empty_raises(self):
        stack = StackLinked()
        with self.assertRaises(IndexError):
            stack.pop()


class TestQueueLinked(unittest.TestCase):
    def test_enqueue_dequeue_fifo(self):
        queue = QueueLinked()
        queue.enqueue("first")
        queue.enqueue("second")
        queue.enqueue("third")
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.dequeue(), "first")
        self.assertEqual(queue.dequeue(), "second")
        self.assertEqual(queue.dequeue(), "third")
        self.assertTrue(queue.is_empty())

    def test_dequeue_empty_raises(self):
        queue = QueueLinked()
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_peek(self):
        queue = QueueLinked()
        queue.enqueue(42)
        self.assertEqual(queue.peek(), 42)
        self.assertEqual(queue.size(), 1)  # peek does not remove


if __name__ == "__main__":
    unittest.main()

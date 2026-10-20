"""Unit tests for sorting and searching algorithms."""

from __future__ import annotations

import os
import sys
import unittest

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from src.dsa.sorting import bubble_sort, insertion_sort, merge_sort
from src.dsa.searching import (
    linear_search,
    binary_search_iterative,
    binary_search_recursive,
)
from src.dsa.stats import OpStats


class TestSorting(unittest.TestCase):
    def _assert_sorted(self, result, original):
        self.assertEqual(len(result), len(original))
        self.assertEqual(sorted(original), result)

    def test_bubble_sort_random(self):
        self._assert_sorted(bubble_sort([3, 1, 4, 1, 5, 9, 2, 6]), [3, 1, 4, 1, 5, 9, 2, 6])

    def test_insertion_sort_random(self):
        self._assert_sorted(insertion_sort([3, 1, 4, 1, 5, 9, 2, 6]), [3, 1, 4, 1, 5, 9, 2, 6])

    def test_merge_sort_random(self):
        self._assert_sorted(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]), [3, 1, 4, 1, 5, 9, 2, 6])

    def test_empty(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(bubble_sort([42]), [42])
        self.assertEqual(insertion_sort([42]), [42])
        self.assertEqual(merge_sort([42]), [42])

    def test_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(data), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort(data), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort(data), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        data = [5, 4, 3, 2, 1]
        self.assertEqual(bubble_sort(data), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort(data), [1, 2, 3, 4, 5])
        self.assertEqual(merge_sort(data), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        data = [3, 1, 3, 1, 2]
        self.assertEqual(bubble_sort(data), [1, 1, 2, 3, 3])
        self.assertEqual(insertion_sort(data), [1, 1, 2, 3, 3])
        self.assertEqual(merge_sort(data), [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        data = [-3, 1, -1, 4, 0]
        self.assertEqual(bubble_sort(data), [-3, -1, 0, 1, 4])
        self.assertEqual(insertion_sort(data), [-3, -1, 0, 1, 4])
        self.assertEqual(merge_sort(data), [-3, -1, 0, 1, 4])

    def test_key_function(self):
        students = [("Ada", 92), ("Linus", 88), ("Grace", 95)]
        result = bubble_sort(students, key=lambda s: s[1])
        self.assertEqual(result, [("Linus", 88), ("Ada", 92), ("Grace", 95)])

    def test_stability(self):
        # bubble_sort and insertion_sort and merge_sort are stable.
        data = [(3, "a"), (1, "b"), (3, "c"), (2, "d"), (1, "e")]
        for fn in (bubble_sort, insertion_sort, merge_sort):
            result = fn(data, key=lambda x: x[0])
            # Elements with key 1 should keep "b" before "e"; key 3 should keep "a" before "c".
            ones = [item for item in result if item[0] == 1]
            threes = [item for item in result if item[0] == 3]
            self.assertEqual(ones, [(1, "b"), (1, "e")])
            self.assertEqual(threes, [(3, "a"), (3, "c")])

    def test_input_not_mutated(self):
        original = [3, 1, 2]
        data = list(original)
        bubble_sort(data)
        insertion_sort(data)
        merge_sort(data)
        self.assertEqual(data, original)  # sorting returns a copy, input unchanged

    def test_stats_recorded(self):
        stats = OpStats()
        bubble_sort([3, 1, 2], stats=stats)
        self.assertGreater(stats.comparisons, 0)

    def test_merge_sort_large(self):
        data = list(range(1000, 0, -1))
        self.assertEqual(merge_sort(data), list(range(1, 1001)))


class TestSearching(unittest.TestCase):
    def test_linear_search_found(self):
        self.assertEqual(linear_search([10, 20, 30, 40], 30), 2)

    def test_linear_search_first_last(self):
        self.assertEqual(linear_search([10, 20, 30], 10), 0)
        self.assertEqual(linear_search([10, 20, 30], 30), 2)

    def test_linear_search_not_found(self):
        self.assertEqual(linear_search([10, 20, 30], 99), -1)

    def test_linear_search_empty(self):
        self.assertEqual(linear_search([], 1), -1)

    def test_linear_search_duplicates_returns_first(self):
        self.assertEqual(linear_search([1, 2, 2, 3], 2), 1)

    def test_binary_search_iterative_found(self):
        data = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binary_search_iterative(data, 7), 3)
        self.assertEqual(binary_search_iterative(data, 1), 0)
        self.assertEqual(binary_search_iterative(data, 11), 5)

    def test_binary_search_iterative_not_found(self):
        self.assertEqual(binary_search_iterative([1, 3, 5], 4), -1)
        self.assertEqual(binary_search_iterative([], 1), -1)

    def test_binary_search_recursive_matches_iterative(self):
        data = [1, 3, 5, 7, 9, 11]
        for target in data:
            self.assertEqual(
                binary_search_recursive(data, target),
                binary_search_iterative(data, target),
            )
        self.assertEqual(binary_search_recursive(data, 4), -1)

    def test_binary_search_stats(self):
        stats = OpStats()
        binary_search_iterative(list(range(1, 1001)), 999, stats=stats)
        self.assertGreater(stats.comparisons, 0)

    def test_binary_search_requires_sorted(self):
        # Unsorted input: result is undefined but should not crash.
        result = binary_search_iterative([3, 1, 2], 2)
        self.assertIsInstance(result, int)


if __name__ == "__main__":
    unittest.main()

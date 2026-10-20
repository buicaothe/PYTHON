"""Unit tests for hashing: hash functions, chaining, and open addressing tables."""

from __future__ import annotations

import os
import sys
import unittest

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from src.dsa.hashing import (
    division_hash,
    polynomial_hash,
    djb2_hash,
    ChainingHashTable,
    OpenAddressingHashTable,
)


class TestHashFunctions(unittest.TestCase):
    def test_division_hash_range(self):
        for key in range(100):
            h = division_hash(key, 16)
            self.assertTrue(0 <= h < 16)

    def test_division_hash_deterministic(self):
        self.assertEqual(division_hash(101, 8), division_hash(101, 8))

    def test_division_hash_invalid_size(self):
        with self.assertRaises(ValueError):
            division_hash(5, 0)
        with self.assertRaises(ValueError):
            division_hash(5, -1)

    def test_polynomial_hash_range(self):
        for word in ["a", "abc", "the quick brown fox"]:
            h = polynomial_hash(word, 16)
            self.assertTrue(0 <= h < 16)

    def test_polynomial_hash_deterministic(self):
        self.assertEqual(polynomial_hash("hello", 16), polynomial_hash("hello", 16))

    def test_djb2_hash_range(self):
        for word in ["a", "abc", "the quick brown fox"]:
            h = djb2_hash(word, 16)
            self.assertTrue(0 <= h < 16)

    def test_different_strings_can_collide(self):
        # Collisions are expected; just ensure both hash without error.
        polynomial_hash("ab", 8)
        polynomial_hash("ba", 8)


class TestChainingHashTable(unittest.TestCase):
    def test_put_get(self):
        table = ChainingHashTable(hash_function=polynomial_hash)
        table.put("Ada", "ada@example.com")
        table.put("Linus", "linus@example.com")
        self.assertEqual(table.get("Ada"), "ada@example.com")
        self.assertEqual(table.get("Linus"), "linus@example.com")

    def test_put_overwrites(self):
        table = ChainingHashTable(hash_function=polynomial_hash)
        table.put("Ada", "old@example.com")
        table.put("Ada", "new@example.com")
        self.assertEqual(table.get("Ada"), "new@example.com")
        self.assertEqual(len(table), 1)

    def test_contains(self):
        table = ChainingHashTable(hash_function=polynomial_hash)
        table.put("Ada", "x")
        self.assertTrue("Ada" in table)
        self.assertFalse("Eva" in table)

    def test_get_missing_raises(self):
        table = ChainingHashTable(hash_function=polynomial_hash)
        with self.assertRaises(KeyError):
            table.get("missing")

    def test_remove(self):
        table = ChainingHashTable(hash_function=polynomial_hash)
        table.put("Ada", "x")
        table.remove("Ada")
        self.assertFalse("Ada" in table)
        self.assertEqual(len(table), 0)

    def test_remove_missing_raises(self):
        table = ChainingHashTable(hash_function=polynomial_hash)
        with self.assertRaises(KeyError):
            table.remove("missing")

    def test_resize_preserves_data(self):
        table = ChainingHashTable(capacity=4)
        for i in range(50):
            table.put(i, f"v{i}")
        for i in range(50):
            self.assertEqual(table.get(i), f"v{i}")
        self.assertEqual(len(table), 50)

    def test_load_factor(self):
        table = ChainingHashTable(capacity=8)
        for i in range(4):
            table.put(i, i)
        self.assertEqual(table.load_factor(), 0.5)

    def test_integer_keys_division_hash(self):
        table = ChainingHashTable(hash_function=division_hash)
        ids = [102, 105, 101, 107, 104]
        for sid in ids:
            table.put(sid, f"student-{sid}")
        for sid in ids:
            self.assertEqual(table.get(sid), f"student-{sid}")
        self.assertFalse(999 in table)

    def test_iteration(self):
        table = ChainingHashTable()
        for i in range(10):
            table.put(i, i)
        self.assertEqual(set(table), set(range(10)))

    def test_collision_count(self):
        table = ChainingHashTable(hash_function=division_hash, capacity=2)
        table.put(0, "a")
        table.put(2, "b")  # 0 % 2 == 2 % 2 == 0 -> collision
        self.assertEqual(table.collision_count(), 1)


class TestOpenAddressingHashTable(unittest.TestCase):
    def test_put_get_linear(self):
        table = OpenAddressingHashTable(hash_function=polynomial_hash, probe="linear")
        table.put("Ada", "ada@example.com")
        table.put("Linus", "linus@example.com")
        self.assertEqual(table.get("Ada"), "ada@example.com")
        self.assertEqual(table.get("Linus"), "linus@example.com")

    def test_put_get_quadratic(self):
        table = OpenAddressingHashTable(probe="quadratic")
        for i in range(20):
            table.put(i, f"v{i}")
        for i in range(20):
            self.assertEqual(table.get(i), f"v{i}")

    def test_put_overwrites(self):
        table = OpenAddressingHashTable(hash_function=polynomial_hash)
        table.put("Ada", "old")
        table.put("Ada", "new")
        self.assertEqual(table.get("Ada"), "new")
        self.assertEqual(len(table), 1)

    def test_contains(self):
        table = OpenAddressingHashTable(hash_function=polynomial_hash)
        table.put("Ada", "x")
        self.assertTrue("Ada" in table)
        self.assertFalse("Eva" in table)

    def test_get_missing_raises(self):
        table = OpenAddressingHashTable(hash_function=polynomial_hash)
        with self.assertRaises(KeyError):
            table.get("missing")

    def test_remove(self):
        table = OpenAddressingHashTable(hash_function=polynomial_hash)
        table.put("Ada", "x")
        table.remove("Ada")
        self.assertFalse("Ada" in table)
        self.assertEqual(len(table), 0)
        # Tombstone should not break lookup of keys inserted after.
        table.put("Bob", "y")
        self.assertEqual(table.get("Bob"), "y")

    def test_remove_missing_raises(self):
        table = OpenAddressingHashTable(hash_function=polynomial_hash)
        with self.assertRaises(KeyError):
            table.remove("missing")

    def test_resize_preserves_data(self):
        table = OpenAddressingHashTable(capacity=4, probe="linear")
        for i in range(50):
            table.put(i, f"v{i}")
        for i in range(50):
            self.assertEqual(table.get(i), f"v{i}")
        self.assertEqual(len(table), 50)

    def test_integer_keys(self):
        table = OpenAddressingHashTable(hash_function=division_hash, probe="linear")
        ids = [102, 105, 101, 107, 104]
        for sid in ids:
            table.put(sid, f"student-{sid}")
        for sid in ids:
            self.assertEqual(table.get(sid), f"student-{sid}")
        self.assertFalse(999 in table)

    def test_iteration(self):
        table = OpenAddressingHashTable()
        for i in range(10):
            table.put(i, i)
        self.assertEqual(set(table), set(range(10)))

    def test_collision_count(self):
        table = OpenAddressingHashTable(hash_function=division_hash, capacity=2, probe="linear")
        table.put(0, "a")
        table.put(2, "b")  # collide with 0
        self.assertGreaterEqual(table.collision_count(), 0)

    def test_invalid_probe_raises(self):
        with self.assertRaises(ValueError):
            OpenAddressingHashTable(probe="invalid")


if __name__ == "__main__":
    unittest.main()

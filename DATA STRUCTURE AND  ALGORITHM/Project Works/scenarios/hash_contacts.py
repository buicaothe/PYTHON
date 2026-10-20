"""Scenario: contact directory, word-frequency counter, and a collision demo.

Demonstrates two hash functions (``division_hash`` for integer keys,
``polynomial_hash`` and ``djb2_hash`` for string keys) crossed with the two
collision strategies (separate chaining and open addressing).

Run directly: ``python scenarios/hash_contacts.py``
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dsa.hashing import (
    division_hash,
    polynomial_hash,
    djb2_hash,
    ChainingHashTable,
    OpenAddressingHashTable,
)


def build_contacts(hash_function, strategy: str):
    """Build a small contact directory and return the table."""
    table = _new_table(hash_function, strategy)
    directory = [
        ("Ada", "ada@example.com"),
        ("Linus", "linus@example.com"),
        ("Grace", "grace@example.com"),
        ("Margaret", "margaret@example.com"),
        ("Katherine", "katherine@example.com"),
        ("Alan", "alan@example.com"),
        ("Dennis", "dennis@example.com"),
        ("Barbara", "barbara@example.com"),
    ]
    for name, email in directory:
        table.put(name, email)
    return table, directory


def build_word_counter(hash_function, strategy: str, text: str):
    """Count word frequencies in ``text`` using the given table."""
    table = _new_table(hash_function, strategy)
    for word in text.split():
        table.put(word, table.get(word) + 1 if word in table else 1)
    return table


def _new_table(hash_function, strategy: str):
    if strategy == "chaining":
        return ChainingHashTable(hash_function=hash_function)
    return OpenAddressingHashTable(hash_function=hash_function, probe="linear")


def main() -> None:
    print("=== Contact directory (string-keyed polynomial hash) ===")
    table, directory = build_contacts(polynomial_hash, "chaining")
    for name, email in directory:
        print(f"  {name} -> {table.get(name)}")
    print(f"  lookup missing 'Eva': ", end="")
    try:
        table.get("Eva")
    except KeyError:
        print("KeyError (expected)")

    print("\n=== Student-id directory (integer-keyed division hash) ===")
    id_table = ChainingHashTable(hash_function=division_hash)
    ids = [102, 105, 101, 107, 104, 108, 103, 106]
    for sid in ids:
        id_table.put(sid, f"student-{sid}")
    print(f"  size={len(id_table)}, load_factor={id_table.load_factor():.3f}")
    for sid in (101, 104, 107, 999):
        if sid in id_table:
            print(f"  id {sid} -> {id_table.get(sid)}")
        else:
            print(f"  id {sid} not found")

    text = "the quick brown fox jumps over the lazy dog the quick brown fox"
    print("\n=== Word-frequency counter ===")
    for hash_fn, label in ((polynomial_hash, "polynomial"), (djb2_hash, "djb2")):
        for strategy in ("chaining", "open addressing"):
            table = build_word_counter(hash_fn, strategy, text)
            print(
                f"  {label} / {strategy}: "
                f"'the'={table.get('the')}, 'fox'={table.get('fox')}, "
                f"collisions={table.collision_count()}, resizes={table.resize_count()}"
            )

    print("\n=== Collision demo: many integer keys ===")
    # Sequential keys collide heavily with the division hash when the table
    # is small; watch the collision count climb and the table resize.
    for strategy in ("chaining", "open addressing"):
        table = _new_table(division_hash, strategy)
        for i in range(50):
            table.put(i, i)
        print(
            f"  {strategy}: size={len(table)}, capacity={table.capacity}, "
            f"load_factor={table.load_factor():.3f}, "
            f"collisions={table.collision_count()}, resizes={table.resize_count()}"
        )


if __name__ == "__main__":
    main()
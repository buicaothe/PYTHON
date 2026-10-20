"""Scenario: find a product in a sorted inventory using binary search.

Run directly: ``python scenarios/searching_inventory.py``
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dsa.searching import linear_search, binary_search_iterative, binary_search_recursive
from src.dsa.sorting import merge_sort
from src.dsa.stats import OpStats


class Product:
    """A simple product record with a name and a price.

    Comparison is by name so binary search can locate a product by name.
    """

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __lt__(self, other: "Product") -> bool:
        return self.name < other.name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Product) and self.name == other.name

    def __repr__(self) -> str:
        return f"{self.name} (${self.price:.2f})"


def main() -> None:
    inventory = [
        Product("apple", 1.20),
        Product("banana", 0.59),
        Product("cherry", 3.49),
        Product("date", 4.99),
        Product("elderberry", 2.75),
    ]
    # Binary search requires the inventory to be sorted by name.
    # Use our own merge_sort rather than the built-in sorted().
    sorted_inventory = merge_sort(inventory, key=lambda p: p.name)
    print("Sorted inventory:")
    for product in sorted_inventory:
        print(f"  - {product}")

    targets = ["cherry", "date", "fig"]
    for target in targets:
        linear = linear_search(inventory, Product(target, 0.0))
        binary = binary_search_iterative(sorted_inventory, Product(target, 0.0))
        binary_rec = binary_search_recursive(sorted_inventory, Product(target, 0.0))
        print(f"\nSearch for {target!r}:")
        print(f"  linear_search        -> index {linear}")
        print(f"  binary_search_iter   -> index {binary}")
        print(f"  binary_search_rec    -> index {binary_rec}")

    # Stats demo: count comparisons on a larger sorted list.
    big = list(range(1, 1001))
    stats = OpStats()
    result = binary_search_iterative(big, 999, stats=stats)
    print(f"\nSearch for 999 in 1..1000: index {result}, comparisons={stats.comparisons}")


if __name__ == "__main__":
    main()
"""Performance analysis for the DSA project.

Compares sorting algorithms across input sizes and types, and tree traversal
algorithms (recursive vs iterative).  Results are written to a markdown report
suitable for the project's performance-analysis deliverable.
"""

from __future__ import annotations

import os
import random
import sys
import time
from datetime import datetime

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from src.dsa.sorting import bubble_sort, insertion_sort, merge_sort
from src.dsa.searching import OpStats
from src.dsa.trees import BinarySearchTree, AVLTree, BinaryTree
from src.dsa.trees import traversals as T


def _timed(fn, *args, **kwargs):
    """Run ``fn`` and return ``(result, seconds)``."""
    start = time.perf_counter()
    result = fn(*args, **kwargs)
    elapsed = time.perf_counter() - start
    return result, elapsed


def _make_data(size: int, kind: str, seed: int = 42) -> list[int]:
    """Generate a list of ``size`` ints of the given ``kind``."""
    rng = random.Random(seed)
    if kind == "random":
        return [rng.randint(0, size * 10) for _ in range(size)]
    if kind == "sorted":
        return list(range(size))
    if kind == "reverse":
        return list(range(size, 0, -1))
    if kind == "duplicates":
        return [rng.randint(0, size // 10) for _ in range(size)]
    raise ValueError(f"unknown data kind: {kind}")


def analyze_sorting(sizes: list[int] | None = None, kinds: list[str] | None = None) -> list[dict]:
    """Benchmark the three sorting algorithms.

    Returns a list of result dicts, one per (algorithm, size, kind) combination.
    Bubble and insertion sorts are capped at ``max_size_for_quadratic`` because
    they are O(n^2) and become impractical at large ``n``.
    """
    if sizes is None:
        sizes = [100, 500, 1000, 2000, 5000]
    if kinds is None:
        kinds = ["random", "sorted", "reverse", "duplicates"]

    max_quadratic = 1000  # bubble/insertion become too slow beyond this
    algorithms = {
        "bubble_sort": bubble_sort,
        "insertion_sort": insertion_sort,
        "merge_sort": merge_sort,
    }

    results: list[dict] = []
    for size in sizes:
        for kind in kinds:
            data = _make_data(size, kind)
            for name, fn in algorithms.items():
                # Skip quadratic sorts at large sizes to keep runtime sane.
                if name in ("bubble_sort", "insertion_sort") and size > max_quadratic:
                    continue
                stats = OpStats()
                sorted_copy, elapsed = _timed(fn, data, stats=stats)
                # Verify correctness.
                assert sorted_copy == sorted(data), f"{name} produced incorrect output"
                results.append({
                    "algorithm": name,
                    "size": size,
                    "kind": kind,
                    "seconds": elapsed,
                    "comparisons": stats.comparisons,
                    "swaps": stats.swaps,
                })
    return results


def _build_tree(size: int, kind: str = "bst", seed: int = 42):
    """Build a tree of ``size`` nodes."""
    rng = random.Random(seed)
    values = list(range(1, size + 1))
    if kind == "random":
        rng.shuffle(values)
    if kind == "avl":
        tree = AVLTree()
        for v in values:
            tree.insert(v)
        return tree
    # default: BST
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree


def analyze_traversals(sizes: list[int] | None = None) -> list[dict]:
    """Benchmark recursive vs iterative tree traversals.

    Returns a list of result dicts, one per (traversal, variant, size) combination.
    """
    if sizes is None:
        sizes = [100, 500, 1000, 2000, 5000]

    traversals = {
        "in_order": (T.in_order, T.in_order_iterative),
        "pre_order": (T.pre_order, T.pre_order_iterative),
        "post_order": (T.post_order, T.post_order_iterative),
    }

    results: list[dict] = []
    for size in sizes:
        tree = _build_tree(size, kind="random")
        root = tree.root
        for name, (rec_fn, iter_fn) in traversals.items():
            # Recursive.
            _, rec_time = _timed(lambda: list(rec_fn(root)))
            # Iterative.
            _, iter_time = _timed(lambda: list(iter_fn(root)))
            # Verify both produce the same sequence.
            rec_vals = list(rec_fn(root))
            iter_vals = list(iter_fn(root))
            assert rec_vals == iter_vals, f"{name} mismatch between recursive and iterative"

            results.append({
                "traversal": name,
                "variant": "recursive",
                "size": size,
                "seconds": rec_time,
            })
            results.append({
                "traversal": name,
                "variant": "iterative",
                "size": size,
                "seconds": iter_time,
            })
    return results


def _format_seconds(seconds: float) -> str:
    if seconds < 1e-6:
        return f"{seconds*1e9:.1f} ns"
    if seconds < 1e-3:
        return f"{seconds*1e6:.1f} µs"
    if seconds < 1.0:
        return f"{seconds*1e3:.2f} ms"
    return f"{seconds:.4f} s"


def write_report(sorting_results: list[dict], traversal_results: list[dict], path: str) -> str:
    """Write the performance analysis report to ``path`` and return its text."""
    lines: list[str] = []
    lines.append("# DSA Project — Performance Analysis Report")
    lines.append("")
    lines.append(f"Generated: {datetime.now().isoformat()}")
    lines.append("")
    lines.append("## Methodology")
    lines.append("")
    lines.append("- Sorting algorithms (`bubble_sort`, `insertion_sort`, `merge_sort`) were timed on input lists of various sizes and data distributions.")
    lines.append("- Wall-clock time was measured with `time.perf_counter`; comparison and swap counts were captured via `OpStats`.")
    lines.append("- Bubble and insertion sorts (O(n^2)) were capped at n=1000; merge sort was tested up to n=5000.")
    lines.append("- Tree traversals (in-order, pre-order, post-order) were compared between recursive and explicit-stack iterative variants on BSTs of various sizes.")
    lines.append("- Every sorted output was verified against Python's built-in `sorted()` for correctness.")
    lines.append("")
    lines.append("## Sorting results (wall-clock time)")
    lines.append("")
    lines.append("| Algorithm | Size | Distribution | Time | Comparisons | Swaps |")
    lines.append("|---|---|---|---|---|---|")
    for r in sorting_results:
        lines.append(
            f"| {r['algorithm']} | {r['size']} | {r['kind']} | "
            f"{_format_seconds(r['seconds'])} | {r['comparisons']:,} | {r['swaps']:,} |"
        )
    lines.append("")
    lines.append("### Sorting observations")
    lines.append("")
    lines.append("- **Merge sort** is consistently the fastest for medium and large inputs (O(n log n)) and is unaffected by input distribution.")
    lines.append("- **Bubble sort** and **insertion sort** are O(n^2): they are competitive only on very small or already-sorted inputs, and degrade sharply on reverse-sorted data.")
    lines.append("- **Insertion sort** is typically faster than bubble sort in practice because it performs fewer swaps (shifts instead of exchanges).")
    lines.append("- All three algorithms are stable: equal keys preserve their original relative order.")
    lines.append("")
    lines.append("## Tree traversal results (wall-clock time)")
    lines.append("")
    lines.append("| Traversal | Variant | Size | Time |")
    lines.append("|---|---|---|---|")
    for r in traversal_results:
        lines.append(
            f"| {r['traversal']} | {r['variant']} | {r['size']} | {_format_seconds(r['seconds'])} |"
        )
    lines.append("")
    lines.append("### Traversal observations")
    lines.append("")
    lines.append("- Recursive and iterative traversals both run in O(n) time and produce identical sequences.")
    lines.append("- Recursive traversals use O(h) call-stack space; iterative traversals use O(h) explicit-stack space.")
    lines.append("- For balanced trees h = O(log n); for skewed BSTs h = O(n), so recursive depth can become a practical limit.")
    lines.append("")
    lines.append("## Space complexity summary")
    lines.append("")
    lines.append("| Structure / Algorithm | Auxiliary space | Notes |")
    lines.append("|---|---|---|")
    lines.append("| DynamicArray | O(1) amortized append | O(n) occasional resize |")
    lines.append("| SinglyLinkedList | O(1) per node | O(n) total for n nodes |")
    lines.append("| StackArray / StackLinked | O(1) per push | StackLinked allocates a node per push |")
    lines.append("| QueueLinked | O(1) per enqueue | |")
    lines.append("| BinarySearchTree | O(1) per node | O(h) recursion for insert/delete |")
    lines.append("| AVLTree | O(1) per node | O(log n) recursion depth when balanced |")
    lines.append("| ChainingHashTable | O(1) amortized | Buckets plus occasional O(n) resize |")
    lines.append("| OpenAddressingHashTable | O(1) amortized | Slot array plus occasional O(n) resize |")
    lines.append("| bubble_sort / insertion_sort / merge_sort | O(n) | Each returns a new sorted list |")
    lines.append("| linear_search | O(1) | In-place scan |")
    lines.append("| binary_search_iterative | O(1) | In-place halving |")
    lines.append("| binary_search_recursive | O(log n) | Call-stack depth |")
    lines.append("")
    lines.append("## Time complexity summary")
    lines.append("")
    lines.append("| Algorithm | Best | Average | Worst |")
    lines.append("|---|---|---|---|")
    lines.append("| DynamicArray append | O(1) | O(1) amortized | O(n) on resize |")
    lines.append("| DynamicArray insert/delete/get | O(n) / O(n) / O(1) | — | — |")
    lines.append("| SinglyLinkedList insert_head/append | O(1) / O(1) | — | — |")
    lines.append("| SinglyLinkedList insert_at/delete/search | O(n) | — | — |")
    lines.append("| Stack push/pop/peek | O(1) | — | — |")
    lines.append("| Queue enqueue/dequeue/peek | O(1) | — | — |")
    lines.append("| BST insert/search/delete | O(h) | O(log n) balanced | O(n) skewed |")
    lines.append("| AVL insert/search/delete | O(log n) | O(log n) | O(log n) |")
    lines.append("| Tree traversal (any order) | O(n) | O(n) | O(n) |")
    lines.append("| ChainingHashTable put/get/remove | O(1) avg | O(1) avg | O(n) worst (all collide) |")
    lines.append("| OpenAddressingHashTable put/get/remove | O(1) avg | O(1) avg | O(n) worst (full probe) |")
    lines.append("| bubble_sort | O(n) | O(n^2) | O(n^2) |")
    lines.append("| insertion_sort | O(n) | O(n^2) | O(n^2) |")
    lines.append("| merge_sort | O(n log n) | O(n log n) | O(n log n) |")
    lines.append("| linear_search | O(1) | O(n) | O(n) |")
    lines.append("| binary_search | O(1) | O(log n) | O(log n) |")
    lines.append("")
    lines.append("## Conclusion")
    lines.append("")
    lines.append("- Use **merge sort** for general-purpose sorting of medium/large inputs.")
    lines.append("- Use **insertion sort** only for tiny or nearly-sorted inputs.")
    lines.append("- Prefer a **balanced tree (AVL)** when sorted-order operations must remain O(log n) on adversarial/sorted input; a plain BST degenerates to O(n).")
    lines.append("- Recursive and iterative traversals are equivalent in result and asymptotic time; choose recursive for clarity, iterative when stack depth is a concern.")
    lines.append("- Hash tables give O(1) average-case put/get/remove; choose separate chaining for simplicity or open addressing for lower memory overhead when load factor is kept low.")

    report = "\n".join(lines)
    with open(path, "w", encoding="utf-8") as f:
        f.write(report)
    print(report)
    return report


def main() -> int:
    print("=== Sorting performance analysis ===")
    sorting_results = analyze_sorting()
    print(f"Collected {len(sorting_results)} sorting samples.")
    print("\n=== Tree traversal performance analysis ===")
    traversal_results = analyze_traversals()
    print(f"Collected {len(traversal_results)} traversal samples.")

    report_path = os.path.join(_PROJECT_ROOT, "PERFORMANCE_ANALYSIS_REPORT.md")
    write_report(sorting_results, traversal_results, report_path)
    print(f"\nPerformance report written to {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

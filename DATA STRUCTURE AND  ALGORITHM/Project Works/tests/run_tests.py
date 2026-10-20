"""Test runner that executes all DSA project tests and writes a validation report."""

from __future__ import annotations

import importlib
import os
import sys
import unittest
from datetime import datetime

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)


_TEST_MODULES = [
    "tests.test_linear",
    "tests.test_trees",
    "tests.test_hashing",
    "tests.test_sorting_searching",
]


def discover_and_run() -> unittest.TestResult:
    """Load all test modules and run them."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for mod_name in _TEST_MODULES:
        module = importlib.import_module(mod_name)
        suite.addTests(loader.loadTestsFromModule(module))
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


def write_report(result: unittest.TestResult, path: str) -> None:
    """Write a human-readable validation report to ``path``."""
    total = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    passed = total - failures - errors
    success_rate = (passed / total * 100) if total else 0.0

    lines: list[str] = []
    lines.append("# DSA Project — Test Validation Report")
    lines.append("")
    lines.append(f"Generated: {datetime.now().isoformat()}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total test cases run: {total}")
    lines.append(f"- Passed: {passed}")
    lines.append(f"- Failed: {failures}")
    lines.append(f"- Errors: {errors}")
    lines.append(f"- Success rate: {success_rate:.1f}%")
    lines.append("")
    lines.append("## Modules covered")
    lines.append("")
    lines.append("- `tests/test_linear.py` — DynamicArray, SinglyLinkedList, StackArray, StackLinked, QueueLinked")
    lines.append("- `tests/test_trees.py` — BinaryTree, BinarySearchTree, AVLTree, traversals (in-order, pre-order, post-order, level-order)")
    lines.append("- `tests/test_hashing.py` — division_hash, polynomial_hash, djb2_hash, ChainingHashTable, OpenAddressingHashTable")
    lines.append("- `tests/test_sorting_searching.py` — bubble_sort, insertion_sort, merge_sort, linear_search, binary_search (iterative & recursive)")
    lines.append("")
    lines.append("## Edge cases covered")
    lines.append("")
    lines.append("- Empty containers (empty list, empty tree, empty hash table)")
    lines.append("- Single-element containers")
    lines.append("- Duplicate values / keys")
    lines.append("- Insert at head, middle, and tail")
    lines.append("- Delete leaf, one-child, two-child, and root nodes")
    lines.append("- Delete from empty container (raises)")
    lines.append("- Pop/peek from empty stack/queue (raises)")
    lines.append("- Get/remove missing key (raises KeyError)")
    lines.append("- Out-of-range index access (raises IndexError)")
    lines.append("- Already-sorted and reverse-sorted inputs")
    lines.append("- Negative numbers and mixed sign inputs")
    lines.append("- Stability of sorting algorithms")
    lines.append("- Input immutability (sorting returns a copy)")
    lines.append("- AVL balance after sorted insertions and deletions")
    lines.append("- Resize preserving data in both hash table strategies")
    lines.append("- Iterative traversals matching recursive results")
    lines.append("")
    lines.append("## Failure / error details")
    lines.append("")
    if not failures and not errors:
        lines.append("None — all tests passed.")
    else:
        for test, traceback in result.failures:
            lines.append(f"### FAILURE: {test}")
            lines.append("```")
            lines.append(traceback)
            lines.append("```")
            lines.append("")
        for test, traceback in result.errors:
            lines.append(f"### ERROR: {test}")
            lines.append("```")
            lines.append(traceback)
            lines.append("```")
            lines.append("")
    lines.append("## Conclusion")
    lines.append("")
    if failures == 0 and errors == 0:
        lines.append("All implemented data structures and algorithms passed their validation tests. "
                       "The implementation is correct across normal scenarios and edge cases.")
    else:
        lines.append(f"{failures + errors} test(s) did not pass. Review the details above before considering the implementation complete.")

    report = "\n".join(lines)
    with open(path, "w", encoding="utf-8") as f:
        f.write(report)
    print(report)
    return report


def main() -> int:
    result = discover_and_run()
    report_path = os.path.join(_PROJECT_ROOT, "TEST_VALIDATION_REPORT.md")
    write_report(result, report_path)
    print(f"\nValidation report written to {report_path}")
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())

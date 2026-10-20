# DSA Project — Data Structures and Algorithms in Python

A complete, runnable "Data Structures and Algorithms" project. Every structure
and algorithm is implemented **from scratch using only the Python standard
library** — no `collections.deque`, `heapq`, `bisect`, `dict`, or `set` inside
the hash tables, and no `list.sort()`/`sorted()` inside the sorting algorithms.

This project satisfies the course assignment: fundamental data structures
(arrays, linked lists, stacks, queues), trees (binary trees, binary search
trees, balanced AVL trees), hash tables, sorting/searching/tree-traversal
algorithms, complexity analysis, test coverage, performance comparison, and
documentation — all demonstrated through runnable scenarios.

---

## Table of contents

1. [Project layout](#project-layout)
2. [Implemented data structures](#implemented-data-structures)
3. [Implemented algorithms](#implemented-algorithms)
4. [Run the scenarios](#run-the-scenarios)
5. [Run the tests and view the validation report](#run-the-tests)
6. [Performance analysis](#performance-analysis)
7. [Design principles](#design-principles)
8. [Usage examples](#usage-examples)
9. [Project deliverables & evaluation criteria](#project-deliverables--evaluation-criteria)

---

## Project layout

```
dsa-project/
├── main.py                        # argparse entry point: runs all scenarios
├── README.md                      # this file
├── TEST_VALIDATION_REPORT.md      # generated test validation report
├── PERFORMANCE_ANALYSIS_REPORT.md # generated performance comparison report
├── project_config.json            # project configuration
├── src/dsa/                       # library package
│   ├── __init__.py                # public API exports
│   ├── linear/                    # DynamicArray, SinglyLinkedList, stacks, queues
│   │   ├── __init__.py
│   │   ├── array.py
│   │   ├── linked_list.py
│   │   ├── stack.py
│   │   └── queue.py
│   ├── trees/                     # TreeNode, BinaryTree, BST, AVL, traversals
│   │   ├── __init__.py
│   │   ├── node.py
│   │   ├── binary_tree.py
│   │   ├── bst.py
│   │   ├── avl.py
│   │   └── traversals.py
│   ├── hashing/                   # hash functions, chaining, open addressing
│   │   ├── __init__.py
│   │   ├── hash_functions.py
│   │   ├── chaining.py
│   │   └── open_addressing.py
│   ├── sorting.py                 # bubble, insertion, merge sort
│   ├── searching.py               # linear, binary (iterative + recursive)
│   └── stats.py                   # OpStats comparison/swap counters
├── scenarios/                     # runnable scenario demos (one per structure area)
│   ├── __init__.py
│   ├── dynamic_array_grades.py
│   ├── linked_list_playlist.py
│   ├── stack_undo_redo.py
│   ├── queue_scheduling.py
│   ├── binary_tree_expr.py
│   ├── bst_student_records.py
│   ├── avl_sorted_ids.py
│   ├── hash_contacts.py
│   ├── searching_inventory.py
│   └── sorting_students.py
├── tests/                         # unit tests + validation report runner
│   ├── __init__.py
│   ├── test_linear.py
│   ├── test_trees.py
│   ├── test_hashing.py
│   ├── test_sorting_searching.py
│   └── run_tests.py
├── performance/                   # performance analysis
│   ├── __init__.py
│   └── analysis.py
├── docs/
│   └── DESIGN.md                  # design principles & trade-offs
└── presentation/                  # presentation/report files
    ├── report.py                  # Python-generated presentation report
    └── report.html                # Generated HTML report
```

---

## Implemented data structures

| Structure | File | Key operations | Complexity |
|---|---|---|---|
| `DynamicArray` | `src/dsa/linear/array.py` | append, insert, delete, get, set | append amortized O(1); insert/delete O(n); get/set O(1) |
| `SinglyLinkedList` | `src/dsa/linear/linked_list.py` | insert_head, append, insert_at, delete, search, reverse | head/tail O(1); indexed O(n) |
| `StackArray` | `src/dsa/linear/stack.py` | push, pop, peek | O(1) amortized push/pop |
| `StackLinked` | `src/dsa/linear/stack.py` | push, pop, peek | O(1) push/pop |
| `QueueLinked` | `src/dsa/linear/queue.py` | enqueue, dequeue, peek | O(1) |
| `BinaryTree` | `src/dsa/trees/binary_tree.py` | level-order insert, height, size | insert O(n); height/size O(n) |
| `BinarySearchTree` | `src/dsa/trees/bst.py` | insert, search, delete, min, max | O(h); O(log n) balanced / O(n) skewed |
| `AVLTree` | `src/dsa/trees/avl.py` | insert, search, delete, is_balanced | O(log n) guaranteed |

Concrete **Balanced BST** (self-balancing via rotations); satisfies the
"BalancedTree" requirement of the assignment.
| `ChainingHashTable` | `src/dsa/hashing/chaining.py` | put, get, remove | O(1) amortized average |
| `OpenAddressingHashTable` | `src/dsa/hashing/open_addressing.py` | put, get, remove | O(1) amortized average |

---

## Implemented algorithms

### Sorting (`src/dsa/sorting.py`)
- **Bubble Sort** — O(n²) worst/average, O(n) best (already sorted), stable, O(n) space for the returned copy.
- **Insertion Sort** — O(n²) worst/average, O(n) best, stable, O(n) space for the returned copy.
- **Merge Sort** — O(n log n) all cases, stable, O(n) space.

All three accept an optional `key` function and an optional `OpStats` object that records comparisons and swaps.

### Searching (`src/dsa/searching.py`)
- **Linear Search** — O(n) worst, works on any list.
- **Binary Search (iterative)** — O(log n), requires sorted input, O(1) space.
- **Binary Search (recursive)** — O(log n), requires sorted input, O(log n) stack space.

### Tree traversals (`src/dsa/trees/traversals.py`)
- **In-order** (left-root-root), **Pre-order** (root-left-right), **Post-order** (left-right-root), **Level-order** (breadth-first).
- Each provided as a recursive generator and an explicit-stack iterative variant.

### Hashing (`src/dsa/hashing/`)
- Hash functions: `division_hash` (key % size), `polynomial_hash` (Horner's method), `djb2_hash`.
- Collision resolution: **separate chaining** and **open addressing** (linear & quadratic probing), both with grow-only resizing and load-factor thresholds.

---

## Run the scenarios

From the project root:

```bash
# Run every scenario
python main.py
python main.py --scenario all

# Run a single scenario
python main.py --scenario dynamic_array_grades
python main.py --scenario bst_student_records
python main.py --scenario avl_sorted_ids

# Run a scenario directly
python scenarios/hash_contacts.py
```

Each scenario is a standalone Python module with a `main()` function demonstrating
a real-world use case (grade book, playlist, undo/redo text editor, job
scheduler, expression tree, student records, BST-vs-AVL comparison, contact
directory, inventory search, student grade sorting).

---

## Run the tests and view the validation report

```bash
# Run all unit tests and generate TEST_VALIDATION_REPORT.md
python tests/run_tests.py
```

The test suite covers every data structure and algorithm with edge cases:
empty containers, single elements, duplicates, insert/delete at boundaries,
pop/peek on empty containers, missing-key lookups, out-of-range indexes,
sorting stability, input immutability, AVL balance preservation, hash-table
resize preserving data, and iterative-vs-recursive traversal equivalence.

The generated `TEST_VALIDATION_REPORT.md` summarizes pass/fail counts and lists
every edge case exercised.

---

## Performance analysis

```bash
# Generate PERFORMANCE_ANALYSIS_REPORT.md
python performance/analysis.py
```

The analysis benchmarks:
- **Sorting** — bubble, insertion, merge across input sizes (100–5000) and distributions (random, sorted, reverse, duplicates), capturing wall-clock time plus comparison/swap counts via `OpStats`.
- **Tree traversals** — recursive vs explicit-stack iterative in-order/pre-order/post-order across BST sizes.

The generated `PERFORMANCE_ANALYSIS_REPORT.md` includes timing tables, space/time
complexity summaries, and practical recommendations (e.g., use merge sort for
general sorting; prefer AVL over BST when input may be sorted/adversarial).

---

# Generate presentation report

```bash
# Generate presentation/report.html (open in any browser)
python presentation/report.py
```

The report (15 slides) summarizes key findings, challenges faced, and lessons
learned, plus a deliverables checklist and how-to-run commands.

---

## Design principles

See `docs/DESIGN.md` for the full design rationale. Highlights:

- **From scratch**: no built-in `dict`/`set` inside hash tables, no `list.sort`/`sorted` inside sorting algorithms, no `collections.deque` inside queues.
- **Plain lists only as raw storage**: a plain Python list is used solely as a fixed-capacity buffer (`[None] * capacity`) inside `DynamicArray`, the circular queue, and hash-table buckets/slots. Every other structure implements its own behaviour on top of its own primitives (nodes, buckets, slots).
- **Grow-only resizing**: arrays, circular queues, and hash tables grow (never shrink) when full / over load threshold.
- **Set-like trees**: BST and AVL ignore duplicates to keep the tree a clean ordered set.
- **Tombstones**: open addressing uses a tombstone sentinel so deletions never break probe sequences.
- **Complexity documented**: every public method carries a `Time:` / `Space:` docstring.
- **Scenario-driven**: each structure is demonstrated through a concrete real-world scenario under `scenarios/`.

---

## Usage examples

### Dynamic array (grade book)

```python
from src.dsa.linear import DynamicArray

grades = DynamicArray()
grades.append("Ada")
grades.append(92)
grades.append("Linus")
grades.append(88)

print(grades.get(0), grades.get(1))   # Ada 92
print(len(grades))                    # 4
```

### Singly linked list (playlist)

```python
from src.dsa.linear import SinglyLinkedList

playlist = SinglyLinkedList()
playlist.append("Bohemian Rhapsody")
playlist.append("Stairway to Heaven")
playlist.insert_head("Billie Jean")
playlist.delete("Stairway to Heaven")
print("Hotel California" in playlist)  # False (not added)
playlist.reverse()
```

### Stack (undo/redo)

```python
from src.dsa.linear import StackArray

undo = StackArray()
redo = StackArray()
undo.push("type Hello")
undo.push("type World")
last = undo.pop()          # "type World"
redo.push(last)
```

### Queue (job scheduling)

```python
from src.dsa.linear import QueueLinked

queue = QueueLinked()
queue.enqueue(Job(1, "Print report.pdf"))
queue.enqueue(Job(2, "Render video.mp4"))
while not queue.is_empty():
    job = queue.dequeue()   # FIFO order
```

### Binary search tree (student records)

```python
from src.dsa.trees import BinarySearchTree

tree = BinarySearchTree()
tree.insert(StudentRecord(102, "Grace Hopper", 95.0))
tree.insert(StudentRecord(101, "Ada Lovelace", 92.0))
print([r.student_id for r in tree])   # [101, 102] (in-order = ascending)
print(101 in tree)                    # True
tree.delete(StudentRecord(102, "", 0.0))
```

### AVL tree (self-balancing on sorted input)

```python
from src.dsa.trees import AVLTree, BinarySearchTree

avl = AVLTree()
bst = BinarySearchTree()
for i in range(1, 1001):
    avl.insert(i)
    bst.insert(i)
print(avl.height())   # small (~log n)
print(bst.height())   # 999 (degenerate linked list)
print(avl.is_balanced())  # True
```

### Tree traversals

```python
from src.dsa.trees import BinaryTree
from src.dsa.trees import traversals as T

tree = BinaryTree(1)
tree.insert(2)
tree.insert(3)
print(list(T.in_order(tree.root)))       # recursive
print(list(T.in_order_iterative(tree.root)))  # iterative, same result
```

### Hash tables

```python
from src.dsa.hashing import ChainingHashTable, division_hash

table = ChainingHashTable(hash_function=division_hash)
table.put(101, "Ada")
table.put(104, "Linus")
print(table.get(101))   # Ada
print(999 in table)     # False
table.remove(101)
```

```python
from src.dsa.hashing import OpenAddressingHashTable, polynomial_hash

table = OpenAddressingHashTable(hash_function=polynomial_hash, probe="quadratic")
table.put("Ada", "ada@example.com")
print(table.get("Ada"))
```

### Sorting with stats

```python
from src.dsa.sorting import bubble_sort, merge_sort
from src.dsa.stats import OpStats

stats = OpStats()
sorted_grades = bubble_sort(grades, key=lambda g: g.grade, stats=stats)
print(sorted_grades)
print(f"comparisons={stats.comparisons}, swaps={stats.swaps}")
```

### Searching

```python
from src.dsa.searching import linear_search, binary_search_iterative

index = linear_search([10, 20, 30, 40], 30)   # 2
index = binary_search_iterative([1, 3, 5, 7, 9], 5)  # 2
```

---

## Project deliverables

| # | Deliverable / Criterion | Where it lives | Status |
|---|---|---|---|
| 1 | Python code implementing all data structures & algorithms (trees + hash tables) | `src/dsa/`, `scenarios/` | ✅ Complete |
| 2 | Documentation (design principles, functionality, usage examples) | `README.md`, `docs/DESIGN.md`, inline docstrings | ✅ Complete |
| 3 | Test cases & validation report (scenarios + edge cases) | `tests/`, `TEST_VALIDATION_REPORT.md` | ✅ Complete |
| 4 | Performance analysis report (time/space complexity comparison) | `performance/`, `PERFORMANCE_ANALYSIS_REPORT.md` | ✅ Complete |
| 5 | Presentation report (key findings, challenges, lessons learned) | `presentation/report.py` (+ generated HTML) | ✅ Complete |

---

## Requirements

- Python 3.9+ (uses `from __future__ import annotations` and `X \| None` syntax).
- Standard library only — no third-party packages.

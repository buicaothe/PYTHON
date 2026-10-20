# Design Principles & Trade-offs

This document explains the design decisions behind the DSA project implementation.

---

## 1. From-scratch implementation

Every data structure and algorithm is implemented from scratch using only the
Python standard library. Specifically:

- **No `dict` / `set` inside hash tables** — chaining uses plain lists as buckets; open addressing uses a plain list as the slot buffer.
- **No `list.sort()` / `sorted()` inside sorting algorithms** — bubble, insertion, and merge sort perform their own comparisons and moves.
- **No `collections.deque`** — queues use a linked list (`QueueLinked`).
- **No `heapq` / `bisect`** — not needed for the required structures.

This satisfies the assignment's requirement that students "design and implement" the structures themselves rather than wrapping built-ins.

---

## 2. Plain lists are raw storage only

A plain Python list (`[None] * capacity`) appears in exactly three places:

1. `DynamicArray._storage` — the growable array's backing buffer.
3. Hash-table buckets (`ChainingHashTable._buckets`) and slots (`OpenAddressingHashTable._slots`).

In every other structure, behaviour is built from custom primitives (`_Node`, `TreeNode`, buckets, slots). The list is never used as a general-purpose container that would hide the data-structure logic.

---

## 3. Grow-only resizing policy

`DynamicArray`, and both hash tables grow when full or
when the load factor crosses a threshold, but never shrink. Rationale:

- Simplicity: no shrink heuristics to tune or bugs from thrashing near the threshold.
- Predictability: capacity only increases, so references/indices remain stable longer.
- Matches the "growth" focus of the assignment (dynamic arrays, hash-table resizing).

The growth factor is `2` everywhere, giving amortized O(1) append/enqueue/put.

---

## 4. Set-like trees (duplicates ignored)

`BinarySearchTree.insert` and `AVLTree.insert` return `False` on duplicates and
do not insert a second node. Rationale:

- Keeps the tree a clean ordered set, matching the typical BST/ADT abstraction.
- Avoids ambiguity about where a duplicate belongs (left subtree? right subtree? both?).
- Simplifies delete (single node per value).

`BinaryTree` (generic, non-ordered) allows any values including duplicates because it has no ordering constraint.

---

## 5. Balanced BST (AVLTree) via recursive return values

`AVLTree` uses no parent pointers. Each recursive insert/delete returns the new
subtree root, and rotations are applied on the way back up the recursion:

```
_insert(node, value):
    recurse left/right
    return _balance(node)   # restore balance factors in {-1, 0, +1}
```

Rationale:

- Parent pointers add memory and complexity; the return-value idiom is simpler
  and easier to reason about at the student level.
- Balance factor is computed from child heights each time (O(h) per node visited
  during rebalance), keeping the code readable at the cost of a small constant.

---

## 6. Open addressing with tombstones + triangular quadratic probing

`OpenAddressingHashTable`:

- Deleted slots become a `_TOMBSTONE` sentinel rather than `None`. This keeps
  probe sequences intact: lookups skip tombstones, inserts reuse the first
  tombstone seen.
- Quadratic probing uses **triangular numbers** (`i*(i+1)//2`) rather than `i*i`.
  For power-of-two table sizes, triangular offsets are guaranteed to visit every
  slot; plain `i^2` probing visits only about half. This prevents the "table
  full" failure at ~50% load.

---

## 7. Collision counting semantics

- **Chaining**: `_collision_count` increments when a new key lands in a bucket
  that already holds entries (a chain collision).
- **Open addressing**: `_collision_count` increments for every live slot probed
  before landing on the empty/tombstone insert slot.

These are observable via `collision_count()` and demonstrated in the
`hash_contacts.py` scenario.

---

## 8. Complexity documented on every method

Every public method carries a `Time:` / `Space:` line in its docstring. This
makes the analysis deliverable self-documenting and lets students see the
efficiency characteristics alongside the code.

---

## 9. Scenario-driven design

Each structure is paired with a scenario under `scenarios/`:

| Scenario | Structure | Real-world framing |
|---|---|---|
| `dynamic_array_grades.py` | DynamicArray | student grade book |
| `linked_list_playlist.py` | SinglyLinkedList | music playlist |
| `stack_undo_redo.py` | StackArray | text-editor undo/redo + bracket matching |
| `queue_scheduling.py` | QueueLinked | print-job FIFO scheduler |
| `binary_tree_expr.py` | BinaryTree | arithmetic expression tree |
| `bst_student_records.py` | BinarySearchTree | student record lookup by ID |
| `avl_sorted_ids.py` | AVLTree vs BST | sorted-input height comparison |
| `hash_contacts.py` | both hash tables + hash functions | contact directory, word frequency, collision demo |
| `searching_inventory.py` | linear + binary search | product inventory lookup |
| `sorting_students.py` | all three sorts | student grade sorting with stats |

Scenarios make the implementation concrete and show *using scenarios* as the
assignment requires.

---

## 10. Testing philosophy

The test suite (`tests/`) is independent of the scenarios and covers:

- Normal operation of every public method.
- Edge cases: empty/single-element containers, duplicates, boundary inserts/deletes,
  pop/peek/get on empty (raises), missing keys (raises KeyError), out-of-range
  indexes (raises IndexError).
- Correctness invariants: sorting matches `sorted()`, traversals match between
  recursive and iterative variants, AVL stays balanced after sorted inserts and
  deletes, hash-table resize preserves all data.
- Sorting stability and input immutability (sorting returns a copy).

`tests/run_tests.py` runs everything and writes `TEST_VALIDATION_REPORT.md`.

---

## 11. Known limitations

- `BinaryTree.insert` is level-order only; there is no ordered/generic insert
  API (that is the role of `BinarySearchTree` / `AVLTree`).
- Hash tables are grow-only; they never shrink after mass deletion.
- AVL balance factor is recomputed from child heights on each rebalance step
  rather than stored per node — fine for clarity, slightly more work per rebalance.
- `binary_search_*` assumes the input is sorted; unsorted input yields undefined
  (but crash-free) results.

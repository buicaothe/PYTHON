# DSA Project — Test Validation Report

Generated: 2026-10-20T08:40:13.323185

## Summary

- Total test cases run: 111
- Passed: 111
- Failed: 0
- Errors: 0
- Success rate: 100.0%

## Modules covered

- `tests/test_linear.py` — DynamicArray, SinglyLinkedList, StackArray, StackLinked, QueueLinked
- `tests/test_trees.py` — BinaryTree, BinarySearchTree, AVLTree, traversals (in-order, pre-order, post-order, level-order)
- `tests/test_hashing.py` — division_hash, polynomial_hash, djb2_hash, ChainingHashTable, OpenAddressingHashTable
- `tests/test_sorting_searching.py` — bubble_sort, insertion_sort, merge_sort, linear_search, binary_search (iterative & recursive)

## Edge cases covered

- Empty containers (empty list, empty tree, empty hash table)
- Single-element containers
- Duplicate values / keys
- Insert at head, middle, and tail
- Delete leaf, one-child, two-child, and root nodes
- Delete from empty container (raises)
- Pop/peek from empty stack/queue (raises)
- Get/remove missing key (raises KeyError)
- Out-of-range index access (raises IndexError)
- Already-sorted and reverse-sorted inputs
- Negative numbers and mixed sign inputs
- Stability of sorting algorithms
- Input immutability (sorting returns a copy)
- AVL balance after sorted insertions and deletions
- Resize preserving data in both hash table strategies
- Iterative traversals matching recursive results

## Failure / error details

None — all tests passed.
## Conclusion

All implemented data structures and algorithms passed their validation tests. The implementation is correct across normal scenarios and edge cases.
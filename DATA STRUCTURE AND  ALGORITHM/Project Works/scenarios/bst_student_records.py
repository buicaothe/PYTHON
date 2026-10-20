"""Scenario: student record lookup by ID with a :class:`BinarySearchTree`.

Run directly: ``python scenarios/bst_student_records.py``
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dsa.trees import BinarySearchTree


class StudentRecord:
    """A simple student record keyed by integer id.

    Comparison is by ``student_id`` so the record can be stored directly in a
    :class:`BinarySearchTree` and searched by id.
    """

    def __init__(self, student_id: int, name: str, grade: float) -> None:
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def __lt__(self, other: "StudentRecord") -> bool:
        return self.student_id < other.student_id

    def __eq__(self, other: object) -> bool:
        return isinstance(other, StudentRecord) and self.student_id == other.student_id

    def __repr__(self) -> str:
        return f"StudentRecord(id={self.student_id}, name={self.name!r}, grade={self.grade})"


def main() -> None:
    # The BST stores StudentRecord objects, ordered by student_id.
    tree: BinarySearchTree = BinarySearchTree()
    records = [
        StudentRecord(102, "Grace Hopper", 95.0),
        StudentRecord(105, "Linus Torvalds", 88.0),
        StudentRecord(101, "Ada Lovelace", 92.0),
        StudentRecord(107, "Margaret Hamilton", 99.0),
        StudentRecord(104, "Katherine Johnson", 90.0),
    ]
    for record in records:
        tree.insert(record)

    print(f"Tree size: {tree.size()}, height: {tree.height()}")
    print("IDs in ascending order:", [r.student_id for r in tree])

    for sid in (101, 104, 107, 999):
        probe = StudentRecord(sid, "", 0.0)
        if probe in tree:
            # Recover the stored record by id.
            for record in tree:
                if record.student_id == sid:
                    print(f"Found: {record}")
                    break
        else:
            print(f"No student with id {sid}")

    # Delete a record and show the tree still works.
    target = StudentRecord(105, "", 0.0)
    removed = tree.delete(target)
    print(f"\nDeleted id 105: {removed}")
    print("IDs now:", [r.student_id for r in tree])
    print(f"105 still present: {StudentRecord(105, '', 0.0) in tree}")


if __name__ == "__main__":
    main()
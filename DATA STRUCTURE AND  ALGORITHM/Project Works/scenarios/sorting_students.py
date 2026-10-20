"""Scenario: sort student records by grade with all three algorithms.

Run directly: ``python scenarios/sorting_students.py``
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dsa.sorting import bubble_sort, insertion_sort, merge_sort
from src.dsa.stats import OpStats


class Student:
    """A student record with a name and a numeric grade."""

    def __init__(self, name: str, grade: float) -> None:
        self.name = name
        self.grade = grade

    def __repr__(self) -> str:
        return f"{self.name} ({self.grade})"


def grade_key(student: Student) -> float:
        """Return the student's grade, used as the sort key."""
        return student.grade


def main() -> None:
    students = [
        Student("Ada", 92.0),
        Student("Linus", 88.0),
        Student("Grace", 95.0),
        Student("Margaret", 79.0),
        Student("Katherine", 90.0),
    ]

    for name, fn in (("bubble", bubble_sort), ("insertion", insertion_sort), ("merge", merge_sort)):
        stats = OpStats()
        result = fn(students, key=grade_key, stats=stats)
        print(f"{name}_sort: {[repr(s) for s in result]}")
        print(f"  comparisons={stats.comparisons}, swaps={stats.swaps}")


if __name__ == "__main__":
    main()
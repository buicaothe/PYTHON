"""Scenario: a student grade book backed by a :class:`DynamicArray`.

Run directly: ``python scenarios/dynamic_array_grades.py``
"""

from __future__ import annotations

import sys
import os

# Allow running this file directly from the project root.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dsa.linear import DynamicArray


def main() -> None:
    grades = DynamicArray()
    # Each entry is a (name, grade) pair stored in adjacent slots.
    names = ["Ada", "Linus", "Grace", "Margaret"]
    scores = [92, 88, 95, 79]
    for name, score in zip(names, scores):
        grades.append(name)
        grades.append(score)

    print("Grade book contents:")
    for i in range(0, len(grades), 2):
        print(f"  {grades.get(i)}: {grades.get(i + 1)}")

    # Demonstrate insert/delete on the underlying array.
    grades.insert(0, "Headmaster")
    grades.insert(1, 100)
    print("\nAfter inserting Headmaster/100 at the front:")
    for i in range(0, len(grades), 2):
        print(f"  {grades.get(i)}: {grades.get(i + 1)}")

    removed_name = grades.delete(0)
    removed_score = grades.delete(0)
    print(f"\nRemoved from front: {removed_name} ({removed_score})")

    total = 0
    count = 0
    for i in range(1, len(grades), 2):
        total += grades.get(i)
        count += 1
    print(f"\nClass average: {total / count:.1f}")


if __name__ == "__main__":
    main()
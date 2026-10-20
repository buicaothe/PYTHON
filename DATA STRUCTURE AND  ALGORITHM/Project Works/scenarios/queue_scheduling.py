"""Scenario: print-job / support-ticket scheduling with a FIFO queue.

Run directly: ``python scenarios/queue_scheduling.py``
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dsa.linear import QueueLinked


class Job:
    """A simple named work item with an id."""

    def __init__(self, job_id: int, name: str) -> None:
        self.job_id = job_id
        self.name = name

    def __repr__(self) -> str:
        return f"Job({self.job_id}, {self.name!r})"


def main() -> None:
    queue: QueueLinked = QueueLinked()
    for job_id, name in [
        (1, "Print report.pdf"),
        (2, "Render video.mp4"),
        (3, "Backup database"),
    ]:
        queue.enqueue(Job(job_id, name))

    print("Jobs waiting in queue:")
    for job in queue:
        print(f"  - {job}")

    print("\nProcessing in FIFO order:")
    while not queue.is_empty():
        job = queue.dequeue()
        print(f"  Processed {job}")


if __name__ == "__main__":
    main()
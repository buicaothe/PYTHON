"""Operation counters shared by the sorting and searching modules."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class OpStats:
    """Counts of comparisons and swaps performed by an algorithm.

    Pass an instance into a sorting or searching function to have it
    increment the counters as it works; ``stats=None`` (the default) adds no
    meaningful overhead because the counter increments are skipped entirely.
    """

    comparisons: int = 0
    swaps: int = 0
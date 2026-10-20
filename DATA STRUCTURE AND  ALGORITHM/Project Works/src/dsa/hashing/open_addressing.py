"""Hash table using open addressing with linear or quadratic probing.

The buffer is a plain ``[None] * capacity`` list.  A slot holds either
``None`` (never used), a ``(key, value)`` pair, or the sentinel ``_TOMBSTONE``
to mark a deleted slot that must be skipped (but not treated as empty) during
lookups.  Probing is either linear (step = 1) or quadratic (step = i*i).

Resize is grow-only: when the load factor crosses a threshold the table
doubles its capacity and rehashes every live entry.
"""

from __future__ import annotations

from typing import Any, Iterator

from src.dsa.hashing.hash_functions import division_hash

_TOMBSTONE = object()


class OpenAddressingHashTable:
    """A hash table resolved by open addressing (linear or quadratic probe)."""

    INITIAL_CAPACITY: int = 8
    LOAD_THRESHOLD: float = 0.75

    def __init__(
        self,
        capacity: int = INITIAL_CAPACITY,
        hash_function=division_hash,
        load_threshold: float = LOAD_THRESHOLD,
        probe: str = "linear",
    ) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        if not 0.0 < load_threshold <= 1.0:
            raise ValueError("load_threshold must be in (0, 1]")
        if probe not in ("linear", "quadratic"):
            raise ValueError("probe must be 'linear' or 'quadratic'")
        self._hash_function = hash_function
        self._load_threshold = load_threshold
        self._probe = probe
        # Plain list used purely as raw fixed-capacity storage.
        self._slots: list[Any] = [None] * capacity
        self._size: int = 0
        self._collision_count: int = 0
        self._resize_count: int = 0

    @property
    def capacity(self) -> int:
        return len(self._slots)

    def _probe_offset(self, attempt: int) -> int:
        """Return the cumulative offset for the ``attempt``-th probe (0-based).

        ``linear`` steps by 1 each time, so the offset is just ``attempt``.
        ``quadratic`` uses triangular numbers (``attempt * (attempt + 1) // 2``)
        rather than ``attempt * attempt``: triangular numbers are guaranteed to
        visit every slot of a power-of-two table, whereas plain ``i^2``
        probing only visits about half of them.
        """
        if self._probe == "linear":
            return attempt
        return attempt * (attempt + 1) // 2

    def _find_slot(self, key: Any) -> "tuple[int, bool, int | None]":
        """Return ``(index, found, tombstone_index)`` for ``key``.

        ``found`` is ``True`` when a live entry matching ``key`` is located.
        When not found, ``index`` is where a new entry should be inserted:
        the first tombstone seen during probing, or the first empty slot.
        ``tombstone_index`` is the remembered tombstone slot (or ``None``).
        """
        capacity = self.capacity
        first_tombstone: int | None = None
        for attempt in range(capacity):
            index = (self._hash_function(key, capacity) + self._probe_offset(attempt)) % capacity
            slot = self._slots[index]
            if slot is None:
                target = first_tombstone if first_tombstone is not None else index
                return target, False, first_tombstone
            if slot is _TOMBSTONE:
                if first_tombstone is None:
                    first_tombstone = index
                continue
            if slot[0] == key:
                return index, True, first_tombstone
        # Every slot in the probe sequence was live or a tombstone.  If we
        # saw a tombstone, reuse it; otherwise the table is effectively full.
        if first_tombstone is not None:
            return first_tombstone, False, first_tombstone
        raise RuntimeError("hash table is full; probe sequence exhausted")

    def put(self, key: Any, value: Any) -> None:
        """Insert or update ``key`` -> ``value``.

        Time: O(1) amortized (probe walk + occasional resize).
        Space: O(1) amortized.
        """
        if self.load_factor() >= self._load_threshold:
            self._resize(self.capacity * 2)
        try:
            index, found, _ = self._find_slot(key)
        except RuntimeError:
            # Tombstones filled the whole probe sequence; grow and retry.
            self._resize(self.capacity * 2)
            index, found, _ = self._find_slot(key)
        if found:
            self._slots[index] = (key, value)
            return
        # A new key: count a collision for every live slot we probed before
        # landing on the empty/tombstone slot where we will insert.
        capacity = self.capacity
        for attempt in range(capacity):
            probe_index = (self._hash_function(key, capacity) + self._probe_offset(attempt)) % capacity
            slot = self._slots[probe_index]
            if probe_index == index:
                self._slots[index] = (key, value)
                self._size += 1
                return
            if slot is not _TOMBSTONE:
                self._collision_count += 1

    def get(self, key: Any) -> Any:
        """Return the value for ``key``; raise ``KeyError`` if absent.

        Time: O(1) amortized.
        Space: O(1).
        """
        index, found, _ = self._find_slot(key)
        if not found:
            raise KeyError(key)
        return self._slots[index][1]

    def remove(self, key: Any) -> None:
        """Remove ``key`` by marking its slot as a tombstone.

        Time: O(1) amortized.
        Space: O(1).
        """
        index, found, _ = self._find_slot(key)
        if not found:
            raise KeyError(key)
        self._slots[index] = _TOMBSTONE
        self._size -= 1

    def __contains__(self, key: Any) -> bool:
        _, found, _ = self._find_slot(key)
        return found

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        for slot in self._slots:
            if slot is not None and slot is not _TOMBSTONE:
                yield slot[0]

    def load_factor(self) -> float:
        """Return live-size / capacity (tombstones still occupy a slot)."""
        return self._size / self.capacity

    def collision_count(self) -> int:
        """Return the number of probes that hit an occupied slot."""
        return self._collision_count

    def resize_count(self) -> int:
        """Return the number of resizes performed so far."""
        return self._resize_count

    def _resize(self, new_capacity: int) -> None:
        """Rehash every live entry into a fresh plain-list buffer."""
        old_slots = self._slots
        self._slots = [None] * new_capacity
        self._size = 0
        for slot in old_slots:
            if slot is not None and slot is not _TOMBSTONE:
                index, found, _ = self._find_slot(slot[0])
                self._slots[index] = slot
                self._size += 1
        self._resize_count += 1

    def __repr__(self) -> str:
        return (
            f"OpenAddressingHashTable(probe={self._probe!r}, "
            f"size={self._size}, capacity={self.capacity}, "
            f"load_factor={self.load_factor():.3f})"
        )
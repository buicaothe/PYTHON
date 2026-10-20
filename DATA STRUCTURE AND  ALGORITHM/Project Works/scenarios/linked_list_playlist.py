"""Scenario: a music playlist backed by a :class:`SinglyLinkedList`.

Run directly: ``python scenarios/linked_list_playlist.py``
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dsa.linear import SinglyLinkedList


def main() -> None:
    playlist = SinglyLinkedList()
    for track in ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"]:
        playlist.append(track)

    print("Playlist (in order):")
    for track in playlist:
        print(f"  - {track}")

    # Insert a track at the front (newest first).
    playlist.insert_head("Billie Jean")
    print("\nAfter adding 'Billie Jean' to the top:")
    for track in playlist:
        print(f"  - {track}")

    # Remove a track by value.
    removed = playlist.delete("Stairway to Heaven")
    print(f"\nRemoved 'Stairway to Heaven': {removed}")

    # Search for a track.
    print(f"Contains 'Hotel California': {playlist.search('Hotel California')}")
    print(f"Contains 'Missing Song': {playlist.search('Missing Song')}")

    # Reverse the playlist for a "now playing" view.
    playlist.reverse()
    print("\nReversed (now playing):")
    for track in playlist:
        print(f"  - {track}")


if __name__ == "__main__":
    main()
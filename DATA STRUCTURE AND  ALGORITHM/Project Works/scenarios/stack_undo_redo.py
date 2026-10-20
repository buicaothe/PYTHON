"""Scenario: text-editor undo/redo with two stacks, plus a parentheses checker.

Run directly: ``python scenarios/stack_undo_redo.py``
"""

from __future__ import annotations

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dsa.linear import StackArray


class TextEditor:
    """A minimal text editor keeping an undo stack and a redo stack.

    Every accepted edit is pushed onto the undo stack; redoing an edit clears
    the redo stack because the new edit invalidates any previously redone
    state.
    """

    def __init__(self) -> None:
        self._undo: StackArray = StackArray()
        self._redo: StackArray = StackArray()
        self._text: str = ""

    def do(self, action: str) -> None:
        """Apply ``action`` (a string to append) and push it for undo."""
        self._text += action
        self._undo.push(action)
        # New edit invalidates the redo history.
        self._redo = StackArray()

    def undo(self) -> str | None:
        """Pop the most recent edit off the undo stack and revert it.

        Returns the reverted action text, or ``None`` if there is nothing to
        undo.  The reverted action is pushed onto the redo stack.
        """
        if self._undo.is_empty():
            return None
        action = self._undo.pop()
        # Revert by dropping the trailing characters that this action added.
        self._text = self._text[: len(self._text) - len(action)]
        self._redo.push(action)
        return action

    def redo(self) -> str | None:
        """Pop the most recent undone edit off the redo stack and reapply it.

        Returns the reapplied action text, or ``None`` if there is nothing to
        redo.
        """
        if self._redo.is_empty():
            return None
        action = self._redo.pop()
        self._text += action
        self._undo.push(action)
        return action

    @property
    def text(self) -> str:
        return self._text


def is_balanced(expression: str) -> bool:
    """Return ``True`` when every opening bracket has a matching closer.

    Uses a single stack: opening brackets are pushed; closing brackets must
    match the top of the stack or the expression is unbalanced.

    Time: O(n).
    Space: O(n) worst case (all characters are opening brackets).
    """
    stack: StackArray = StackArray()
    pairs = {"(": ")", "[": "]", "{": "}"}
    for ch in expression:
        if ch in pairs:
            stack.push(ch)
        elif ch in pairs.values():
            if stack.is_empty():
                return False
            opener = stack.pop()
            if pairs[opener] != ch:
                return False
    return stack.is_empty()


def main() -> None:
    editor = TextEditor()
    for word in ["Hello", " ", "World", "!"]:
        editor.do(word)
    print(f"Text after typing: {editor.text!r}")

    undone = editor.undo()
    print(f"Undo: removed {undone!r} -> {editor.text!r}")
    undone = editor.undo()
    print(f"Undo: removed {undone!r} -> {editor.text!r}")

    redone = editor.redo()
    print(f"Redo: reapplied {redone!r} -> {editor.text!r}")

    # Balanced-parentheses checks.
    samples = ["()[]{}", "(]", "([)]", "((()))", "((())"]
    for sample in samples:
        print(f"is_balanced({sample!r}) = {is_balanced(sample)}")


if __name__ == "__main__":
    main()
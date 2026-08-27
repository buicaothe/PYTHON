# 1. IMPORT FUCTIONS FROM puzzle.py:
import puzzle
from random import shuffle

while True:
    target = input('Input letter of 15 characters: ')
    if len(target) == 15:
        break
    else:
        print(
            f"You have enter {len(target)} characters. Please make sure this is 15 characters!")

original, indexes = puzzle.prepare(target, n=4)

puzzle.play(original, indexes, n=4)

import random

# 1 ------------ PREPARATION STAGE ------------
# Original Immutable Tuple - One-dimentional) :
# Chọn chữ gồm 15 ký tự:

while True:
    selection = input('Nhập chữ có 15 ký tự: ')
    if len(selection) == 15:
        break

ORIGINAL = tuple(selection)

# Solvable or not?
solvable = False
while solvable == False:
    # Create a Mutable List:
    indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    # Shuffle the indexes:
    random.shuffle(indexes)

    # Check the Inversions (solvable):
    inversions = 0
    for i in range(15):
        for j in range(i + 1, 15):
            # Pair (a, b) form an inversion if a before b but a > b
            if indexes[i] > indexes[j]:
                inversions += 1

    # If the number of inversions is even --> solvable!
    if inversions % 2 == 0:
        solvable = True

# 2 ------------ BOARD SETUP ------------
board = []
for i in range(15):
    # Put the items from ORIGINAL into a new board with shuffled indexes:
    board.append(ORIGINAL[indexes[i]])

# Add the Blank Slot to the end of board:
board.append(" ")

# 3 ------------ SOLVING LOOP ------------
while True:
    print('--- WELCOME TO SLIDING PUZZLE 4x4 ---')
    # Print the board 4x4:
    for i in range(0, 16, 4):
        print(board[i], "\t", board[i+1], "\t", board[i+2], "\t", board[i+3])

    # Check whether matching ORIGINAL
    solved = True
    for i in range(15):
        if board[i] != ORIGINAL[i]:
            solved = False

    # If the Matching and the last slot is Blank --> Winner:
    if solved and board[15] == " ":
        print("Congratulation! You win!!!!!!!!!!!")
        break

    # Request the User to choose the number to move
    # Programme will crash if the number is not is the board!
    move = int(input("Enter the number to move: "))

    # Find the index of the Selected Slot and the Blank Slot
    index_move = -1
    index_empty = -1
    for i in range(16):
        if board[i] == move:
            index_move = i
        if board[i] == " ":
            index_empty = i

    # Calcuate row and column from one-directional index
    row_move = index_move // 4
    col_move = index_move % 4
    row_empty = index_empty // 4
    col_empty = index_empty % 4

    # Calculate the distance rows and columns:
    diff_row = abs(row_move - row_empty)
    diff_col = abs(col_move - col_empty)

    # Check the slot is adjacient to Bank slot: allow to swap if true:
    if (row_move == row_empty and diff_col == 1) or (col_move == col_empty and diff_row == 1):
        # Swapping with the Black Slot (using "temp" variable)
        temp = board[index_empty]
        board[index_empty] = board[index_move]
        board[index_move] = temp
    else:
        print("Invalid number - The selected number is not next to the Blank Slot or outside the range!")
        print("Please enter a valid number:")

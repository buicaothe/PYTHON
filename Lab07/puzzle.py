'''https://www.geeksforgeeks.org/dsa/check-instance-15-puzzle-solvable/
If N is even, puzzle instance is solvable if 
-   the blank is on an even row counting from the bottom 
    (second-last, fourth-last, etc.) and number of inversions is odd.
-   the blank is on an odd row counting from the bottom 
    (last, third-last, fifth-last, etc.) and number of inversions is even.
'''
from random import shuffle


def prepare(word, n=4):
    #  even number of rows and columns

    #  example contents of the board
    # word = "dermatoglyphics" # "uncopyrightable" # 'ABCDEFGHIJKLMNO' # tuple(map(str, range(1, n*n)))
    #  original has the solved content without the blank tile
    #  board contains the indexes of the original board

    original = tuple(word.upper())  # numbers
    # list of indexes of the original board
    indexes = list(range(len(original)))
    while True:  # keep shuffling until we get an even number of inversions
        shuffle(indexes)
        if inversions(indexes) % 2 != 0:
            break
    return original, indexes


def inversions(indexes, n=4):
    #  calculate the inversions
    #  a pair of tiles (a, b) form an inversion if a appears before b but a > b
    inversions = 0
    for i in range(n*n - 1):
        for j in range(i+1, n*n - 1):
            if indexes[i] > indexes[j]:
                inversions += 1

    return inversions


def move(move_index, blank_index, n, board):
    #  check if the tile to move is adjacent (row or column) to the blank tile
    if (move_index == blank_index - 1 and blank_index % n != 0) or \
        (move_index == blank_index + 1 and blank_index % n != n - 1) or \
        (move_index == blank_index - n and blank_index >= n) or \
            (move_index == blank_index + n and blank_index < n*(n-1)):
        #  swap the tile with the blank tile
        board[move_index], board[blank_index] = board[blank_index], board[move_index]
        return board
    else:
        return None


def print_puzzle(board, n):
    #  print the board
    for i in range(n):
        for j in board[i*n:(i+1)*n]:
            print(f'{j:^3}', end=' ')
        print()


def issolved(board, original):
    #  original is a tuple
    return tuple(board[:-1]) == original


def play(original, indexes, n=4):
    board = [str(original[i]) for i in indexes]
    # blank tile, last row (=1) counting from the bottom is odd
    board.insert(10, '_')

    print(f"Solve the puzzle - {''.join(original)}")

    while True:
        print_puzzle(board, n)
        if issolved(board, original):
            print('Congratulations! You solved the puzzle!')
            break
        # get user input
        user_move = input('Enter the tile to move: ').upper()
        #  find the index of the tile to move
        if user_move in board:
            move_index = board.index(user_move)
            blank_index = board.index('_')
            move(move_index, blank_index, n, board)


if __name__ == "__main__":
    original, indexes = prepare('ABCDEFGHIJKLMNO', n=4)
    play(original, indexes, n=4)

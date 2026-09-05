'''
_____________LAB4_C____________
1. AI Tool: Gemini (Google)
2. Prompts used:
    "Write a code (Python 3.14) to create 4x4 board game"
'''
def create_board(size=4):
    # Creates a 2D list: [['.', '.', '.', '.'], ...]
    return [["." for _ in range(size)] for _ in range(size)]

def print_board(board, player_pos):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if (r, c) == player_pos:
                print("P", end=" ") # Player icon
            else:
                print(board[r][c], end=" ")
        print() # New line after each row

def main():
    board_size = 4
    board = create_board(board_size)
    # Player starts at top-left (row 0, column 0)
    p_row, p_col = 0, 0

    print("Welcome to the 4x4 Navigator!")
    print("Use W (up), A (left), S (down), D (right) to move. Type 'q' to quit.")

    while True:
        print("\n--- Current Board ---")
        print_board(board, (p_row, p_col))
        
        move = input("Move: ").lower()

        if move == 'q':
            break
        elif move == 'w' and p_row > 0:
            p_row -= 1
        elif move == 's' and p_row < board_size - 1:
            p_row += 1
        elif move == 'a' and p_col > 0:
            p_col -= 1
        elif move == 'd' and p_col < board_size - 1:
            p_col += 1
        else:
            print("Invalid move or hit a wall!")

if __name__ == "__main__":
    main()
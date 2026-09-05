import puzzle as library
import tkinter as tk
import tkinter.ttk as ttk  # basic Tk widgets are overridden
import tkinter.messagebox as mb
import tkinter.font as font

# Global variable to track the blank tile index
empty = 0


def preparecontent(word: str) -> tuple:
    # original, indexes = puzzle.prepare(word)
    original, indexes = library.prepare(word)
    board = [str(original[i]) for i in indexes]
    # blank tile, last row (=1) counting from the bottom is odd
    blank_index = 10
    board.insert(blank_index, '')
    return board, blank_index


def is_ready(board, word):
    # calls puzzle’s issolved function
    if library.issolved(board, tuple(word.upper())):
        mb.showinfo("Good work!", "You solved it!")


def move(tilenum: int, bcontent: list, board: list) -> None:
    global empty
    n = 4
    # passing the selected button’s index, index of the empty slot, rows, and board
    result = library.move(tilenum, empty, n, board)

    if result is not None:
        # swap the contents of the buttons
        bcontent[tilenum].config(text=board[tilenum])
        bcontent[empty].config(text=board[empty])

        # update the empty's new value
        new_empty = tilenum
        # set the empty button disabled and enable the previous button
        bcontent[new_empty].config(state=tk.DISABLED)
        bcontent[empty].config(state=tk.NORMAL)
        empty = new_empty


def create_layout(word: str, n: int = 4):
    global empty
    root = tk.Tk()
    s = ttk.Style()
    s.configure('.', font=('Helvetica', 20))  # style's name is now '.'
    root.title(f'Arrange-the-puzzle')
    root.geometry('450x450')

    bcontent = []
    board, empty = preparecontent(word)

    # Loop to create 16 buttons
    for i in range(n * n):
        # Callback is now a list with two function calls
        button = ttk.Button(root,
                            command=lambda i=i: [
                                move(i, bcontent, board), is_ready(board, word)],
                            text=board[i])

        # Each button fills its cell in the grid
        button.grid(row=i//n, column=i % n, padx=5, pady=5, sticky=tk.NSEW)
        root.rowconfigure(i//n, weight=1)
        root.columnconfigure(i % n, weight=1)

        # Disable the initial empty tile
        if i == empty:
            button.config(state=tk.DISABLED)

        bcontent.append(button)

    root.mainloop()


# Use name-main-pattern to start the program
if __name__ == "__main__":
    create_layout("ABCDEFGHIJKLMNO")

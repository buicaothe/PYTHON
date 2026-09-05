# LAB6B - MODULE 3:
# 1. pvmemo.py_____________________
from pathlib import Path
import tkinter as tk
from tkinter import filedialog as fd
# 2. Import read_write.py file:
import read_write

# 3. Define function close:


def close(window, s):
    '''before closing the window save the text'''
    options = {}
    options['defaultextension'] = '.txt'
    options['filetypes'] = [('text files', '.txt'), ('all files', '.*')]
    # Use .home() safely; adding / "Desktop" is fine if it exists
    options['initialdir'] = Path.home() / "Desktop"
    options['initialfile'] = ''
    options['parent'] = window

    # Note: tk.Text.get() usually adds a newline, so len > 1 is a good check
    if len(s.strip()) > 0:
        filename = fd.asksaveasfilename(title='Save the file', **options)
        if filename:
            read_write.write(s, filename)
    window.destroy()

# 4. Define function open:


def open_file(window):  # Renamed to open_file to avoid shadowing Python's built-in open()
    options = {}
    options['defaultextension'] = '.txt'
    options['filetypes'] = [('text files', '.txt'), ('all files', '.*')]
    options['initialdir'] = Path.home() / "Desktop"
    options['initialfile'] = ''
    options['parent'] = window

    filename = fd.askopenfilename(title='Open file', **options)
    if filename:
        return read_write.read(filename)
    return ""  # Return empty string if user cancels

# 5. Define main()-function:


def main():
    # 6. inside the main function:
    window = tk.Tk()
    window.geometry('400x200')
    window.title('Memo')

    # Define textarea (tk.Text)
    content = tk.Text(window)
    content.grid(row=0, column=0, sticky="nsew")

    # Closing protocol (Using lambda to pass current text)
    window.protocol('WM_DELETE_WINDOW', lambda: close(
        window, content.get("1.0", tk.END)))

    # Define scrollbar (tk.Scrollbar):
    sbar = tk.Scrollbar(window)
    sbar.grid(row=0, column=1, sticky="ns")

    # Bind scrollbar to the content
    sbar.config(command=content.yview)
    content.config(yscrollcommand=sbar.set)

    # Fill the whole window with textarea:
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    # Load initial content
    initial_text = open_file(window)
    content.insert('1.0', initial_text)

    # Start listening the events in the window’s main loop:
    window.mainloop()


if __name__ == '__main__':
    main()

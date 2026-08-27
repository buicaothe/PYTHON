'''hello world with input as tkinter progam'''
from tkinter import Tk, Frame, Label, Button, Entry, messagebox
# create a program window
window = Tk()
window.title('Hello')

# create a Frame for lable and entry
frame = Frame(window)
Label(frame, text='What is your name?',padx=10, pady=10).pack(side='left')
entry = Entry(frame)
entry.pack(side='right')

# show frame and button
frame.pack(side='top')
Button(window, text='Press me',
       command=lambda : [messagebox.showinfo('Hello',
            f'Nice to see you, {entry.get()}.'), entry.delete(0,'end')]).\
            pack(side='bottom')
# start the event loop
window.mainloop()
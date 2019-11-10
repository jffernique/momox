from tkinter import *

root = Tk()

def command():
    Toplevel(root)

button = Button(root, text="New Window", command=command)
button.pack()

root.mainloop()
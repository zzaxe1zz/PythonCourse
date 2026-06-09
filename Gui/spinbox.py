from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x300")

w = Spinbox(root, values=('Python', 'C++', 'Java')).pack()

e = Spinbox(root, values=('Axel', 'Diana', 'David')).pack()


root.mainloop()

from tkinter import *

root = Tk()

frame = Frame(root, width=500, height=300)
frame.pack()

entrada = Entry(frame)
entrada.grid(row=0, column=1)
entrada.config(justify='center', state="normal")


entrada2 = Entry(frame)
entrada2.grid(row=1, column=1, padx=5, pady=5)
entrada2.config(show='*')

label1 = Label(frame, text='Nombre')
label1.grid(row=0, column=0, sticky='w', padx=5, pady=5)

label2 = Label(frame, text='Password')
label2.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()

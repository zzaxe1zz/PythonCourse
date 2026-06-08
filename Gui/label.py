from tkinter import *

root = Tk()


# texto_nuevo = StringVar()
# texto_nuevo.set('Python')

# imagen = PhotoImage(file=".gif")
# abelImg = Label(root, image=imagen)
# label.pack()

root.title('Bienvenidos')
root.iconbitmap("atomic_121940.ico")
root.config(width=400, height=300)

Label1 = Label(root, text='Una gui')
Label1.place(x=100, y=50)

Label2 = Label(root, text='xDDDD')
Label2.place(x=200, y=60)

Label1.config(bg="red", fg="white", font=("Arial", 20))
Label2.config(bg="blue")

root.mainloop()

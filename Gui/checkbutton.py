from tkinter import *


def Eleccion():
    elegir = ""

    if pizza.get() == 1:
        elegir += "Has elegido pizza\n"
    if pollo.get() == 1:
        elegir += "Has elegido pollo\n"
    if hambrgs.get() == 1:
        elegir += "Has elegido hamburgesa\n"
    if (pizza.get() and pollo.get() and hambrgs.get()) == 1:
        elegir += """
        Tu orden final es: [Pizza, Hamburgesa y Pollo]"""

    imprimir.config(text=elegir)


root = Tk()
root.geometry("400x300")

frame = Frame(root)
frame.pack()

pizza = IntVar()
pollo = IntVar()
hambrgs = IntVar()

# fotoPizza = PhotoImage(file="Pepperoni.png")

# Label(root, image=fotoPizza).pack()


Checkbutton(frame, text='Pizza', variable=pizza,
            onvalue=1, offvalue=0, command=Eleccion).pack(side="right")
Checkbutton(frame, text='Hamburgesa',  variable=hambrgs,
            onvalue=1, offvalue=0, command=Eleccion).pack(side="right")
Checkbutton(frame, text='Pollo',  variable=pollo,
            onvalue=1, offvalue=0, command=Eleccion).pack(side="right")

imprimir = Label(root)
imprimir.pack()

root.mainloop()

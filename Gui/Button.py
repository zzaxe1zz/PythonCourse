from tkinter import *


def Sumar():
    resultado.set(int(var1.get())+int(var2.get()))


def Restar():
    resultado.set(int(var1.get())-int(var2.get()))


root = Tk()

frame = Frame(root, width=500, height=300)
frame.pack()


var1 = StringVar()
var2 = StringVar()
resultado = StringVar()


entrada1 = Entry(frame)
entrada1.pack()
entrada1.config(bd=10, font="Currier, 20", textvariable=var1)

entrada2 = Entry(frame)
entrada2.pack()
entrada2.config(bd=10, font="Currier, 20", textvariable=var2)


entrada3 = Entry(frame)
entrada3.pack()
entrada3.config(bd=10, font="Currier, 20",
                state="disabled", textvariable=resultado)


boton1 = Button(frame, text='Sumar')
boton1.pack()
boton1.config(bd=5, font="Currier, 10", command=Sumar)

boton2 = Button(frame, text='Restar', command=Restar)
boton2.pack()
boton2.config(bd=5, font="Currier, 10")

root.mainloop()

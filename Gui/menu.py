from tkinter import *
from tkinter import messagebox


def Salir():
    i = messagebox.askquestion("Salir", "Estas seguro?")
    if i == "yes":
        root.destroy()


def AcercaDe():
    messagebox.showinfo("Hola", "Creado por Axel")


def Licencia():
    messagebox.showwarning("Hola", "No hay")


def Error():
    messagebox.showerror("Error", "Error fatal")


def Deshacer():
    messagebox.askquestion("Esta seguro?", "Deshacer todo?")


root = Tk()
root.geometry("400x300")

barraMenu = Menu(root)
root.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo")
archivoMenu.add_command(label="Nueva Ventana", command=Error)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=Salir)


archivoEditar = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Editar", menu=archivoEditar)
archivoEditar.add_command(label="Deshcaer", command=Deshacer)
archivoEditar.add_command(label="Reacer")


archivoAyuda = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label="Acerca de...", command=AcercaDe)
archivoAyuda.add_command(label="Licencia", command=Licencia)

root.mainloop()

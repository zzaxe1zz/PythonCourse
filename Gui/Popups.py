from tkinter import *
from tkinter import filedialog

root = Tk()


def Abrir():
    archivo = filedialog.askopenfilename(title="Abrir",
                                         filetypes=(("Documento de texto", "*.txt"), ("Archivo pdf", "*.pdf")))
    print(archivo)


Button(root, text="Archivos", command=Abrir).pack()


root.mainloop()

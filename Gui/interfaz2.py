from tkinter import *

root = Tk()

root.title('Una GUI')  # Nombre de la ventana

root.resizable(1, 1)  # Tamaño de la ventana True True

root.iconbitmap("atomic_121940.ico")  # icono de la ventana

# Configuracion de tamaño de ventana
miFrame = Frame(root)
# miFrame.pack(side=RIGHT, anchor='n') # muestra el frame en esa  pos
miFrame.pack(fill="y", expand=1)  # expander en el eje
miFrame.config(width=400, height=300)
# Cursores
# miFrame.config(cursor="Boat")
miFrame.config(cursor="pirate")
# Estilos
miFrame.config(bg="red")
miFrame.config(bd="20")
miFrame.config(relief="ridge")


# Raiz de ventana
root.config(cursor="Boat")
# Estilos
root.config(bg="blue")
root.config(bd="20")
root.config(relief="groove")

root.mainloop()  # Evita que se cierre la ventana

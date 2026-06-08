from io import open

fichero = open('archivo.txt', 'a')
fichero.write('\nEste es el metodo append')
fichero.close()

print(fichero)

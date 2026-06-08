from io import open

fichero = open('archivo.txt', 'r')
texto = fichero.read()
linea = fichero.readlines()
fichero.close()
print(texto)
print(linea)

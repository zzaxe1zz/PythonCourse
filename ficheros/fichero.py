from io import open

fichero = open('archivo.txt', 'w')
texto = 'Hola mundo\nEstoy estudiando Python'
fichero.write(texto)

fichero.close()

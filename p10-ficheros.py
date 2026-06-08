# Cree un fichero y ábralo en modo escritura, luego asigne un texto a una variable e insértelo en el fichero.
# Por último, visualice el documento.txt si fue escrito correctamente.
from io import open
import pickle

fichero = open('practica10.txt', 'w')
texto = 'Test de archivo\nEstoy estudiando Python'
fichero.write(texto)

fichero.close()
# 1. Serialice un diccionario utilizando el método dump. El archivo una vez serializado
# debe mostrarnos un mensaje que nos diga que no se puede abrir.

personas = {'Axel': 'Gomez', 'Diana': 'Vazquez'}
ficheroDic = open('personas', 'wb')
pickle.dump(personas, ficheroDic)
ficheroDic.close()
del (ficheroDic)

ficheroRead = open('personas', 'rb')
miPersona = pickle.load(ficheroRead)
ficheroRead.close()


for clave, valor in personas.items():
    print(clave, valor)

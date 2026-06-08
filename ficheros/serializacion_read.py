import pickle

fichero = open('lista', 'rb')
lista = pickle.load(fichero)
fichero.close()
print(lista)
print(lista[1])

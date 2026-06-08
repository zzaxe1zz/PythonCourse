import pickle

lista = ['Axel', 'Diana', 'David']

fichero = open('lista', 'wb')  # Codigo binario

pickle.dump(lista, fichero)

fichero.close()

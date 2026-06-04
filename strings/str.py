# **************** Conjuntos *****************************
i = set()
i.add(1)
i.add(2)
i.add(3)

i.discard(3)
print(i)

a = set()
a = {1, 2, 3, 4}
b = a.copy()
b.discard(2)
print(a, b)
# **************** Diccionarios *****************************
personas = {'Axel': 'Gomez', 'Diana': 'Vazquez'}
print(personas.get('Axel'))

print(personas.keys())  # nombre
print(personas.values())  # apellido
print(personas.items())  # nombre y apellido

for clave, valor in personas.items():
    print(clave, valor)


personas.pop('Diana')
print(personas)
# **************** Arrays *****************************

lista = [1, 1, 2, 3, 4, 5, 6]
lista2 = [8, 9, 10]
lista.append(7)  # agrega al final
print(lista)

lista.extend(lista2)  # agrega al final la segunda lista
print(lista)

print(lista.count(1))  # cuenta cuantos elementos hay (#)
lista.index(1)  # indica la posicion del elemento
print(lista)


lista.insert(0, 0)  # Inserta (indice, elemento)
print(lista)

print(len(lista))  # cuantos elementos hay en total

lista.remove(0)  # elimina el elemento del indice
print(lista)


lista.reverse()
print(lista)

print(lista.sort())

lista.clear()
print(lista)


# **************** Strings ****************************

i = '123'
print(i.isdigit())

# Cambia a mayusculas con .upper()
nombre = input('Ingrese su nombre: ')
print('El nombre del usuario es :', nombre.upper())

# Cambia a minusculas con .lower()
nombre = input('Ingrese su nombre: ')
print('El nombre del usuario es :', nombre.lower())

# Cambia a la primera mayuscula con .capitaliza()
nombre = input('Ingrese su nombre: ')
print('El nombre del usuario es :', nombre.capitalize())

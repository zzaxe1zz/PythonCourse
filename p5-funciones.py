# Funciones indeterminadas

def sumar(*args):
    for i in args:
        print(i)


sumar('Python', True, 10, 'a', 5.6)

# 1. Escriba una función que muestre por consola un saludo personalizado. Por ejemplo ‘¡Hola mundo!’


def Saludo():
    print('Hola a todos')


Saludo()
# 1. Escriba una función que reciba un nombre por parámetro y que luego muestre en pantalla ¡Hola <nombre>!


def SaludoUsuario(nombre):
    return print(f'Hola {nombre}')


SaludoUsuario('Axel')

# 1. Cree una función que le pida el usuario su nombre y su edad, luego muestre en pantalla los resultados.


def Usuario(nombre, edad):
    print(f'El usuario es: {nombre} con {edad} años')


nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
Usuario(nombre, edad)
# 1. Definir una función que reciba dos números por parámetros y que luego los sume.


def Suma(a, b):
    resultado = a+b
    return print(f'El resultado de {a} + {b} es: {resultado}')


a = float(input('Numero:'))
b = float(input('Numero:'))
Suma(a, b)

# 1. Escriba un programa que almacene la cadena de caracteres contraseña en una variable,
# para luego preguntarle al usuario por la contraseña. Luego, imprima en la consola si
# la contraseña que el usuario ingreso coincide con la guardada en variable.
contraseña = "axel123"
intento = input('Ingrese la contraseña: ')
if intento == contraseña:
    print('Contraseña correcta!')
else:
    print('Incorrecto')
# 1. Realice un programa que le pida al usuario dos números y muestre por consola su división.
# Si el divisor es cero el programa debe mostrar un error.
num1 = float(input('Ingrese un numero: '))
num2 = float(input('Ingrese un segundo numero: '))
if num2 > 0:
    division = num1 / num2
    print(division)
else:
    print('Error')
# 1. Escriba un programa que le pida al usuario por teclado un numero entero y
# muestre en consola si es par o impar.
num1 = int(input('Ingrese un numero: '))
resultado = num1 % 2
if resultado == 0:
    print('Par')
else:
    print('Inpar')
# 1. Escriba un programa donde se evalué el ingreso a menores de edad,
# si la persona tiene menos de 19 años el programa le debe mostrar en pantalla que
# ¡No puede ingresar!, de caso contrario que le diga ¡Bienvenido!
edad = int(input('Ingrese su edad: '))
if edad > 19:
    print('Bienvenido')
else:
    print('No puede ingresar')

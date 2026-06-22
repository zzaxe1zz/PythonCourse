# 1. Escriba un programa que lea dos números por teclado y determine con un valor booleano de True o False estos ejemplos:
# • Si los dos números son iguales
num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un segundo numero: '))
comprobacionIg = num1 == num2
print(comprobacionIg)
# • Si los dos números son diferentes
comprobacionDif = num1 != num2
print(comprobacionDif)
# • Si el primero es mayor que el segundo
comprobacionMay = num1 > num2
print(comprobacionMay)
# • Si el segundo es mayor o igual que el primero
comprobacionMayIg = num1 >= num2
print(comprobacionMayIg)

# Conociendo los operadores lógicos, realice una comprobación
# si una cadena de texto ingresada desde teclado por le usuario tiene
# la longitud mayor o igual que 4 y a su vez que 7 (determinar con un valor booleano True o False)

string = input('Ingrese un texto: ')
print(len(string) >= 4 and len(string) >= 7)

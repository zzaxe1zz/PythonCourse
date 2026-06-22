# 1. Escriba un programa que almacene en una Lista los cursos que has cursado o los que te
# gustaría cursar en Udemy. Luego muestre la lista por consola.
cursos = ['Python', 'Cyberseguridad', 'Machine learning']
print(cursos)
# 1. Escriba un programa que almacene personas en una lista, luego que le muestre por
# pantalla el mensaje de ‘Su nombre es ‘nombre’
personas = ['Axel', 'Diana', 'Samantha', 'David']
for i in range(len(personas)):
    print(f'su nombre es {personas[i]}')
# 1. Escribir un programa que guarde en una variable un diccionario con los siguientes
# valores {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y
# muestre en consola el símbolo o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
print(divisas)
entrada = input('Que divisa va a seleccionar?:')
if entrada.title() in divisas:
    print(divisas[entrada.title()])
else:
    print("La divisa no está.")

# 1. En una tupla coloque los siguientes valores: números enteros, decimales, String,
# colecciones. Luego muestre en consola.
tupla = (1, 2.5, 'Hola', [1, 5, 4])
print(tupla)

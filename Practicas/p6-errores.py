# 1. Encuentra el error en la siguiente línea de código.
# Luego tendrás que crear una excepción para evitar que el
# programa se caiga. Además, debes explicarle al usuario que fue lo que sucedió y darle la solución.
try:
    valor = 10/0
except ZeroDivisionError:
    print('No se puede dividir entre 0')
# 1. Encuentra el error en la siguiente línea de código.
# Luego tendrás que crear una excepción para evitar que
# el programa se caiga. Además, debes explicarle al usuario que fue lo que sucedió y darle la solución.
try:
    miLista = [1, 2, 3, 4, 5]
    miLista[7]
except IndexError:
    print('El inice que busca esta fuera de rango')

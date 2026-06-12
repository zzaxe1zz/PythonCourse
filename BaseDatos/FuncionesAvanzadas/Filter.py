edades = [11, 12, 25, 44, 16, 20, 66, 18, 79]


def mayores(edad):
    return edad >= 18


entrar = list(filter(mayores, edades))
print(entrar)
print(entrar[0])

def GenerarPares(limite):
    num = 1
    miLista = []
    while num < limite:
        miLista.append(num*2)
        num = num+1
    return miLista


print(GenerarPares(10))


# Version con Generadores
def GenerarPares(limite):
    num = 1
    miLista = []
    while num < limite:
        yield num*2
        num = num+1


devuelvePares = GenerarPares(10)
print(next(devuelvePares))


# Generadores II

def DevuelvePaises(*paises):
    for elemneto in paises:
        yield elemneto
    # for Subelemneto in paises: retorna Letra por letra
    #     yield Subelemneto


paisesDevuelta = DevuelvePaises('Mexico', 'Alemania', 'Brasil', 'Francia')
print(next(paisesDevuelta))
# print(next(paisesDevuelta))
# print(next(paisesDevuelta))
# print(next(paisesDevuelta))

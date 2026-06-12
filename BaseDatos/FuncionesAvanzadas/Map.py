def Doblar(numero):
    return numero*2


numeros = [2, 4, 10, 23, 50, 33]
# i = map(Doblar, numeros)
# print(list(i))
i = map(lambda x: x*2, numeros)
print(list(i))


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
i = map(lambda x, y: x*y, a, b)
print(list(i))

try:
    c = int(input('Ingrese un valor: '))
    c/0
except ValueError:
    print('Ingreso un texto no un numero')
except Exception as c:
    print(type(c).__name__)

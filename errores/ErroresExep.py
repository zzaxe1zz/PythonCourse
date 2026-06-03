def restar(num1,num2):
    return num1 - num2

def sumar(num1,num2):
    return num1 + num2

def multiplicar(num1,num2):
    return num1 * num2

def dividir(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print('Error no se puede dividir entre 0' )
        return 'Operacion no valida'
    

op1 = int(input('Introduce el primer valor: '))
op2 = int(input('Introduce el segundo valor: '))

operacion = input('Introduce la operacion a realizar ---> \nSumar\nRestar\nDividir\nMultiplicar: ')

if operacion == 'Sumar':
    print(sumar(op1,op2))
elif operacion == 'Restar':
    print(restar(op1,op2))

elif operacion == 'Multiplicar':
    print(multiplicar(op1,op2))

elif operacion == 'Dividir':
    print(dividir(op1,op2))

else:
    print('ERROR OPCION NO VALIDA')



print('Ejecutando nueva linea de codigo')
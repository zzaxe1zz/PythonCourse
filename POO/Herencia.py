class Persona:
    def __init__(self, nombre, apellido, edad, sexo):
        self. nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def datosPersonales(self):
        print(f'El nombre de la persona es: {self.nombre}')
        print(f'El apellido de la persona es: {self.apellido}')
        print(f'La edad de la persona es: {self.edad}')
        print(f'EL sexo de la persona es: {self.sexo}')


miPersona = Persona('Axel', 'Gomez', 21, 'Masculino')
miPersona.datosPersonales()
print()


class Empleado(Persona):  # Esta clase hereda de Persona
    def datosEmpleado(self, vacaciones, salario):
        print(f'Los dias de vacaciones son: {vacaciones}')
        print(f'El salario es de: {salario}')


miEmpleado = Empleado('Esmeralda', 'Gomez', 18, 'Femenino')
miEmpleado.datosPersonales()
print()
miEmpleado .datosEmpleado(15, 2500)
print()


# Herencia multiple *****************
class Clase1:
    def metodo1(self):
        print("Metodo de clase 1")


class Clase2:
    def metodo2(self):
        print("Metodo de clase 2")


class Clase3(Clase1, Clase2):
    def metodo3(self):
        print("Metodo de clase 3")


c = Clase3()
c.metodo1()
c.metodo2()
c.metodo3()

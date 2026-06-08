class Persona:
    def __init__(self, __nombre, edad, sexo):
        self.nombre = __nombre
        self.edad = edad
        self.sexo = sexo

    def datosPersonales(self):
        print(f'El nombre de la persona es: {self.nombre}')
        print(f'La edad de la persona es: {self.edad}')
        print(f'El sexo de la persona es: {self.sexo}')

import pickle


class Persona:
    def __init__(self, nombre, edad, sexo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad

    def datosPersonales(self):
        print(f'El nombre de la persona es {self.nombre}')
        print(f'La edad de la persona es {self.edad}')
        print(f'El sexo de la persona es {self.sexo}')
        print(f'La nacionalidad de la persona es {self.nacionalidad}')


persona1 = Persona('Axel', 21, 'Masculino', 'Mexicano')
persona2 = Persona('David', 20, 'Masculino', 'Mexicano')
persona3 = Persona('Diana', 21, 'Femeneino', 'Mexicana')


listaPersonas = [persona1, persona2, persona3]
fichero = open('Personas', 'wb')
pickle.dump(listaPersonas, fichero)
fichero.close()
del (fichero)


ficheroRead = open('Personas', 'rb')
miPersona = pickle.load(ficheroRead)
ficheroRead.close()

for i in miPersona:
    print(i.datosPersonales())
    print()

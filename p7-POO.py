# 1. Cree una clase Persona con sus atributos correspondientes:
# nombre, edad, sexo, nacionalidad. Luego cree una instancia de la clase Persona.
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
persona1.datosPersonales()

# 1. Cree una clase Auto con sus atributos correspondientes:
# marca, modelo, año, color. Defina también un método, donde luego al
# instanciar la clase nos diga si el auto esta encendido o apagado.


class Auto:
    def __init__(self, marca, kilometros, año):
        self.__marca = marca
        self.kilometros = kilometros
        self.__año = año

    def estado(self, encendido):
        encendido = True
        self.estado = encendido
        if (self.estado == True):
            return print(f'El auto esta encendido')
        else:
            return print('El auto esta apagado')

    def __str__(self):
        return 'El vehiculo es un {}, tiene {} km, del año {}'.format(self.__marca, self.kilometros, self.__año)


miAuto = Auto('Dodge', 0, 2026)
print(str(miAuto))
miAuto.estado(True)

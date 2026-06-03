class Gelatina:
    def __init__(self, sabor, color, tamaño):
        self.sabor = sabor
        self.color = color
        self.tamaño = tamaño

    def imprimir(self):
        print(f'La gelatina es de {self.sabor}')
        print(f'La gelatina se ve de {self.color}')
        print(f'La gelatina es de tamaño {self.tamaño}')


gelatina1 = Gelatina('Limon', 'Verde', 'Grande')
gelatina1.imprimir()

print()
gelatina2 = Gelatina('Naranja', 'Anaranjado', 'Mediano')
gelatina2.imprimir()


class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def datosPersonales(self):
        print(f'El nombre de la persona es {self.nombre}')
        print(f'La edad de la persona es {self.edad}')
        print(f'El sexo de la persona es {self.sexo}')


persona1 = Persona('Axel', 21, 'Masculino')
persona2 = Persona('Diana', 20, 'Femenino')

persona1.datosPersonales()
print()
persona2.datosPersonales()
print()


class Vehiculo:
    def __init__(self, marca, kilometros, año):
        self.__marca = marca  # __ se usa doble ""_"_" para hacerlo privado
        self.kilometros = kilometros
        self.año = año
        print(
            f'Se ha adquirido el vehiculo {self.__marca} con {self.kilometros} kilometros')

    def __del__(self):
        print(f'Se ha vendido el vehiculo {self.__marca}')

    def __str__(self):
        return 'El vehiculo es un {}, tiene {}, del año {}'.format(self.__marca, self.kilometros, self.año)


miCarro = Vehiculo('Dodge', 0, 2026)
print(str(miCarro))
del (miCarro)

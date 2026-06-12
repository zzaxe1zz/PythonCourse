# 1. Cree una base de datos que se llame Personas. Luego introduzca
# al menos diez personas en esa base de datos.

# 2. Cree una base de datos personas con los siguientes
# requerimientos: nombre, edad, sexo y DNI. El DNI debe ser una
# clave primaria, por lo cual no se puede repetir.
import sqlite3

conexion = sqlite3.connect('Personas')
cursor = conexion.cursor()

cursor.execute(
    'CREATE TABLE PERSONAS (Nombre VARCHAR(50), Edad INTEGER, Sexo VARCHAR(10), DNI INTEGER PRIMARY KEY)')
cursor.execute('INSERT INTO PERSONAS VALUES("Axel",21,"Masculino", 1)')
cursor.execute('INSERT INTO PERSONAS VALUES("David",21,"Masculino", 2)')
cursor.execute('INSERT INTO PERSONAS VALUES("Erik",21,"Masculino", 3)')

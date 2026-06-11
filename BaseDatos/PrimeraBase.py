import sqlite3

conexion = sqlite3.connect('BaseCurso.db')
cursor = conexion.cursor()
# cursor.execute(
#     'CREATE TABLE USUARIOS(NOMBRE VARCHAR(50), EDAD INTEGER, SEXO VARCHAR(50))')


# cursor.execute("INSERT INTO USUARIOS VALUES('Axel', 25, 'Masculino')")

# cursor.execute('SELECT * FROM USUARIOS')
# usuarios = cursor.fetchone()
# print(usuarios)
# usuarios = [
#     ('Diana', 21, 'Femenino'),
#     ('David', 20, 'Masculino')
# ]
# cursor.executemany('INSERT INTO USUARIOS VALUES(?,?,?)', usuarios)

cursor.execute('SELECT * FROM USUARIOS')
usuarios = cursor.fetchall()
print(usuarios)

conexion.commit()
conexion.close()

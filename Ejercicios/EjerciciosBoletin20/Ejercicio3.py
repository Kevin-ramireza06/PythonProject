# 3. Haz un programa que pida por teclado el nombre, el peso y la altura e introduzca un nuevo
# pokemon en la pokedex. El código debería de ser consecutivo al último que haya en la base de
# datos.
# NOTA: No te fies de que el último registro sea el que tiene un mayor número en la pokedex. Eso
# es así en este caso por la forma en que se ha creado la tabla, pero u ordenas la salida desde la
# instrucción select o te aseguras de cual es el mayor cuando recuperes los datos!

import mysql.connector

try:
    conexion = mysql.connector.connect(
        user="root",
        password="root",
        host="localhost",
        database="pokemondb"
    )

    cursor = conexion.cursor()

    nombre = input("Porfavor ingresa uel nombre ")
    peso = input("Porfavor ingresa el peso ")
    altura = input("Porfavor ingresa el altura ")

    sql = "INSERT INTO Pokemon (nombre,peso,altura) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, peso, altura))
    conexion.commit()

    cursor.execute("Select * from Pokemon where nombre = %s", (nombre,))
    elemento = cursor.fetchone()
    print(elemento)


except mysql.connector.Error as e:
    print(e)

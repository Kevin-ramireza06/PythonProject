# 4. Haz un programa que pida un código y elimine el pokemon con dicho código.
# NOTA: Pruébalo con un código introducido por ti en el ejercicio anterior y así evitarás
# problemas de integridad debido a las foreign keys.

import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="pokemondb"
    )

    idEliminar = input("Ingresa el ID del pokemon que quieres eliminar: ")
    cursor = conexion.cursor()

    sql = "Delete from pokemon where numero_pokedex = %s"
    cursor.execute(sql, (idEliminar,))
    conexion.commit()

    lista = cursor.execute("Select * from pokemon where numero_pokedex = %s",(idEliminar,))

    print(lista)

    cursor.close()
    conexion.close()

except mysql.connector.Error as error:
    print(error)
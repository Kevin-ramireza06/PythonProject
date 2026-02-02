# 1. Haz un programa que liste por consola los nombres (sólo los nombres) de todos los
# pokemons de mas de 1.5 de altura

import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="pokemondb"
    )
    cursor = conexion.cursor()
    cursor.execute("Select nombre from Pokemon where altura > 1.5")

    for fila in cursor:
        print(fila[0])

    cursor.close()
    conexion.close()

except mysql.connector.Error as err: #ESte es el manejo de excepciones oficial,
    print(err)

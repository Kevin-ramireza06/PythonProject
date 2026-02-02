# 2. Haz un programa que cambie a mayúsculas (por ejemplo SNORLAX en lugar de Snorlax) los
# nombres de todos los pokemon de mas de 200 de peso. Informa por pantalla el número de
# registros modificados

import mysql.connector
try:
    conexion = mysql.connector.connect(
        user='root',
        password="root",
        host="localhost",
        database="pokemondb"
    )
    cursor = conexion.cursor()
    cursor.execute("Select nombre from Pokemon where peso > 200")
    for fila in cursor:
        textoMayusculas = fila[0]
        print(textoMayusculas.upper())

    print("-------------------------------")
    print("La cantidad de filas afectadas fue", cursor.rowcount)

    cursor.close()
    conexion.close()
except mysql.connector.Error as e:
    print(e)


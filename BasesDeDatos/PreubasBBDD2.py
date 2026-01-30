import mysql.connector

try:
    connexion = mysql.connector.connect(
        user="dam2" ,
        password="asdf.1234",
        host="localhost" ,
        database="adat7"
    )
    cursor = connexion.cursor()
    id = 3501
    sql1 = f"select PLayListId,TrackId from PlaylistTrack where TrackId = {id}"
    #cursor.execute(sql1)
    # #Tambien funcionan los fString
    #
    # tupla = cursor.fetchall()
    # if len(tupla) == 0:
    #     print("El select no devuelve datos")
    # else:
    #     print(tupla)

    sql2 = f"Delete from PlaylistTrack where TrackId = {id}"
    cursor.execute(sql1)

    resultado = cursor.fetchall()
    print(resultado)

    print(cursor.execute(sql2))
    #Cuando hacemos un delete, el cursor ejecute no devuelve nada si borra o no
    cursor.execute(sql1)
    resultado = cursor.fetchall()
    print(resultado)

    connexion.commit()
    #EN python para persistir en BBDD Es obligatorio hacer el commit

    cursor.close()
    connexion.close()
except mysql.connector.Error as err: #Este es el manejo de excepciones oficial,
    print(err)
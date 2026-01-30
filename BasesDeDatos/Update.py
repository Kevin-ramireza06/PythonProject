import mysql.connector

try:
    connexion = mysql.connector.connect(
        user="dam2" ,
        password="asdf.1234",
        host="localhost" ,
        database="adat7"
    )
    cursor = connexion.cursor()
    id = 341
    sql1 = f"Select * from Album where AlbumId = {id}"
    sql2 = f"Update Album set Title = 'Los Pajaritos' where AlbumId = {id}"
    #Para hacer un Update y vamos a poner Strings debemos de jugar con las comillas simples o usar los caracteres de escape

    cursor.execute(sql1)
    resultado = cursor.fetchall()
    print(resultado)

    print(cursor.execute(sql2))
    cursor.execute(sql1)
    resultado = cursor.fetchall()
    print(resultado)

    connexion.commit()

    cursor.close()
    connexion.close()
except mysql.connector.Error as err: #Este es el manejo de excepciones oficial,
    print(err)
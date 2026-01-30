# #import mysql.connector
#
# try:
#     connexion = mysql.connector.connect(user="dam2" , password="asdf.1234", host="localhost" , database="adat7")
#     #ASi abrimos la conexion
#     cursor = connexion.cursor()
#     #y ya con esta variabele ay podemos manipular la base de datos
#
#     cursor.execute("Select * from Album")
#     #Asi ejecutamos una query, una de las formas de recogerla es como tuplas
#     for fila in cursor:
#         print(fila)
#
#     cursor.close()
#     connexion.close()
# except mysql.connector.Error as err: #ESte es el manejo de excepciones oficial,
#     print(err)

# Mano acordate instalarte el conector en casa para quee furule JSJSJSJJSJSJJSJSSJJSJSJSJ

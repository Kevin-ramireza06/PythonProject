"""
Para la entrada por teclado se una la funcion input, y guarda el valor en la variable que lo usemos
"""

nombre = input("Ingresa tu nombre: ") #Ponemos de argumento lo que queremos que sea el mensaje
edad = int( input("Ingresa tu edad: ") )

#La funcion int/float() nos permite cabiar el tipo de valor de un texto, siempre y cuando se pueda, si no, salta error

print("Hola ", nombre,"Tu edad es:",edad)

print("Te faltan", 67 - edad , "Para jubilarte")

"""
Esta fuuncion guarda los datos como una cadena de caracteres, para usarlas como otros valores tendriamos que setearlos
"""
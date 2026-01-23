# #Crea una función en python que se llame compararFicheros y que reciba como argumento el
# #nombre de dos ficheros de texto. La función debería de devolver un valor booleano indicando
# si el contenido de ambos ficheros es exactamente el mismo o no.

def compararFicheros(nommbre1, nombre2):
    try :
        with open(nommbre1, "r") as fichero1 :
            with open(nombre2, "r") as fichero2 :

                contenidoFichero1 = fichero1.read()
                contenidoFichero2 = fichero2.read()

                if contenidoFichero1 == contenidoFichero2:
                    return True
                else:
                    return False
    except :
        print("Error con los ficheros")
        return False

print(compararFicheros("Ejercicio1Prueba1" , "Ejercicio1Prueba2"))



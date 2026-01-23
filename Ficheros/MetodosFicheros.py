try:
    # fichero = open("quijote.txt","r")
    # #fichero.seek(10,2)
    # print("Posicion:" , fichero.tell())
    # #El .tell nos devuelve en donde esta el cursor, en que posicion del fichero
    # print(fichero.readline())
    # print("Posicion" , fichero.tell())
    # fichero.seek(0)
    # #el .seek nos permite mover el cursor, el imer parametro indicamos cuanto lo vamos a mover, y el segundo son posiciones
    # #constantes, el 0 es el inicio, el 1 la posicion actual y el 2 la ultima posicion
    #
    # #Al poner los 2 parametros con el primero indicamos que tanto se mueve, y el segundo desde donde, teniendo en cuenta
    # #lo anterior mencionado, si es 0 ps se queda donde esta, ESTE SOLO FUNCIONA EN BINARIOS
    # fichero.close()

    fichero = open("quijote.txt", "r+")
    #El a+ nos permite leer y escribir en el fichero, y reposicionar con el seek
    #AL poner el modo a este va a poner el puntero al final
    #Con r+ posiciona el cursor al principio y si escribimos borra la linea en la que esta y laa sobreescribe
    #con w borra el fichero para volverlo a escribir
    fichero.write("Nueva Linea al final")
    print(fichero.tell())

    fichero.seek(8)
    print(fichero.read())
    fichero.close()

except :
    print("Error en el fichero")
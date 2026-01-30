try:
    with open("quijote.txt", "wt") as fichero:
        #DE esta froma hacemos que el fichero se abra, y se encarga de cerrar el fichero al acabar su bloque de codigo
        fichero.write("Esto se escribio desde la prueba del autocerrado del fichero\n")
        fichero.write("Oli")
except :
    print("El fichero no existe")
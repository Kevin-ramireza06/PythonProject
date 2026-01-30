try:
    fichero = open("quijote.txt", "wt")
    # De este modo nos permite escribir en el fichero, pero con este permiso, borra y empieza a escribir lo que pongamos
    # Y si estamos en modo escritura, si el fichero no existe, se crea

    ficeroAgregar = open("quijote.txt", "at")
    #Con el "a" se escribe al final del fichero


    fichero.write("Texto agregado")
    fichero.write("Texto agregado 2\n")
    #EL por deecto al escribir no pone el salto de linea asi que hay que ponerlo nosotros
    fichero.write("Texto agregado 3\n")

    lista = ["Sisas", "NOnas", "Hola"]
    fichero.writelines(lista)

    ficeroAgregar.write("Este texto fue agragado al final indiferente de todo\n")


    fichero.close()
    ficeroAgregar.close()

except :
    print("El fichero no existe")
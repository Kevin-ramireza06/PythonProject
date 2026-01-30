import re

try:
    fichero = open("telefonos.txt","rt")

    regexTelefonoMovil = r"^[6-8][0-9]{8}$"
    regexTelefono = r"^[6-8][0-9]{8}$|^00[0-9]{11}$"

    linea = fichero.readline()
    linea = linea[:-1]

    while linea != "":
        elementos = linea.split("-")
        if re.fullmatch(regexTelefonoMovil, elementos[0]) and re.fullmatch(regexTelefono, elementos[1]) and re.fullmatch("[0-9]+", elementos[2]):
            print(linea)
        linea = fichero.readline()
        linea = linea[:-1]
    fichero.close()
except:
    print("Error al abrir el archivo")
# Tenemos un fichero llamado estadisticas.txt. El formato del fichero es el siguiente (pero el
# contenido puede variar, lógicamente):
# Hombre
# 1.73
# Mujer
# 1.68
# Mujer
# 1.83
# Realiza un programa que lea el contenido de ese fichero y muestre el número de hombres, el
# número de mujeres y la altura media (con dos decimales) de todos sin hacer distinción de
# sexo.
# Por ejemplo, para el fichero del ejemplo anterior, la salida del programa sería esta:
# Hombres: 1.
# Mujeres: 2.
# Estatura media: 1.75
# El formato del fichero se supone correcto y comprobado y nunca va dar problemas

# try:
with open("Ejercicio2Prueba", "r") as fichero:

    hombres = 0
    mujeres = 0
    alturas = 0
    cantidad = 0

    linea = fichero.readline()
    if linea == "Hombre\n":
        hombres += 1
    elif linea == "Mujer\n":
        mujeres += 1
    else:
        alturas += float(linea[:-1])

    while linea != "":
        linea = fichero.readline()
        if linea != "":
            if linea == "Hombre\n":
                hombres += 1
            elif linea == "Mujer\n":
                mujeres += 1
            else:
                alturas += float(linea[:-1])
                cantidad += 1

    print("Cantidad hombres:", hombres)
    print("Cantidad mujeres:", mujeres)
    print("Media Alturas" , round(alturas/cantidad, 2))
# except :
#     print("El fichero no existe")

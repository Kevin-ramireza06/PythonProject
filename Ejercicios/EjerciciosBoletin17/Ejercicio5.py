# 5. En los centros de datos es normal anonimizar de alguna forma los ficheros de clientes para poder
# hacer pruebas con ellos sin vulnerar las leyes de protección de datos. Una de las formas mas
# utilizadas es “barajar” los datos de los clientes originales. Imagina que el fichero de clientes de tu
# empresa es el siguiente:
# Diego Norrea 28222777J
# Inés Perado 07333888X
# Demetrio Imedio 97221345Y
# Roberto Rija 22876345M
# Rubén Tosidad 12987543C
# Armando Adistancia 32879563V
# Germán Tequilla 18000777H
# Cuenta con que la estructura del fichero es siempre correcta y todas las líneas están formadas por
# la misma estructura: nombre, primer apellido y DNI separados por un único espacio en blanco
# Queremos hacer una función que reciba como argumento un nombre de fichero. Tu programa
# debería de leer de un fichero llamado clientes.txt con una estructura como la anterior y escribir en el
# fichero que has recibido como argumento los datos “barajados”. Por ejemplo así:
# Armando Imedio 12987543C
# Imedio Norrea 28222777J
# Roberto Adistancia 97221345Y
# Inés Rija 18000777H
# Diego Perado 22876345M
# Rubén Tequilla 07333888X
# Germán Tosidad 32879563V
# Como puedes observar, lo que hacemos es mezclar de forma aleatoria los nombres, los apellidos y
# los dnis de los clientes a la hora de generar el fichero resultante.

def barajarDatos(nombreFichero):
    import random
    try:
        with open(nombreFichero , "r+") as fichero:
            valoresBarajados = []
            nombres = []
            apellidos = []
            dnis = []

            for linea in fichero:
                linea = linea.strip()
                elementos = linea.split(" ")
                nombres.append(elementos[0])
                apellidos.append(elementos[1])
                dnis.append(elementos[2])

            random.shuffle(nombres)
            random.shuffle(apellidos)
            random.shuffle(dnis)

            for i in range (0, len(nombres)):
                valoresBarajados.append(str(nombres[i] + " " + apellidos[i] + " " + dnis[i]))

            fichero.seek(0)
            for i in valoresBarajados:
                fichero.write(i+"\n")

    except Exception as e:
        print(e)

barajarDatos("Ejercicio5Prueba")

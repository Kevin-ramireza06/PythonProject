#!/usr/bin/python3

#dede python podemos trabajar desde consola de comandos, usando el comadno "python3" y ya con esto podemos
#programar en java desde comandos

#Podemos usar los scipts de python desde comandos, usando el comando "python3 nombreFichero.py" y se ejecuta
#Y para ejecutarlo sin el interprete, solamente le damos permito de ejecucion al fichero,y lo ejecutamos en comandos
#normal(En Linux)

#Debemos de poner esta linea "#!/usr/bin/python3" para que el Sistema Operativo sepa el interprete que tiene que usar
#para ejecutar el archivo

import re

def esconderPin(pin):
    patron = r"^[0-9]{,4}$"
    lista = []
    strPin = str(pin)
    if re.fullmatch(patron, strPin):
        pin = str(pin)
        textoAuxiliar = ""
        for i in pin:
            for j in range(1, 10):
                if j == int(i):
                    textoAuxiliar += "0"
                else:
                    textoAuxiliar += "X"
            if int(i) == 0:
                textoAuxiliar += "0"
            else:
                textoAuxiliar += "X"
            lista.append(textoAuxiliar)
            textoAuxiliar = ""
        tupla = tuple(lista)
        return tupla
    else:
        return lista

pinTupla = esconderPin(6240)

for i in pinTupla:
    print(i)

#-------------------------Correccion-------------------------






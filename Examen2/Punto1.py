from math import isnan
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


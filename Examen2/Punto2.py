import re

def binarios(numeroBin):
    patron = r"^[0-1]{1,}"

    if re.fullmatch(patron, numeroBin):
        numAuxiliar = 0
        return numAuxiliar
    else:
        return -1

print(binarios("1101"))
print(binarios("345"))
print(binarios("hola"))
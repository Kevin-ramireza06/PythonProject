import re

def binarios(numeroBin):
    patron = r"^[0-1]{1,}"

    if re.fullmatch(patron, numeroBin):
        numAuxiliar = 0
        if isinstance(numAuxiliar,int): #Esta funcion permite identificar si una variable es de un tipo de dato concreto
            return numAuxiliar
    else:
        return -1

print(binarios("1101"))
print(binarios("345"))
print(binarios("hola"))

#-------------------Correccion------------

def binarios(numeroBin):
    patron = r"^[0-1]{1,}"

    if re.fullmatch(patron, numeroBin):
        numeroBinLista = list(numeroBin)
        decimal = 0
        for i in range(len(numeroBin)):
            decimal = decimal + int(numeroBinLista[i] * 2 ** (len(numeroBin)-i-1))
    else:
        return -1

def binarios(numeroBin):
    patron = r"^[0-1]{1,}"

    if re.fullmatch(patron, numeroBin):
        decimal = int(numeroBin,2) #int permite poner la base desde la que tiene que transofrmar un binario
        valor = decimal
        return valor
    else:
        return -1
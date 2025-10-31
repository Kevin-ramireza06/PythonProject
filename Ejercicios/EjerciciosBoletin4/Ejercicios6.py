#Escribir un programa que muestre por pantalla los 50 primeros números primos, sus
#raíces cuadradas, sus cuadrados y sus cubos

import math

def sacarDatos(numero) :
    contador = 0


    print("Raiz del numero:", math.sqrt(numero))
    print("Cuadrado del numero:", numero * numero)
    print("Cubo del numero:", numero * numero * numero)

    for i in range(1 , numero+1):
        if numero % i == 0:
            contador += 1
    if contador == 2 :
        print("El numero es primo")
    else:
        print("El numero NOOOOOOO es primo")

for i in range(50) :
    print("El numero:" , i)
    sacarDatos(i)
    print("----------------")
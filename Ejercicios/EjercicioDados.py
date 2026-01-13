
import random

contador = 1
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

print(dado1 , "---", dado2)
while dado1 != dado2 :
    contador += 1
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print(dado1, "---", dado2)

print("se debio tirar el dado" , contador, "Veces")

print("Prueba para subir")

"""
igual = False
contador1 = 0

while igual == False :
    dado3 = random.randint(1, 6)
    dado4 = random.randint(1, 6)

    if dado3 != dado4 :
        contador1 += 1
        dado3 = random.randint(1, 6)
        dado4 = random.randint(1, 6)
        print(dado3, "---", dado4)
    else:
        igual = True

print("se debio tirar el dado nuevo" , contador1, "Veces")
"""
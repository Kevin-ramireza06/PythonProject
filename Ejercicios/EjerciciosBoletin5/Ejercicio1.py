import random

numeros = []

for i in range(0,7) :
    nuevoNUmero = random.randint(0,50)
    if nuevoNUmero not in numeros :
        numeros.append(nuevoNUmero)

print(numeros)
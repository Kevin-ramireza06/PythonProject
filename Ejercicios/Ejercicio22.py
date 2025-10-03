import random
import math

acabado = False

while acabado == False :
    numero = random.randint(1, 100)
    raiz = math.sqrt(numero)
    contador = 0
    if numero in range(1,4) :
            acabado = True
    else:
        for i in range(2,int(raiz)+1):
            if numero % i != 0 :
                acabado = True

    if acabado == True :
        print(numero)


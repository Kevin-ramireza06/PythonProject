numero1 = 0
numero2 = 1
numeroAux = 0
size = int(input("Ingresa cuantas veces se haga la secuencia: "))
print(numero1)
print(numero2)

for _ in range(1,size-1) :
    numeroAux = numero1 + numero2
    numero1 = numero2
    numero2 = numeroAux
    print(numeroAux)
numero1 = int(input("Porfavor ingresa el primer numero: "))
numero2 = int(input("Porfavor ingresa el segundo numero: "))

for i in range(numero1,numero2) :
    contador = 0
    for j in range(1,(int(i/2))+1) :
        if i % j == 0 :
            contador += 1
    if contador == 1 :
        print(i)
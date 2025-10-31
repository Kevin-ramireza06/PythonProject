frase = input("Porfavor introduce una frase: ")

#la lluvia en sevilla es una pura maravilla

letra = input("Porfavor ingresa la letra a mantener: ")

if len(letra) == 1 :
    for i in range(0, len(frase)):
        if letra == frase[i]:
            print(letra, end="")
        elif frase[i] == " ":
            print(" ", end="")
        else:
            print("*", end="")
else:
    print("Porfavor ingresa una sola letra")


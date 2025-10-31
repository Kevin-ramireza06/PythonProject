frase = input("Porfavor introduce una frase: ")
fraseCompleta = ""

#la lluvia en sevilla es una pura maravilla
contador = 0

letra = input("Porfavor ingresa la letra a mantener: ")

if len(letra) == 1 :
    for i in range(0, len(frase)):
        if letra == frase[i]:
            contador += 1
            fraseCompleta += frase[i]
        elif frase[i] == " ":
            fraseCompleta += frase[i]
        else:
            fraseCompleta += "*"
    print("\nLa letra", letra, "aparece",contador,"veces")
    print("Resultado: ",fraseCompleta)
else:
    print("Porfavor ingresa una sola letra")
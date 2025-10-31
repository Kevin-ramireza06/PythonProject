#from Ejercicios.Practica.Punto2 import contador

frase = input("Porfavor introduce una frase: ")
fraseCompleta = ""
#la lluvia en sevilla es una pura maravilla
contadorWin = 0
while(frase != fraseCompleta) :
    contador = 0
    letra = input("Porfavor ingresa la letra a mantener: ")
    if len(frase) != len(fraseCompleta) :
        for i in range(0, len(frase)):
            fraseCompleta += "*"
    for i in range(0, len(frase)):
        if letra == frase[i]:
            contador += 1
            fraseCompleta = fraseCompleta.replace(fraseCompleta[i], frase[i])
            #fraseCompleta += frase[i]
        elif frase[i] == " ":
            fraseCompleta = fraseCompleta.replace(fraseCompleta[i], frase[i])
            #fraseCompleta += frase[i]
        else:
            fraseCompleta = fraseCompleta.replace(fraseCompleta[i], "*")
            #fraseCompleta += "*"
    print("\nLa letra", letra, "aparece",contador,"veces")
    print("Resultado: ",fraseCompleta)
    contadorWin += 1

print("Haz ganado. has necesitado",contadorWin,"para completar la frase")
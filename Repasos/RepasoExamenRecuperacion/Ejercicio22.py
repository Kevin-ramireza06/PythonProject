
def indexarPalabras(texto):
    letrasRepetidas = {}

    textoSeparado = texto.split(" ")

    for palabra in textoSeparado:
        if len(palabra) > 2:
            letra = palabra[:1:]
            if letra not in letrasRepetidas:
                letrasRepetidas[letra]= set([palabra])
            else:
                letrasRepetidas[letra].add(palabra)

    texto= "Diccionario resultante: {"
    for i in letrasRepetidas:
        texto += f" '{i}': {letrasRepetidas[i]}"

    print(texto)

indexarPalabras("El gato gordo corre por el garaje grande y el perro ladra")




def diccionarioDeUnTexto(texto):
    diccionarioPalabras = {}

    palabras = texto.split(" ")

    for palabra in palabras:
        diccionarioPalabras[palabra] = 0

    for palabrasRepetidas in diccionarioPalabras:
        for i in palabras:
            if i == palabrasRepetidas:
                diccionarioPalabras[palabrasRepetidas] += 1

    return diccionarioPalabras

print(diccionarioDeUnTexto("Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"))

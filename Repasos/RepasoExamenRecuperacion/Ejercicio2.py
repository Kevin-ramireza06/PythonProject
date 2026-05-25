
diccionarioFrutas = {
    "Aguacate" : 4.35,
    "Mandarina": 2.60,
    "Kiwi": 3.75,
    "Naranja": 1.80,
}

repeticion = True

while repeticion != False:

    opcion = input("¿Qué fruta quieres comprar?")

    if opcion == "fin":
        repeticion = False
        break

    if opcion not in diccionarioFrutas:
        print("Lo siento mucho pero no vendemos esa fruta")

    if opcion in diccionarioFrutas:
        try:
            peso = float(input("¿Cuantos kilos quieres?"))
            print(f"{peso} de {opcion} cuestan {peso * diccionarioFrutas[opcion]}$")
        except ValueError:
            print("No has introducido bien la cantidad que quieres")
            continue

#Crear un programa o una función que reciba un diccionario con los datos de los clientes de una tienda
#y su edad y los muestre por consola ordenados por nombre de pila. El diccionario, ya creado en el
#código de tu programa, tendrá esta forma
#clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto,
#Francisco": 44, "Cotón, Carmelo": 56 }
#Y la salida por consola así:
#Carmelo Cotón (56)
#Francisco Rupto (44)
#José Chuletón (35)
#Rubén Tosidad (27)

clientes = {
    "Chuletón, José": 35,
    "Tosidad, Rubén": 27,
    "Rupto, Francisco": 44,
    "Cotón, Carmelo": 56
}

def ordenarDiccionario(diccionario):

    elementos = []
    for clave, valor in diccionario.items():
        claveSeparada = clave.split(", ")
        elementos.append(f"{claveSeparada[1]} {claveSeparada[0]} ({valor})")

    elementos.sort()

    for elemento in elementos:
        print(elemento)

#ordenarDiccionario(clientes)

def nuevoCliente(diccionario, nombre, apellido, edad):
    nuevoCliente = f"{apellido}, {nombre}"

    if nuevoCliente not in diccionario:
        diccionario[nuevoCliente] = edad
    else:
        opcion = input("¿Quires sobreescribir la edad de esta persona?")
        if opcion == "s":
            diccionario[nuevoCliente] = edad

    ordenarDiccionario(diccionario)

#nuevoCliente(clientes, "Armando", "Casas", 99)

def cumpleClientes (diccionario, nombre, apellido):
    cliente = f"{apellido}, {nombre}"
    if cliente not in diccionario:
        print("El cliente no existe")
        return

    diccionario[cliente] = diccionario[cliente] + 1
    ordenarDiccionario(diccionario)

cumpleClientes(clientes, "José", "Chuletón")





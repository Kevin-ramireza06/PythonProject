def miFUncion():
    texto = "Hol mundo"
    texto2 = "Hola mundo otra vez"
    print("Desde la funcion: ", texto)
    return texto2
#Con las funciones si hay ambito

texto = "hola mundo por fuera"
print(miFUncion())
print(texto)

def miFUncionConParametros(texto, veces):
    for i in range(0, veces):
        print(texto)
        veces = 7

#print(parametro)

miFUncionConParametros("sisas",3)
miFUncionConParametros(3,True)

def miFUncionConParametrosDeReferencia(texto, lista,numero):
    texto = "Holiwis"
    numero = 1.1
    lista[1] = 23

textoPR = "Sisas"
numeroPR = 5.5
listaPR = [1,22,13]

#Lo unico que se pasa por parametro como referencia son las listas, osea que si una lista se pasa por
#parametro, en una funcion se modifica, en cambio el resto de tipos de valores no

miFUncionConParametrosDeReferencia(textoPR,listaPR,numeroPR)
print(textoPR,listaPR,numeroPR)


def saludoParametroPorDEfecto(nombre, mensaje = "Hola"):
    print(mensaje, nombre)


saludoParametroPorDEfecto("Kevin")
saludoParametroPorDEfecto("Kevin", "Sisas")

def saludoParametroPorDEfecto1(nombre, mensaje = "Hola", despedida = "Hasta la vista"):
    print(mensaje, nombre,despedida)

saludoParametroPorDEfecto1("Kevin", despedida="Adios")
saludoParametroPorDEfecto1("Kevin", "Bienvenida")

def argumentosVarios(nombre, *titulos):
    #ASi hacemos que una funcion pueda recibir una cantidad de parametros indefinidos
    #Y funcionan como una tupla
    for titulo in titulos:
        print(titulo, end=" ")
    print(nombre)

argumentosVarios("Kevin", "Si", "No", "Hola")
argumentosVarios("Kevin", "Caca")

def mostarDatos(nombre,edad):
    print("Nombre:", nombre , "Edad:", edad)

mostarDatos("Kevin", "19")

datos = ["Pedro", 32]
mostarDatos(*datos)
#De esta forma le pasamos "Empaquetados" los valores de una lista/tupla a funcion
#Obviamente ordenados por los tipos de valores que recibe la funcion

def devolverVariosValores() :
    return 14,17,56

num1, num2, num3 = devolverVariosValores()

print(num1, num2, num3)







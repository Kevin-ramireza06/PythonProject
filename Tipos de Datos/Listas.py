#Listas

print("---------------------Listas------------------------")

lista = []
lista2 = list()

#Estas son las foormas de crear listas

lista3 = [5,1,3,2,6] # de eta forma es la unica manera en la que se crea con objetos por default

lista4 = [34,"pepe","sisas", True, 77,[3,2,1]]
#En python en principio puedo guardar cualquier cosa en un array, casi que no es estricto

print(lista4) #AL imprimir una liista lo imprime casi que como lo escribimos al guardarlo

for element in lista4 :
    print(element)
#Para recorrerlas es igual que con los textos

for posicion in range(0, len(lista4)) : #La funcion len me devuelve el tamaño de la lista
    print(posicion , "->" , lista4[posicion] )

lista4.append("Elemento nuevo") # el metodo append agrega un elemento al final

print(lista4)

lista5 = lista3 + [6,7]
#Taambien podemos sumar listas

print(lista5)

lista6 = lista4 + lista5

print(lista6)

elementoSacado = lista6.pop(13) #el metodo pop saca un elemento de la lista y nos permite usarlo, literalmente lo elimina de la lista
print(lista6)

lista6.remove(6) #este elimina el primer elemento con el que coincida el parametro, si no existe da error
print(lista6)

lista3.sort() #Este ordena liistas de menor a mayor, pero solo si tienen los mismos tipos de datos, si no da error
#Este modifica la lista entera, no crea otra lista ordenada, si no que modifica la que le pasemos
print(lista3)

lista3.sort(reverse=True) #Asi lo podemos organizar de menor a mayor
print(lista3)

texto = str(lista3) #Tambuien podemos cambiar el tipo de dato de las listas de manera sencilla
print(texto)

texto = texto.replace("[", "")
texto = texto.replace("]", "")
#Aqui la usamos como si fuese un string

print(texto)

matriz = [[1,2,3],[4,5,6],[7,8,9]] #De esta forma se puede hacer una matriz, es un array de arrays
#Pero en python no existe como tal las matrices
print(matriz[1][0])

print(lista3[:4]) #aqui tambine funcionan los emparedados, exactamente igual
print(lista3[2:])
print(lista3[1:3])
print(lista3[::-1])

if 3 in lista3:
    print("Esta en la lista 3")

if 88 not in lista3:
    print("NO esta en la lista 3")

#De estas formas podemos saber si una lista tiene o no un elemento
#Tambien funciona con cadenas

#Tuplas

print("---------------------Tuplas------------------------")

tupla = (1,2,3,4,5)
print(tupla)

tupla2 = ("Maria", "Hola", "Mundo")
tupla3 = ("Sisas" , False, 32, (1,2,3))

#Las tuplas son listas que np se pueden modificar, y se crean con los parentesis

print(tupla2)
print(tupla3)

tupla4 = ()
tupla5 = ("Sevilla",) # Sin la coma python pensara que es un elemento con parentesis redundante, asi ya lo reconoce

print(tupla4)
print(tupla5)

listaTupla = list(tupla2) #Se puede convertir una tupla a lista y modificarla, pero es absurdo
print(listaTupla)

textoTupla = str(tupla3)
print(textoTupla)

tupla6 = tuple([1,2,3,4,5])
print(tupla6)

tupla7 = tuple("Hola Mundo")
print(tupla7)

tupla8 = "Pepe" , "Pepa" , "11", tupla6 , "Si"
print(tupla8)

#tupla8[1] = "Pepa"
print(tupla3)
#tupla3[3][1] = 4
print(tupla3)

if 4 in tupla6 :
    print("El 4 esta en la tupla")

if 33 not in tupla6 :
    print("El 33 no esta en la tupla")

profesor = ("Pepe", "Ramirez", 57, False, True)
nombre, apellidos, edad, alumno, profe = profesor
print(apellidos,edad)

#Conjuntos

print("---------------------Conjuntos------------------------")

conjunto = {"Ana", "Juan", "Jose", "Sancho", "Natalia"}
print(conjunto)

#Los conjuntos son estructuras que no contienen orden, son mutables y se peuden usar las operaciones logicas
conjunto2 = set(["Agustin", "Ana", "Natalia", "Javier"])
print(conjunto2)

if "Agustin" in conjunto2 :
    print("Agustin esta en conjunto 2")

if "Javier" not in conjunto :
    print("Javier no estya en el primer conjunto")

for i in conjunto :
    print(i)

#Al no tener orden, no los podemos recorrer con indices
#for i in range(0, len(conjunto)) :
    #print(conjunto[i]) Esto da error

conjunto2.add("Jose Maria") #Add nos permite agregar un elemento al conjunto, pero en cualquier posicion
print(conjunto2)

conjunto2.add("Jose Maria") #Tampoco se pueden agreagar duplicados, si se intenta simplemente se ignora
print(conjunto2)

conjunto2.remove("Agustin") #De esta forma podemos eliminar elementos
print(conjunto2)

conjunto2.discard("Ana") #tambien nos permite borrar, la diferencia con remove es que remove, si no esta el elemento tira error
print(conjunto2)

profeRecuperado = conjunto2.pop() #El punto pop nos recupera y elimina del conjunto el primer elemento, pero ps siempre es aleatorio
print(profeRecuperado)
print(conjunto2)

#conjunto.clear() # el clear nos vacia completamente un conjunto, y de salida muestra "set()"
#print(conjunto)

conjunto3 = set([1,2,3,3,4,5]) #Al crearla con duplicados, crea el conjunto sin ellos
print(conjunto3)

conjunto4 = set("Hola Mundo Sisas") #Aqui guarda cada caracter como un elemento diferente, si esta repetida, la ignora
print(conjunto4)

listaConjunto  = list(conjunto2)
print(listaConjunto)
tuplaCOnjunto = tuple(conjunto3)
print(tuplaCOnjunto)
textoConjuto = str(conjunto4)
print(textoConjuto)

#Operaciones

print(conjunto.union(conjunto2)) #conjunto | conjunto2) #union
print(conjunto.intersection(conjunto2)) #conjunto & conjunto2) #interseccion
print(conjunto.difference(conjunto2)) #conjunto - conjunto2) #diferencia
print(conjunto.symmetric_difference(conjunto2)) #conjunto ^ conjunto2) #diferencia exclusiva

print("------Forma Adicional de recorrer listas-------")

for i, nombre in enumerate(lista4):
    print(i,"-",nombre)

print("-----------------------------------------")
print("-----------------------------------------")

numero1 = 7
numero2 = numero1
numero2 = numero2 * 2

print(numero2 , numero1)

numero1 = [7]
numero2 = numero1 #Lo que demuestra esto es que las variables de lista se guardan como referencia y no como copia
#Por lo que en listas hacer que una variable apunte a otra lista, si esa variable se modifica, cambia la lista tambien
#como en este ejemplo
numero2[0] = numero2[0] * 2

print(numero2 , numero1)

#Si queremos hacer una copia, y qe los cambios en un lado no afecten al otro hacemos una copia

numero1 = [7]
numero2 = numero1.copy() # asi hacemos una copia
numero2[0] = numero2[0] * 2

print(numero2 , numero1)

def miniFuncion(Listado):
    print(Listado)

miniFuncion(numero1.copy()) # asi mismo tambien se pueden pasar por argumento

#Diccionarios

print("---------------Diccionarios---------------")

diccionario = {"Nombre": "sarah", "Edad" : 57, "Estado civil" : True }

#Cada "," separa un elemento clave/ valor, a la izquierda de los : es la clave, a la derecha es el valor

print(diccionario)

print(diccionario["Edad"]) #Para seleccionar un valor del diccionario, es similar que los arrays, solo que se pone el
#De la llave

diccionario2 = {"Nombre": "sarah", "Edad" : 57, "Estado civil" : True , "Edad" : 55}
#No se pueden tener elementos duplicados, al intentarlo, se reescribe el primer elemento por el segundo
print(diccionario2)

for element in diccionario :
    print(element)
    #Al recorrerlo de esta forma, elemento captura la clave NO EL VALOR
    print(diccionario[element])
    #Para capturar el valor, es como dijimos antes

for elemento in diccionario2:
    print(elemento , ":", diccionario2[elemento])

for clave, valor in diccionario.items() :
    #DE esta forma podemos capturar la clave y el valor, el metodo items, devuelve los 2, y en el for asignamos las
    #variables para asignar los valores
    print(clave , "->" , valor)

print(diccionario.get("Edad")) #El metodo get me permite coger el valor que tenga la clave que mande

print(diccionario.get("Edad2"))
#print(diccionario["Edad2"]) la mayor diferencia con este, es que la forma clasica devuelve un error cuando la clave no
#existe

diccionario["Edad"] = 33 #asi se puede cambiar el valor de una clave
print(diccionario["Edad"])

diccionario2["Asignatura"] = "BBDD" #Si me equivoco copn la clave, con esta sintaxis crea uan nueva clave, con ese valor
#Al final del diccionario
print(diccionario2)

diccionario2.clear() #Este metodo vacia el diccionario/lista

print(diccionario2)

#diccionario3 = dict() #Asi podemos crear un diccionario vacio
#

diccionario3 = dict(Primero = "Nonas", Segundo = "Sisas") # de esta otra forma cramos el diccionario con valores por default

diccionario3["Elemento"] = "Sisarras"

print(diccionario3)

diccionario4 = {} #asi tambien se puede crear vacio

print(diccionario4)

print(diccionario)
print(diccionario.keys()) #Este devuelve todas las llaves en una lista
print(diccionario.values()) #Este devuelve todas los valores en una lista
print(diccionario.items()) #Este devuelve todo

print(diccionario.get("Titulo" , "NO existe")) #EL metodo get tiene de segundo parametro, lo que quiero que devuelva en
#caso de que no encuentre el valor

print(diccionario)

diccionario.pop("Estado civil") #Este metodo nos permite borrar un elemento, mediante la clave
#diccionario.pop("Estado civil2") si no existe da error


print(diccionario)

elementoBorrado = diccionario3.popitem() #El popitem borra el ultimo elemento insertado y lo devuelve
print(elementoBorrado)
print(diccionario3)

diccionario.update(diccionario3) #De esta forma actualizamos de manera masiva el diccionario, agregando todos los
#elementos de un diccionario en otro, como el diccionario en parametro tiene la misma clave que el otro, el original se
#le actualiza la clave

print(diccionario)

diccionario6 = {"Lista" : [1,2,3] , "Boolean" : True , "Numero" : 9 , "Texto" : "Sisas"}
#Los diccionarios tambien pueden guardar cualquier tipo de dato de los que ya hemos visto antes

print(diccionario6)

print(diccionario6.setdefault("Elemento","Si"))
print(diccionario6)
print(diccionario6.setdefault("Boolean",False))
print(diccionario6)
#El metodo setdefault, devuelve el valor de una clave que pongamos, si no esta en la lista, la agreaga al final
#Y si esta, devuelve el valor anterior y lo modifica

import random
print("--------------Ejercicio Crear popitem anterior--------------")

def popitemrandom(diccionario) :
    #lista = []
    #for i in diccionario :
    #    lista.append(i)
    lista = list(diccionario.keys())
    numeroRandom = random.randint(0, ( len(lista) - 1 ))

    itemEliminado = diccionario[lista[numeroRandom]]
    diccionario.pop(lista[numeroRandom])

    return itemEliminado

print(diccionario)
print(popitemrandom(diccionario))
print(diccionario)


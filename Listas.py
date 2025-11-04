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


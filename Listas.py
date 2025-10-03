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



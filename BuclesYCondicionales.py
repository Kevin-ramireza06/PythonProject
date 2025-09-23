# Condicionales

"""
Estan los mismos operadores logicos que en java (+, -, =, ==, +=, -=, < , >, <=, >= ), solo que
aqui el ||, el && y el ! cambian

|| -> or
&& -> and
! -> not
"""

edad = 33

if edad > 65:
    print("Eres un viejo")
    print("Esto se va a ejecutar en el else")
else:
    #print("NO eres un viejo")
    pass #Esta funcion nos permite tener un bloque de instrucciones vacio


"""
Aqui el condicional es diferente, no es necesario poner los parentesis, y el bloque de instrucciones
se define despues de los dos puntos ":"

IMPORTANTE: los bloque de instrucciones se definen con las tabulaciones, asi que todo lo que este
tabulado debajo de los dos puntos pertenece al mismo bloque de instruccion, para cerrar el bloque
de instrucciones simplemente quitamos las tabulaciones 

"""

if edad > 60:
    print("Eres un viejo")
elif (edad > 30) and (edad < 40):
    print("Ojo principe")
elif edad > 18: # Asi se usa el else if
    print("Eres un adulto")
elif edad > 15:
    print("Eres un adolescente")

else:
    print("Eres un niño")

print("Esto no ya que esta fuera del bloque , y es el final del programa")

#Bucles

#Bucle for

for i in range(0,5):
    print(i)
"""
Asi se hace un for PERO cuidado ya que el rango que se define ahi, el bucle empieza y adquiere el priemr valor, pero no
el segundo
"""

for i in "Hola Mundo": #Tamien podemos iterar en cadenas, aqui el for va a omitir el ultimo valor(El salto de linea)
    print(i, end="") # asignamos que el end sea vacio para que se escriban de seguido

for i in range(0,30, 2):
    print(i, end=", ")

print("-----------------------------")

for i in range(30, 10, -1):
    print(i, end=", ")

    #De esta forma hacemos que corra hacia atras el bucle, invirtiendo los valorees mayot y menor, e indicando los saltos en negativo

"""
La funcion range tiene 3 argumentos, el primero es el inicio y lo invluye, el segundo es el final y no lo invluye, y el
tercero son los saltos que queremos que de, si no mas asignamos un argumento, este ira por defecto desde el 0 al numero
asignado (Sin incluirlo), si ponemos 2 ira desde el primer numero hasta al segundo sin incluirlo, y si ponemos 3 ira del primer al 
segundo con los saltos que asignamos
"""

for i in range(52):
    print( i )

print("------------------------------------------------------------------")


#Bucle while

i = 0

while i < 10 :
    print(i)
    i+= 1

"""
Asi se crea el while, al igual que el if se ppuede poner la condicion sin parentesis y su contenido son todas aquellas
cosas que estan tabuladas, aqui en phyton no existe el "do while" ni se pueden declarar variables vacias
"""
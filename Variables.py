edad = 19
print(edad)

"""
las variables se definen super facil, solo con escribir algo y asignarle
un valor funciona, no hace falta definir tipos
"""

edad = "Dies y nueve"

print(edad)

"""
Tambien se puede cambiar los valores de las variables super facil, esto es
algo a tener muy en cuenta, al no ser un lenguaje tipado las variables 
pueden coger cualquier valor
"""

#Tipos de datos mas comunes

texto = "Sisarras" # Los textos se tratan como arrays aqui tambien
print(texto)

boleano = True # Para asignar booleans se teinen que poner en mayuscula
print(boleano)

entero = 19
print(entero)

decimales = 1.9
print(decimales)

#Operadores

"""
Existen los operadores tipicos + - * / % y hay 2 nuevos tipos aqui

// = lo que devuelve es el cociente de una operacion
** = este devuelve la potencia del numero

Tambien podemos usar las formas sencillas de asignar += ; *= ... y funciona con los nuevos //= ; **=
"""

cociente = 5 // 2
print(cociente)

potencia = 2**4
print(potencia)

# Tipado (Tambien se puede trunca los valores para usarlos como un tipo de dato que necesitamos)

textoConcatenado = "Hola" + " " + "Mundo"
print("texto: " + textoConcatenado)

decimalEntero = 5.3
decimalEntero = int(decimalEntero)
print(decimalEntero)

enteroDecimal = 10
enteroDecimal = float(enteroDecimal)
print(enteroDecimal)

#FUncion Print

"""
En phyton podemops tener funciones y que estas tengan una cantidad indefinida de argumentos, el ejemplo mas sencillo
 es print 
"""

print("Hola")
print("Hola","mundo")

"""
la funcuon print tiene tiene 2 argumentos predefinidos que son end  y sep, end sirve para poner algo al final de la 
cadena que estemos metiendo, y sep sirve para agregar un separador entre los argumentos del print, por default end tiene
un salto de linea(\n) y en sep tiene un espacio(" ") pero estos los podemos modificar dentro del print de la siguiente
manera
"""

print("SIsas", end="//\n")
print("Hola","mundo", sep="/*/")
text =  "Hello world"

print(len(text))

"""
for c in text :
    print(c)
"""

for i in range(0 , len(text)) :
    print( i, " -> " , text[i])

#En python las cadenas de caracteres tambein funcionan como un array

print(text[3:8])

# de esta forma puedo sacar un fragmento de la cadena, incluyendo el primer valor pero no el ultimo

print(text[:8]) # va desde la primera letra hasta la octava sin contarla

print(text[3:]) #ca desde el tercer elemento contandolo hasta el final de la cadena

print(text[::2]) #Puede tener un tercer parametro, que es los saltos que este va aa aejcutar, en este caso va de incio a fin saltando de dos en dos
#Este puede tener valores negativos, y

# si no ponemos algun lado, usara su extremo, su inicio o su fina

#Podemos usar numeros negativos, en donde el -1 seria el final de la cadena y asi sucesivamente

"""text[2] = "x"""

#No se puede tampoco modificar la cadena directamente

numberString = str(3.1416) # La funcion str, me convierte un numero a un Sting

print(numberString)

print(text.upper()) #ESta funcion vuelve el String en mayusculas sin tocar la cadena original

print(text.lower()) #ESta funcion vuelve el String en minusculas sin tocar la cadena original

print(text.swapcase()) #ESta funcion invierte las mayusculas/minusculas de una cadena

print(text.find("ello")) # esta funcion me indica la posicion donde empieza una cadena en el texto, da -1 si no existe

print(text[2:]. find("o"))

print(text.count("x"))

print(text.replace("o","x"))







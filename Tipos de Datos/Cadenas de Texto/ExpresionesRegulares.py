import re

patron = r"ola" #De esta forma se define un texto con expresion regular
#asi indica que la cadena si o si tiene que tener lo que este ahi

if re.match(patron, "ola manin"): #Esto busca una coincidencia al principio
    print("Hay coincidencia")
else:
    print("No hay")

if re.search(patron, "popola"): #Esto busca una coincidencia en cualquier parte de la cadena
    print("Hay coincidencia")
else:
    print("No hay")

if re.fullmatch(patron, "ola"): #Esto busca si la cadena es exactamente igual a lo que se ponga
    print("Hay coincidencia")
else:
    print("No hay")

if re.fullmatch(r"[0-9]{3,5}", "111"):
    # Esto busca que haya numeros del 0 al 9 minimo 3 maximo 5
    print("Hay coincidencia")
else:
    print("No hay")

if re.fullmatch(r"[0-9]+", "112"):
    # El mas valida si hay alguno, si hay mas lo devuelve bien, y si no, No (1 o mas)
    print("Hay coincidencia")
else:
    print("No hay numero")

if re.fullmatch(r"[0-9]{8}[A-Za-zÑñ]", "112"):
    #Intento de hacer un DNI
    print("Hay coincidencia")
else:
    print("No hay numero")


prueba = r"([1-9]|1[0-2])";
if re.fullmatch(prueba, "12"):
    # El mas valida si hay alguno, si hay mas lo devuelve bien, y si no, No
    print("Hay coincidencia con or")
else:
    print("No hay numero con or")

if re.fullmatch(r"\w+", "Bandera_111"):
    # este valida cualquier caracter alfanumerico min, may, y barra baja (esto gracias a que el \w tiene un +)
    print("Hay coincidencia con barra baja")
else:
    print("No hay numero con barra baja")

if re.fullmatch(r"[0-9]?", "1"):
    #La interrogacion valida si es hay 0 o 1
    print("Hay coincidencia")
else:
    print("No hay numero")

if re.fullmatch(r"[^5]", "5"):
    #Al poner los corchetes, si no ponemos lass llaves, indica que solo va abuscar en una cadena de un valor,
    #Cualquier cosa diferente de 5
    print("Hay coincidencia")
else:
    print("No hay numero")

if re.fullmatch(r"[^5][^0]", "8"):
    #Al poner los corchetes, si no ponemos lass llaves, indica que solo va abuscar en una cadena de un valor,
    #Cualquier cosa diferente de 5
    print("Hay coincidencia")
else:
    print("No hay numero")

#Estas funciones no devuelven true o false, devueven otro tipo de info
#Y cuando no hay coincidencia devuelve none


#   Patrón	Significado
#
#   .	    Cualquier carácter
#   \d	    Dígito (0–9)
#   \w	    Letra o número (cualquier caracter alfanumerico min, may y barra baja)
#   \s	    Espacio en blanco
#   +	    Uno o más
#   *	    Cero o más
#   ?	    Cero o uno
#   {n,m}	Entre n y m repeticiones
#   ^	    Inicio de línea
#   $	    Fin de línea
#   [abc]	Cualquiera de a, b o c
#   [^abc]	Cualquiera menos a, b o c


patronM = r"ola"

# Saber si empieza por algo:
if re.match(patronM, "oladam2"):
    print("Hay coincidencia")
else:
    print("No hay coincidencia")


# Saber si existe en la cadena:
print()
if re.search(patronM, "holadam2"):
    print("Se ha encontrado")
else:
    print("No se ha encontrado")


# Saber si hay coincidencia exacta:
print()
if re.fullmatch(patronM, "ola"):
    print("Hay coincidencia exacta")
else:
    print("No hay coincidencia exacta")

# Coincidencias en rangos:
print()
if re.fullmatch(r"[0-9]{3,5}","12333"):
    print("Hay coincidencia en los nums")
else:
    print("No hay coincidencia en los nums")

print()
if re.fullmatch(r"[0-9]{8}[A-Za-zÑñ]","12333234A"):
    print("Hay coincidencia en el DNI")
else:
    print("No hay coincidencia en el DNI")


print()
if re.fullmatch(r"[1-9]|1[0-2]","12"):
    print("Hay coincidencia en el mes")
else:
    print("No hay coincidencia en el mes")


print()
if re.fullmatch(r"(\w+)","bananaboy448"):
    print("Hay coincidencia en el texto")
else:
    print("No hay coincidencia en el texto")


print()
if re.fullmatch(r"[0-9]?","7"):
    print("Hay coincidencia en el numero2")
else:
    print("No hay coincidencia en el numero2")


print()
if re.fullmatch(r"[^5]","6"):
    print("Hay coincidencia en el numero3 o letra")
else:
    print("No hay coincidencia en el numero3 o letra")


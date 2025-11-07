import re

patron = r"ola" #De esta forma se define un texto con expresion regular
#asi indica que la cadena si o si tiene que tener lo que este ahi

if re.match(patron, "ola manin"): #Esto busca  una coincidencia al principio
    print("Hay coincidencia")
else:
    print("No hay")

if re.search(patron, "popola"): #Esto busca  una coincidencia en cualquier parte de la cadena
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
    # El mas valida si hay alguno, si hay mas lo devuelve bien, y si no, No
    print("Hay coincidencia")
else:
    print("No hay numero")

if re.fullmatch(r"[0-9]{8}", "112"):
    #Intento de hacer un DNI
    print("Hay coincidencia")
else:
    print("No hay numero")

if re.fullmatch(r"[1-9]|1[0-2]]", "14"):
    # El mas valida si hay alguno, si hay mas lo devuelve bien, y si no, No
    print("Hay coincidencia")
else:
    print("No hay numero")

if re.fullmatch(r"\w+", "Bandera_111"):
    # ewste valida cualquier caracter alfanumerico min, may, y barra baja
    print("Hay coincidencia")
else:
    print("No hay numero")

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


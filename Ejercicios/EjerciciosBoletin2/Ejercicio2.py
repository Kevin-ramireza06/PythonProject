palabraCompleta = ""
palabra1 = input("Escribe palabras: ")
palabra2 = input("Escribe palabras: ")
primeraPlabra = min(palabra1, palabra2)
ultimaPlabra = max(palabra1, palabra2)
palabra3 = input("Escribe palabras: ")
if(palabra3 < primeraPlabra) :
    palabraCompleta += ultimaPlabra + " " + primeraPlabra + " " + palabra3
else:
    if palabra3 < ultimaPlabra :
        palabraCompleta += ultimaPlabra + " " + palabra3 + " " + primeraPlabra
    else:
        palabraCompleta += palabra3 + " " + ultimaPlabra + " " + primeraPlabra
print(palabraCompleta)
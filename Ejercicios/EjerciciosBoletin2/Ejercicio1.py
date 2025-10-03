palabraCompleta = ""
palabra1 = input("Escribe palabras: ")
palabra2 = input("Escribe palabras: ")
primeraPlabra = min(palabra1, palabra2)
ultimaPlabra = max(palabra1, palabra2)
palabra3 = input("Escribe palabras: ")
if(palabra3 < primeraPlabra) :
    palabraCompleta += palabra3 + " " + primeraPlabra + " " + ultimaPlabra
else:
    if palabra3 < ultimaPlabra :
        palabraCompleta += primeraPlabra + " " + palabra3 + " " + ultimaPlabra
    else:
        palabraCompleta += primeraPlabra + " " + ultimaPlabra + " " + palabra3
print(palabraCompleta)
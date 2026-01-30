nombre = "Kevin Andres"
edad = 19
sueldo = 1200.845
print("Mi nombre es", nombre, "tengo", edad , "Y cobro",sueldo)
print("Mi nombre es %s tengo %d años y cobro %.2f" %(nombre,edad,sueldo))
print(f"Mi nombre es {nombre} tengo {edad} años y cobro {sueldo:.2f}" )

promedio = 0.86754
print(f"El porcentaje de aprobados es de {promedio:.4%}") # asi se saca el porcentaje, con el punto definimos cuantos decimales
#Usando print(f"") es una forma especial de python para darle formatto a las salidas, mediante las llaves podemos
#poner variables y que se muestren en el print, y desde ahi mismo las podemos formatear de las maneras que hemos visto
poblacion = 1234567899
print(f"La poblacion del pais es de {poblacion: ,}") #asi le asignamos separador de millares que sea la coma
n1 = 11
n2 = 33
n3 = 165
print(f"Numeros:\n{n1:04d}\n{n2:04d}\n{n3:04d}")

print(f"Justificado a la izquierda: ***{n1:<20}***")
print(f"Justificado a la derecha  : ***{n1:>20}***")
print(f"Justificado a la centro   : ***{n1:^20}***")

lista = [1,2,3]
print(f"Inspeccionando variables {lista = }")
#de esta forma le metemos justificacion o espacios al rededor de una variable

#Asi se trabaja con f-string de varias lineas

ficha = f"""
Ficha de Kevin
--------------------------------
Nombre: {nombre}
Edad: {edad}
Sueldo: {sueldo:.2f} euros
--------------------------------
"""
#se crea una variable y dentro guardamos f""" contenido """ y desde ahi podemos usar todas los formatos que hemos visto

print(ficha)

def devolverNombre():
    return "Kevin"

print(f"MI nombre es {devolverNombre()}")

print(f"n1 es par {True if n1%2 == 0 else False}")
print(f"n2 es par {"Si" if n2%2 == 0 else "No"}") #asi se peden poner condiciones, en un extremo lo que queremos
#Que devuelva y en el otro el else

#Se puede usar la sintaxis de un if normal pero ocupara mas lineas y sera mas incomodo

nota = 5
print(f"Nota: {'Excelente' if nota > 8 else 'Suficiente' if nota > 5 else 'Suspenso'}")



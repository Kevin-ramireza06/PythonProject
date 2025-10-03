calificacion1 = float(input("Porfavor ingresa tu tercer nota: "))
calificacion2 = float(input("Porfavor ingresa tu tercer nota: "))
calificaicon3 = float(input("Porfavor ingresa tu tercer nota: "))

calificacionTotal = (calificacion1*0.05) + (calificacion2*0.20) + (calificaicon3*0.80)

print("Nota real: " , round(calificacionTotal,2))
print("Nota boletin: " , round(calificacionTotal,0))


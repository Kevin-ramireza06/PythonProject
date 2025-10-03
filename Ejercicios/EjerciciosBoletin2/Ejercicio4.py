calificacion1 = float(input("Porfavor escribe tu primmer nota:(1 al 10) "))
calificacion2 = float(input("Porfavor escribe tu segunda nota:(1 al 10) "))

if (calificacion1 >= 0 and calificacion1 <= 10) and (calificacion2 >= 0 and calificacion2 <= 10):
    media = (calificacion1 + calificacion2) / 2
    print("Tu media es: " , round(media,0))
else:
    print("Porfavor ingresa valores validos")
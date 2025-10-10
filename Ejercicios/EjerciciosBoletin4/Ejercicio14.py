fecha = input("Porfavor ingresa una fecha con el formato (HH:MM) ")

if len(fecha) == 5 :
    if fecha[2] == ":" :
        if fecha[0:2].isdigit() and fecha[3:5].isdigit():
            horas = int(fecha[0:2])
            minutos = int(fecha[3:5])
            if 0 <= horas < 24 and 0 <= minutos < 60 :
                print("Son las" , horas , "horas con" , minutos , "minutos")
            else:
                print("Porfavor ingresa una hora o minutos validos")
        else:
            print("Porfavor ingresa numeros")
    else:
        print("Debes ingresar los 2 puntos")
else:
    print("Debes ingresar 5 digitos")
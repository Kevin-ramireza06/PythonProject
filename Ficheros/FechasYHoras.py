from datetime import date,time,datetime,timedelta

#Estas librerias nos permiten capturar la fecha actual

hoy = date.today() #Esto nos devuelve el dia actual
print(hoy)

ahora = datetime.now() #este nos devueele la fechaa con laa hora exacta
print(ahora)

hora = time(7,22,15) #De esta forma creamos una hora, y podemos agreagar milisegundos
#SI no especificamos un parametro, lo pone a 0

print(hora)

fecha = date(2020,12,31) #Asi creamos una fecha
print(fecha)

momento = datetime(2006,5,27, 10, 30) # y asi creamos una fecha completa
print(momento)

fechaFormateada = momento.strftime("%d/ %m/ %y") # De esta forma le damos formato a nuestras fechas
#Entre las comillas ponemos como queremos que se vea la fecha, usando el % definimos que eelemento de la fecha va a ser
#y lo ponemos
print(fechaFormateada)

print( momento.strftime("%A %d %B %d-%m-%Y") ) # Tambien hay mas elementos que podemos coger y jugar con ellos

#Podemos convertir un string en un objeto fecha

texto = "2025-01-03 14:30"
formato = "%Y-%m-%d %H:%M" #En este caso creamos el formato desde fuera que tiene la fecha que es tipo String, para castearla
#a este tipo

textoCasteado = datetime.strptime(texto,formato) #COn esta funcion le pasamos de segundo parametro el formato que queremos
#o que tiene la fecha que esta en texto
print(textoCasteado)

print(textoCasteado.year) #Puedo recuperar los elementos de la fecha medainte los getter de la clase date
print(textoCasteado.day)

#Tambien podemos hacer operaciones con fechas

fechaFutura = textoCasteado + timedelta(days=5000, hours=7, weeks=12)#De este modo podemos sumar/restar valores a las fechas
#respetando los viciestos, el dia del que esta, y estas cosas, ejemplo, si pasa del 30 de un mes, ps pasa a contar el restante
#del otro mes
print(fechaFutura)


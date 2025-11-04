print("Inicio del programa")

#Asi controlamos excepciones, con el bloque try/except, en el try ponemos lo que pueda soltar excepcion
#y en el except lo que se ejecute si salta excepcion
try:
    denominador = int(input("Ingresa el denominador: "))
    x = 45 / denominador
    print(x)
except ValueError: #Asi se capturan las excepciones ya contempladas
    print("Excpecion de valor")
except ZeroDivisionError:
    print("Excpecion de division entre 0")
except :
    print("Excepcion general")
    #pass #Esta palabra hace que no pase nada al usarla
else:
    print("No ha ocurrido ninguna excepcion")
finally: #
    print("Esto siempre se va a ejecutar haya o no haya excepcion")

numero = int(input("Introduce un positivo "))
assert numero==1 , "El numero no me gusta"

if numero < 0 :
    raise Exception("No es un entero Positivo")
    #De esta forma lanzamos una excepcion creada por nosotros, con la condicion que querramos

print(numero)

#raise ZeroDivisionError("No has dividido entre 0 pero te salto el error pq soy la picha")
#Con el mismo metodo podemos soltar una excepcion reconocida por python, y dejar un mensaje personalizado




print("Fin del programa")
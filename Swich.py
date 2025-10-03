opcion = input("P para jugar, C para configurar o X para salir: ")

match opcion:
    case "P" | "p" | "J" | "j": #Aqui para que varias opcioones ejecuten lo mismo usamos el operador "|"/"or"
        print("Jugaste")
    case "C" :
        print("Configuraste")
    case "X":
        print("Saliste:")
    case _: #De este modo hacemos un "default" ya que el "_" indica que es vacio o quue no nos interesa
        print("Porfavor ingresa un valor valido")

"""
Aqui en en python se usa el match, que funciona similar al swich, pero este no tiene default como tal, y aparte solo se ejecuta
lo que pase en el case, indiferente de si pusimos o no un break, por decirlo de una porma no es necesario
"""

print("Fin del menu")
# 6. Escribe un programa usando POO que, tomando el mismo fichero clientes.txt del ejercicio
# anterior, tenga una clase que se llame cliente donde guarde la información de los clientes que se
# hayan leído del fichero.
# Tu clase debería de tener un constructor para crear el objeto que reciba la línea tal y como se lee del
# fichero. Así:
# cliente01 = Cliente(“Diego Norrea 28222777J”)
# Tu clase deberá de contar con atributos separados para el nombre, el apellido y el NIF.
# Debes de crear un método que se llame mostrar que nos muestre la información del cliente por
# consola en el siguiente formato:
# 28222777J – Norrea, Diego
# Por último, usando esta clase como soporte, haz un listado del contenido del fichero por consola
# que debería de quedar así:
# 28222777J – Norrea, Diego
# 07333888X – Perado, Inés
# 97221345Y - Imedio , Demetrio
# 22876345M – Rija, Roberto
# 12987543C – Tosidad, Rubém
# 32879563V – Adistancia, Armando
# 18000777H – Tequilla, Germán

class Cliente:
    def __init__(self, ficha):
        cliente = ficha.split(" ")
        self.nombre = cliente[0]
        self.apellido = cliente[1]
        self.dni = cliente[2]

    def mostrar(self):
        print(f"{self.dni} - {self.apellido} - {self.nombre}")

try:
    with open("Ejercicio6Prueba", "r") as fichero:
        for linea in fichero:
            linea = linea.strip()
            cliente01 = Cliente(linea)
            cliente01.mostrar()

except Exception as e:
    print(e)
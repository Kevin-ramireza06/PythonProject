# # Escribe un programa usando POO que, tomando el mismo fichero codigos.txt del ejercicio 3,
# # tenga una clase que se llame IBAN donde guarde la información de los códigos IBAN correctos que
# # se hayan leído del fichero.
# # Tu clase debería de tener, al menos, un constructor para crear el objeto y un método llamado
# # mostrar para que se visualice la información del código por consola. El constructor recibirá el código
# # IBAN en formato de cadena de texto. Así:
# # codigoIBAN01 = Iban(“ES1234567890123456789012”)
# # Y debería de admitir como argumento de entrada cualquier IBAN válido independientemente de los
# espacios en blanco tal y como se describe en el anterior ejercicio.
# Tu clase deberá de contar con atributos separados para los diferentes elementos del IBAN (pais, dc,
# entidad, sucursal, dc_cuenta y num_cuenta). El método mostrar, antes mencionado, nos listará los
# códigos de forma similar a como se describe en el ejercicio anterior.
# En definitiva, tu programa debe de funcionar igual que el ejercicio 3 pero usando POO. Puedes,
# si quieres, hacer este ejercicio en lugar del 3 (y tendrás la misma puntuación en ambos) pero no
# al revés.
import re

class Iban:
    def __init__(self, iban):
        self.pais = iban[0:2]
        self.dc = iban[2:4]
        self.entidad = iban[4:8]
        self.sucursal = iban[8:12]
        self.DCCuenta = iban[12:14]
        self.numCuenta = iban[14:]

    def mostrar(self):
        print("Pais:",self.pais)
        print("DC:",self.dc)
        print("Entidad:",self.entidad)
        print("Sucursal:",self.sucursal)
        print("DC Cuenta:",self.DCCuenta)
        print("Numero de Cuenta:",self.numCuenta)

try:
    with open("Ejercicio4Prueba" , "r") as fichero:

        contadorCorrectos = 0
        contadorIncorrectos = 0

        for linea in fichero:
            regex = r"^[A-Z]{2}( *[0-9] *){22}$"

            linea = linea.replace(" ","").strip()
            if re.fullmatch(regex, linea):
                contadorCorrectos += 1
                iban = Iban(linea)
                iban.mostrar()
            else:
                contadorIncorrectos += 1

        print("Hay", contadorCorrectos, "codigos correctos y", contadorIncorrectos, "codigos incorrectos")

except Exception as e :
    print(e)


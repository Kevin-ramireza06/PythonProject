# Haz un programa en Python que haga lo siguiente:
# - Lea del fichero del ejercicio 11 y convierta las parejas usuario:contraseña en objetos de una
# clase
# - Grabe los objetos en un fichero binario que se llame login.bin
# - Lea del fichero binario que has escrito y muestre el contenido de los objetos por consola
# Tú programa debería de funcionar independientemente del número de elementos que haya en
# el fichero, tanto a la hora de grabarlo en disco como de leerlo posteriormente.
# Ejemplo de ejecución:
# Fichero origen: /home/josemaria/login.txt
# Fichero destino: login.bin
# Número de cuentas encontradas: 2
# Listado de cuentas:
# Usuario: josemaria
# Password: abc123
# Fortaleza de la contraseña: 2
# Usuario: alberto
# Password: M4d4g4scar
# Fortaleza de la contraseña: 4
import pickle

class Usuario:
    def __init__(self,usuario, password):
        self.usuario = usuario
        self.password = password

try:
    with open("Ejercicio16Prueba", "r") as fichero:
        ficheroBinW = open( "Ejercicio16PruebaBin", "wb+" )
        for linea in fichero:
            linea = linea.strip()
            partes = linea.split(':')
            usuario = Usuario(partes[0], partes[1])
            pickle.dump(usuario, ficheroBinW)

        listaObjetos = []

        ficheroBinW.seek(0)
        while True:
            try:
                # Intentamos cargar un objeto
                usuario_recuperado = pickle.load(ficheroBinW)

                # Si llega aquí, es que leyó bien un objeto
                print(f"Usuario: {usuario_recuperado.usuario}")
                print(f"Password: {usuario_recuperado.password}")

            except EOFError:
                # Cuando se acaban los datos, salta este error y rompemos el bucle
                break

except Exception as e:
    print(e)
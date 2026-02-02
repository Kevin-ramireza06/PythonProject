# 7. Te ha contratado la policía nacional para que hagas un programa que permita ver si un ciudadano
# tiene ficha por delitos previos y mostrar los resultados. El archivo de la policía se llama
# delincuentes.txt y tiene este formato:
# - Diego Norrea, 35
# Robo con violencia
# - Demetrio Imedio, 53
# Acoso laboral
# Evasión de impuestos
# Corrupción
# - Inés Perado, 48
# Hurto
# Extorsión
# Como ves, los nombres de los delincuentes siempre empiezan por un guión y un espacio en blanco y
# terminan con una coma y su edad. A continuación aparecen los delitos cometidos uno por línea
# Tu programa debería de pedir por teclado el nombre de un sospechoso y decir si tiene o no
# antecedentes. Por ejemplo, en el caso de alguien sin antecedentes:
# Introduce el nombre del ciudadano: Ricardo Borriquero
# Sin antecedentes penales
# En el caso de tener antecedentes debería de listarlos de la siguiente forma:
# Introduce el nombre del ciudadano: Ines Perado
# Edad: 48 años
# Antecedentes penales:
# Hurto
# Extorsión
# NOTA: Piensa que no sabes cuantos antecedentes puede tener el individuo pero que si está en el
# fichero debe de tener al menos uno

class Delincuente:
    # 1. El constructor debe recibir los datos para guardarlos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.antecedentes = []

    def agregar_delito(self, delito):
        self.antecedentes.append(delito)

    def mostrar_ficha(self):
        print(f"Edad: {self.edad} años")
        print("Antecedentes penales:")
        for delito in self.antecedentes:
            print(f"- {delito}")


# --- PROGRAMA PRINCIPAL ---

lista_delincuentes = []  # Aquí guardaremos a todos los objetos cargados

try:
    with open("delincuentes.txt", "r") as fichero:  # Usamos el nombre del enunciado

        delincuente_actual = None  # Variable para recordar con quién estamos trabajando

        for linea in fichero:
            linea = linea.strip()

            # Si la línea está vacía, la saltamos
            if not linea:
                continue

            # CASO A: Es el inicio de una persona (empieza por guión)
            if linea.startswith("-"):
                # Si ya teníamos un delincuente abierto, lo guardamos en la lista antes de empezar otro
                if delincuente_actual is not None:
                    lista_delincuentes.append(delincuente_actual)

                # Procesamos la línea nueva: "- Diego Norrea, 35"
                # Quitamos el guión inicial
                datos_limpios = linea.replace("-", "").strip()
                # Separamos por la coma
                partes = datos_limpios.split(",")

                nombre = partes[0].strip()
                edad = partes[1].strip()

                # Creamos el nuevo objeto y lo dejamos "abierto" en la variable auxiliar
                delincuente_actual = Delincuente(nombre, edad)

            # CASO B: Es un delito (no empieza por guión)
            else:
                # Si tenemos un delincuente abierto, le añadimos el delito
                if delincuente_actual is not None:
                    delincuente_actual.agregar_delito(linea)

        # IMPORTANTE: Al terminar el bucle, el último delincuente se quedó sin guardar.
        # Lo añadimos ahora.
        if delincuente_actual is not None:
            lista_delincuentes.append(delincuente_actual)

    # --- BÚSQUEDA DEL USUARIO ---
    nombre_buscar = input("Introduce el nombre del ciudadano: ").strip()
    encontrado = False

    for sospechoso in lista_delincuentes:
        # Comparamos nombres (ignorando mayúsculas para ser amables con el usuario)
        if sospechoso.nombre.lower() == nombre_buscar.lower():
            sospechoso.mostrar_ficha()
            encontrado = True
            break  # Ya lo encontramos, dejamos de buscar

    if not encontrado:
        print("Sin antecedentes penales")

except FileNotFoundError:
    print("Error: No se encuentra el fichero delincuentes.txt")
except Exception as e:
    print(f"Error inesperado: {e}")
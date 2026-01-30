# ===============================
# GESTIÓN DE UN INSTITUTO
# Ejercicio sencillo de Programación Orientada a Objetos (POO)
# ===============================

# ----- CLASE ABSTRACTA PERSONA -----
from abc import ABC

class Persona(ABC):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"


# ----- CLASE ALUMNO -----
class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, ciclo, grupo):
        super().__init__(nombre, apellido)
        self.edad = edad
        self.ciclo = ciclo
        self.grupo = grupo
        # mayor_edad se calcula automáticamente según la edad
        self.mayor_edad = edad >= 18


# ----- CLASE PROFESOR -----
class Profesor(Persona):
    def __init__(self, nombre, apellido, departamento, tutor_grupo=None):
        super().__init__(nombre, apellido)
        self.departamento = departamento  # Informática, Empresa o Inglés
        self.tutor_grupo = tutor_grupo     # Puede ser None


# ----- CLASE MÓDULO -----
class Modulo:
    def __init__(self, nombre, curso, horas_semanales, optativo):
        self.nombre = nombre
        self.curso = curso  # primero o segundo
        self.horas_semanales = horas_semanales
        self.optativo = optativo


# ----- CLASE CICLO -----
class Ciclo:
    def __init__(self, nombre, grado):
        self.nombre = nombre
        self.grado = grado  # medio o superior
        self.modulos = []   # lista de módulos

    def agregar_modulo(self, modulo):
        self.modulos.append(modulo)


# ----- CLASE GRUPO -----
class Grupo:
    def __init__(self, nombre, ciclo, curso, tutor):
        self.nombre = nombre
        self.ciclo = ciclo
        self.curso = curso  # primero o segundo
        self.tutor = tutor
        self.alumnos = []   # inicialmente sin alumnos

    # Añadir alumno al grupo
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    # Eliminar alumno del grupo
    def eliminar_alumno(self, alumno):
        if alumno in self.alumnos:
            self.alumnos.remove(alumno)

    # Mostrar toda la información del grupo
    def mostrar_info(self):
        print(f"Grupo: {self.nombre}")
        print(f"Ciclo: {self.ciclo.nombre} ({self.ciclo.grado})")
        print(f"Curso: {self.curso}")
        print(f"Tutor: {self.tutor.nombre_completo()}")
        print(f"Número de alumnos: {len(self.alumnos)}")

        print("\nAlumnos:")
        for alumno in self.alumnos:
            print(f"- {alumno.nombre_completo()} | Edad: {alumno.edad}")

        print("\nMódulos del ciclo:")
        for modulo in self.ciclo.modulos:
            print(f"- {modulo.nombre} ({modulo.curso}) - {modulo.horas_semanales}h")


# ----- EJEMPLO DE USO -----

# Crear ciclo
ciclo_dam = Ciclo("Desarrollo de Aplicaciones Multiplataforma", "Superior")

# Crear módulos
m1 = Modulo("Programación", "Primero", 8, False)
m2 = Modulo("Bases de Datos", "Primero", 6, False)

# Añadir módulos al ciclo
ciclo_dam.agregar_modulo(m1)
ciclo_dam.agregar_modulo(m2)

# Crear profesor
profesor = Profesor("Ana", "García", "Informática")

# Crear grupo
grupo_dam1 = Grupo("DAM1", ciclo_dam, "Primero", profesor)

# Crear alumnos
alumno1 = Alumno("Juan", "Pérez", 19, ciclo_dam, grupo_dam1)
alumno2 = Alumno("Lucía", "López", 17, ciclo_dam, grupo_dam1)

# Añadir alumnos al grupo
grupo_dam1.agregar_alumno(alumno1)
grupo_dam1.agregar_alumno(alumno2)

# Mostrar información del grupo
grupo_dam1.mostrar_info()

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

class Alumno(Persona):
    def __init__(self):
        super().__init__()

class Profesor(Persona):
    pass
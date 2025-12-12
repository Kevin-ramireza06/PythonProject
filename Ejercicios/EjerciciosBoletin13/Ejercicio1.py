from abc import abstractmethod, ABCMeta

class Persona(metaclass=ABCMeta):
    @property
    @abstractmethod
    def nombre(self):
        pass

    @property
    @abstractmethod
    def apellido(self):
        pass

    @property
    @abstractmethod
    def grupo(self):
        pass

class Profesor(Persona):
    def __init__(self, departamento):
        super().__init__()
        if departamento in ["Iformática","Empresa" , "Inglés"]:
            self.__departamento = departamento
        else:
            raise Exception("Departamento invalido")
    pass

class Alumno(Persona):
    def __init__(self, edad, ciclo):
        super().__init__()
        self.__edad = edad
        if edad >= 18 :
            self.__mayorEdad = True
        else:
            self.__mayorEdad = False

    pass

class Ciclo:
    pass

class Grupo:
    pass

class Modulo:
    def __init__(self, nombre, anio, ):
        self.__nombre = nombre



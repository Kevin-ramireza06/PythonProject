# Crea las clases:,
# Trabajador → atributos: nombre, salario,
# Estudiante → atributos: nombre, carrera,
# Becario → hereda de Trabajador y Estudiante,
# Requisitos:,
# Becario debe inicializar correctamente todos los atributos,
# Implementa str() en cada clase para mostrar sus datos,
# Desde el programa principal:,
# Crea un becario y muestra sus datos,
#  Este ejercicio mezcla herencia múltiple + POO avanzada, típico de DAM 2.

class Trabajador:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    @property
    def nombre(self):
        return self.__nombre

    @property
    def salario(self):
        return self.__salario

    def __str__(self):
        return f"Nombre: {self.__nombre}, Salario: {self.__salario}"

class Estudiante:
    def __init__(self, nombre, carrera):
        self.__nombre = nombre
        self.__carrera = carrera

    @property
    def nombre(self):
        return self.__nombre

    @property
    def carrera(self):
        return self.__carrera

    def __str__(self):
        return f"Nombre: {self.__nombre}, Carrera: {self.carrera}"

class Becario(Trabajador, Estudiante):
    def __init__(self, nombre, salario, carrera):
        Trabajador.__init__(self,nombre, salario)
        Estudiante.__init__(self,nombre,carrera)

    def __str__(self):
        return f"Nombre: {self.nombre}, Salario: {self.salario}, Carrera: {self.carrera}"
    #Al tener herencia multiple, para acceder a los atributos privados de los padres desde el str
    #debemos ponerle los getters

becario1 = Becario("Pepe" , 10, "Artes" )
print(becario1)
# Crea las clases Profesor y Asignatura donde:,
# Un profesor puede impartir varias asignaturas,
# Una asignatura tiene un único profesor,
# Requisitos:,
# Al asignar un profesor a una asignatura, esta debe añadirse automáticamente a la lista del profesor,
# Implementa str() en ambas clases,
# Ejemplo de salida:,
# Profesor: Ana → Asignaturas: Matemáticas, Física,
# Asignatura: Matemáticas → Profesor: Ana,
# #
#  Este ejercicio es MUY típico de examen DAM 2

class Profesor:
    #Para que el constructor pueda tener unos atributos o no, les pasamos valor por default para que se hagan opcionales
    def __init__(self,nombre = "", *asignaturas ):
        self.__nombre = nombre
        self.__asignaturasQueImparte = []
        for i in asignaturas:
            self.__asignaturasQueImparte.append(i)

    @property
    def asiganturasQueImparte(self):
        return self.__asignaturasQueImparte

    @asiganturasQueImparte.setter
    def asiganturasQueImparte(self, newList):
        self.__asignaturasQueImparte = newList

    @property
    def nombre(self):
        return self.__nombre

    def agregarAsignatura(self, asignatura):
        self.__asignaturasQueImparte.append(asignatura)

    def __str__(self):
        texto = "Profesor: " + self.__nombre + " ->  "

        for i in self.__asignaturasQueImparte:
            texto += i.nombre + ", "

        return texto

class Asignatura:
    def __init__(self,nombre, profesor = None):
        self.__nombre = nombre
        self.__profesor = profesor
        if profesor != None:
            profesor.agregarAsignatura(self)

    def __str__(self):
        texto = ""
        if self.__profesor == None :
            texto = "Asignatura: " + self.__nombre
        else:
            texto = "Asignatura: " + self.__nombre + " Profesor: " + self.__profesor.nombre

        return texto

    @property
    def nombre(self):
        return self.__nombre

asignatura1 = Asignatura("Matematicas")
asignatura2 = Asignatura("Lenguaje")
profesor1 = Profesor("Ana", asignatura1, asignatura2)
asignatura3 = Asignatura("Filosofia" , profesor1)

print(profesor1)
print(asignatura1)
print(asignatura2)
print(asignatura3)

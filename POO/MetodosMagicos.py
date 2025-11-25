# ------------ Metodos "Magicos"-------------
from readline import append_history_file


class Empleado2:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    @property
    def edad(self):
        return (self.__edad)

    @property
    def nombre(self):
        return (self.__nombre)

    @property
    def apellido(self):
        return (self.__apellido)

    @edad.setter
    def edad(self, newEdad):
        self.__edad = newEdad

    def __str__(self):
        return (self.__apellido + ", " + self.__nombre)


# Los metodos que son __nombre__ son los consideraods "metodos magicos" (por lo menos pal profe) y estos en realidad son
# metodos creados para ser sobreescritos en nuestras clases, los mas usados o conocidos por nosostros son
# __str__,__len__,__count__, y llevamos usando uno tod o es te tiempo el cual es el __init__ el cual es el metodo para
# crear constructores, pero en nuestars clases lo modificamos a nuestra forma.

# Estos los podemos cambiar para que se acoplen a nuestras clases, pero siempre devuelven lo que ya tienen por defecto,
# por ejemplo sobreescribir el __str__ (el toString) nos permite modificar la forma en la que sale la informacion por
# pantalla, pero siempre debe devolver un string

empleado3 = Empleado2("Kevin", "Ramriez", 19)
print(str(empleado3))


class Cuenta: #Por terminar
    def __init__(self, titular, saldo):
        self.__titular = []
        self.__titular = self.__titular.append(titular)
        self.__saldo = saldo

    @property
    def titular(self):
        return (self.__titular)

    @property
    def saldo(self):
        return (self.__saldo)

    @titular.setter
    def titular(self, newTitular):
        self.__titular = newTitular

    @saldo.setter
    def saldo(self, newSaldo):
        self.__saldo = newSaldo

    def __add__(self, cuenta):
        self.saldo = self.saldo + cuenta.saldo
        self.titular = self.titular + cuenta.titular

        return self

cuenta1 = Cuenta("Kevin", 5000)
cuenta2 = Cuenta("Pepe",1000)

cuenta1 = cuenta1 + cuenta2

print(cuenta1)
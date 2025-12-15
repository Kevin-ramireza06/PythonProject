# Crea una clase abstracta llamada Figura usando abc que tenga:,
# Un métodito abstracto area(),
# Crea dos clases que hereden de Figura:,
# Rectangulo (base, altura),
# Circulo (radio),
# Cada una debe implementar el métodito area().,
# Desde el programa principal:,
# Crea una lista de figuras,
# Recorre la lista mostrando el área de cada una,
#  Esto es examen puro de DAM 2 (clases abstractas + polimorfismo).

from abc import abstractmethod, ABCMeta
from math import pi

class Figura(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return (self.__base)

    @base.setter
    def base(self, newBase):
        self.__base = newBase

    @property
    def altura(self):
        return (self.__altura)

    @base.setter
    def altura(self, newAltura):
        self.__altura = newAltura

    def area(self):
        return self.__base * self.__altura

class Circulo(Figura):
    def __init__(self, radio):
        self.__radio = radio

    @property
    def radio(self):
        return (self.__radio)

    @radio.setter
    def radio(self, newRadio):
        self.__radio = newRadio

    def area(self):
        return pi * (self.__radio ** 2)

figura1 = Rectangulo(10,15)
figura2 = Rectangulo(20,10)
figura3 = Rectangulo(10,15)
figura4 = Circulo(10)
figura5 = Circulo(77)

lista = [figura1,figura2,figura3,figura4,figura5]

for i in lista:
    print(i.area())

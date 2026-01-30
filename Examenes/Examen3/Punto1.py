from abc import abstractmethod, ABCMeta

class Conductor:
    def __init__(self, nif, nombre, anioNacimiento, anioCarnet, puntosCarnet):
        self._nif = nif
        self._nombre = nombre
        self._anioNacimiento = anioNacimiento
        self._anioCarnet = anioCarnet
        self._puntosCarnet = puntosCarnet

    def __str__(self):
        return f"Conductor: {self._nombre}. Edad {self._anioNacimiento - 2025}. Año de carnet: {self._anioCarnet}. Puntos{self._puntosCarnet}"

class Vehiculo(metaclass=ABCMeta):
    def __init__(self, conductor, matricula, anioCompra, seguro):
        self._conductor = conductor
        self._matricula = matricula
        self._anioCompra = anioCompra
        self._seguro = seguro

    @abstractmethod
    def calculoPrecioSeguro(self):
        pass

    def __str__(self):
        return f"Vehiculo: {self}. Matricula {self._matricula}. Año de compra: {self._anioCompra}"

class Moto(Vehiculo):
    def __init__(self, conductor, matricula, anioCompra, seguro):
        super().__init__(conductor, matricula, anioCompra, seguro)

    def calculoPrecioSeguro(self):
        calculo = 0
        if self._seguro == "Seguro a terceros":
            for i in range(0, (2025 - self._anioCompra)):
                calculo += 200

            if self._conductor._puntosCarnet < 8:
                calculo += 150

            if 2025 - self._conductor._anioNacimiento < 24:
                calculo += 25

            if 2025 - self._conductor._anioCarnet < 2:
                calculo += 50
        else:
            raise Exception("Seguro invalido")

        return calculo

class Coche(Vehiculo):
    def __init__(self, conductor, matricula, anioCompra, seguro):
        super().__init__(conductor, matricula, anioCompra, seguro)

    def calculoPrecioSeguro(self):
        calculo = 0

        if self._seguro == "Seguro a todo riesgo":
            if (2025 - self._anioCompra) == 0:
                calculo += 400
            elif (2025 - self._anioCompra) == 1:
                calculo += 500
            elif (2025 - self._anioCompra) == 2:
                calculo += 700
            elif (2025 - self._anioCompra) >= 3:
                for i in range(0, (self._anioCompra - 2025)):
                    calculo += 250

            if self._conductor._puntosCarnet < 8:
                calculo += 100
        elif self._seguro == "Seguro a terceros":
            for i in range(0, (2025 - self._anioCompra)):
                calculo += 250

            if 2025 - self._conductor._anioNacimiento < 24:
                calculo += 50

            if 2025 - self._conductor._anioCarnet < 2:
                calculo += 75
        else:
            raise Exception("Seguro invalido")

        return calculo

conductor1 = Conductor("1234567Z", "Jose Maria Morales", 1968, 2024,10)
vehiculo1 = Coche(conductor1, "6310NXB", 2024, "Seguro a todo riesgo")
vehiculo2 = Coche(conductor1, "6310NXB", 2024, "Seguro a terceros")

print(vehiculo1.calculoPrecioSeguro())
print(vehiculo2.calculoPrecioSeguro())




# Crea una clase Pedido con:,
# Atributos:,
# numero,
# estado → puede ser: "pendiente", "enviado", "entregado",
# Reglas:,
# Un pedido empieza siempre en "pendiente",
# Solo se puede pasar:,
# de "pendiente" a "enviado",
# de "enviado" a "entregado",
# Cualquier otro cambio debe lanzar una excepción,
# Métodos:,
# enviar(),
# entregar(),
# str(),
# Desde el programa principal:,
# Crea un pedido,
# Intenta entregarlo directamente (debe fallar),
# Envíalo,
# Entrégalo,
# Muestra el pedido final,
#  Esto es DAM 2 puro y duro (control de estado + excepciones).

class Pedido:
    def __init__(self, numero):
        self.__numero = numero
        self.__estado = "pendiente"


    def enviar(self):
        if self.__estado == "pendiente":
            self.__estado = "enviado"
            print("Se envio el paquete...")
        else:
            raise Exception("No se puede enviar el paquete")

    def entregar(self):
        if self.__estado == "enviado":
            self.__estado = "entregado"
            print("Se entrego el paquete")
        else:
            raise Exception("No se pudo entregar el paquete")

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, newNumero):
        self.__numero = newNumero

    @property
    def estado(self):
        return self.__estado
    #
    # @estado.setter
    # def estado(self, newEstado):
    #     if newEstado in ["pendiente", "enviado", "entregado"]:
    #         if self.__estado == "pendiente" and newEstado == "enviado":
    #             self.__estado = newEstado
    #         elif self.__estado == "enviado" and newEstado == "entregado":
    #             self.__estado = newEstado
    #         else:
    #             raise Exception("Cambio de estado invalido")
    #     else:
    #         raise Exception("Estado invalido")

    def __str__(self):
        return f"Nombre: {self.__numero}, Estado: {self.__estado}"

pedido1 = Pedido(1)
try:
    #pedido1.entregar()
    pedido1.enviar()
    pedido1.entregar()
    #pedido1.enviar()
except Exception:
    print("Algo fallo amor")



# Crea una clase Alumno con:
# nombre
# nota
# Implementa:
# str() →
# Alumno: <nombre>, Nota: <nota>
# #
# eq(self, other) → devuelve True si las notas son iguales
# lt(self, other) → compara alumnos por nota
# Desde el programa principal:
# Crea varios alumnos
# Ordénalos usando sorted()
# Muestra los alumnos ordenados
# 👉 Muy típico de examen DAM 2 (métodos mágicos + ordenación).

class Alumno:
    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, newNombre):
        self.__nombre = newNombre

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, newNota):
        self.__nota = newNota

    def __str__(self):
        return "Nombre: " + self.__nombre + ", Nota: " + str(self.__nota)
        #Para concatenar numeros en strings hay que castearlos a str

    def __eq__(self, other):
        igualdad = True
        if not self.__nota == other.nota :
            igualdad = False

        return igualdad

    def __lt__(self, other):
        respuesta = True
        if not self.__nota > other.nota :
            respuesta = False

        return respuesta

alumno1 = Alumno("Fran", 7)
alumno2 = Alumno("Marcos", 9)
alumno3 = Alumno("Kevin", 8)

lista = [alumno1,alumno2,alumno3]

listaOrdenada = sorted(lista, reverse=True)

for i in listaOrdenada:
    print(i)





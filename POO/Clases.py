
class Perro:
    #nombre = "Ricky" #En este caso yy de esta forma hacemos que el atributo nombre por defecto sea "Ricky"

    #def __init__(self, secreto, secretisimo, nombre = "Rob"): #Asi se crea un constructor en python
    #    self.nombre = nombre
    #    self._secreto = secreto
    #    self.__secretisimo = secretisimo

    numPerros = 0 #Asi hacemos un atributo de clase, solamente lo ponemos fuera del constructor

    def __init__(self, nombre="Rob" ):  # Asi se crea un constructor en python
        self.nombre = nombre
        Perro.numPerros+=1

    def llamar(self): #El self es lo mismo que el this
        return("Ricki " + self.nombre +" Bobby")

    @classmethod #Asi se define un metodo de clase
    def contarPerros(cls): #Recibe de argumento "cls" pq a este se le pasa en realidad la clase
        return(cls.numPerros)
    #Su diferencia es que desde aqui no puedo acceder a ningun metodo de instancia, solo puedo a los de clase

    @staticmethod
    def ladrar():
        return("Rapido Rapido")

    def sobrecarga(self, atributo):
        if isinstance(atributo, int):
            print("Trabajo con un numero")
        elif isinstance(atributo, float):
            print("Trabajo con un flotante")
        elif isinstance(atributo, str):
            print("Trabajo con un texto")
        elif isinstance(atributo, list):
            print("Trabajo con una lista")
        else:
            print("Trabajo con cualquier mierda")

    def sobrecarga2(self, *atributo):
        if (len(atributo) == 2):
            print("Estoy camellando con 2 parametros")
        elif (len(atributo) == 3):
            print("Estoy camellando con 3 parametros")
        elif(len(atributo) >= 4):
            print("Estoy camellando papi")

#En python to-do es publico, no hay mmanera de controlar los accesos a los metodos de otros objetos como tal


#mascota1 = Perro("Ricky") #Asi se definen llas instancias
#print(mascota1.llamar())

#mascota2 = Perro("Bobby")
#print(mascota2.llamar())

#mascota1.nombre = "Ricki" #Asi de facil se pueden modificar los valores de un objeto
#print(mascota1.llamar())

"""
mascota2 = Perro("Cuchi Cuchi", "CARIÑITO MIO", "Ricky")
print(mascota2.llamar())
mascota2._secreto = "HIjo del diablooooo"
print(mascota2._secreto)
#De esta forma no estamos cambiando el atributo privado, si no creando uno nuevo en la clase, y da la sensacion de que 
#lo estyamos cambiando
mascota2.__secretisimo = "ia puñetaaa 77"
print(mascota2.__secretisimo)

#Esta es la verdadera forma de acceder a los atributos privadps
mascota2._Perro__secretisimo = "ia puñetaaa"
print(mascota2._Perro__secretisimo)
"""

mascota1 = Perro("Ricky")
mascota2 = Perro()
mascota3 = Perro("Ricki")

print(mascota2.contarPerros())
print(mascota3.contarPerros())
print(mascota1.contarPerros())
#Aqui la clase cuenta cuantas instancias de perro tenemos

Perro.numPerros = 77

print(mascota1.contarPerros()) #En principio no deberia de poder hacer esto, si el metodo es de clase
print(Perro.contarPerros())
#Podemos modificar los atributos de clase desde fuera tambien

#EStaticos

print(mascota1.ladrar())
print(mascota3.ladrar())
print(Perro.ladrar())

#

mascota1.sobrecarga(1)
mascota1.sobrecarga(1.77)
mascota1.sobrecarga("szs")
mascota1.sobrecarga([1,2,"nonas"])

mascota1.sobrecarga2([1,2,"nonas"], 3)
mascota1.sobrecarga2([1,2,"nonas"], 4,5)
mascota1.sobrecarga2([1,2,"nonas"], 3, 5, 6, 8)


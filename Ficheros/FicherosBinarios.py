import pickle
#Se necesita la libreria pickle

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ver(self):
        print(self.nombre, "(", self.edad ,")")

p1 = Persona("Pepa", 18)
p2 = Persona("Ana", 18)
# p1.ver()
# p2.ver()


ficheroBin = open("personas.bin", "wb") #Aqui definimos si es binario, con la letra b
#pickle.dump(p1, ficheroBin)
#pickle.dump(p2, ficheroBin) #de esta forma guardamos el objeto

lista = [p1,p2]
pickle.dump(lista, ficheroBin) #Es mas comodo guardar una lista para persisitir datos
#EL metodo .dump escribe lo que le pasemos como objeto en donde le digamos, si no existe lo crea (Solo escribe objetos)
ficheroBin.close()

ficheroBin= open( "personas.bin", "rb" )
# persona = pickle.load(ficheroBin) #EL. load nos permiter recuperar el objeto
# persona2 = pickle.load(ficheroBin) al usarlo pasa al siguiente
# persona.ver()
# persona2.ver()

lista = pickle.load(ficheroBin) #AQui recuperamos la lista

for persona in lista:
    print(persona.nombre, persona.edad)

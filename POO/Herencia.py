class ClaseA:
    def __init__(self):
        self.nombre = "Clase A"

    def getNombre(self):
        return (self.nombre)
    #Para que funcione hemos tenido que usar un metodo normal, al usar los @property da errores a la hora de redefinirlos
    #en la clase hijo


class ClaseB(ClaseA): #De esta forma definimos de que clase hereda otra, de este modo se hereda absolutamente todo
    def __init__(self):
        self.nombre = "Clase B"



objetoA = ClaseA()
objetoB = ClaseB()

print(objetoA.getNombre())
print(objetoB.getNombre()) #Sale el mismo nombre que la clase padre, ya que lo heredo

#Aqui lo que pasa es que el Onjeto 2 utiliza su constructor propio, pero utiliza la funcion getNOmbre del padre

class ClaseC:
    def __init__(self):
        self.nombre = "Clase C"
        self.codigo = 77

    def cambiarNombre(self,newNombre):
        self.nombre = newNombre

class ClaseD(ClaseC):
    def __init__(self):
        super().__init__()
        #La palabra "super()" invoca al padre, y con el podemos usar sus atributos y metodos
        self.subclase = "Clase D"
    #En este caso lo que hemos hecho es usar el constructor del padre y agregarle cosas en el hijo, usando el super()

    def incrementaCodigo(self):
        self.codigo += 1



objeto3 = ClaseC()
objeto4 = ClaseD()

print(objeto3.nombre)
print(objeto4.nombre)
print(objeto4.subclase)

print("-------------------------------------")


class ClaseE:
    def __init__(self):
        self.nombre = "Clase E"
        self.codigo = 10

    def queSoy(self):
        print("Soy de la Clase E")

class ClaseF:
    def __init__(self):
        self.nombre = "Clase F"

    def queSoy(self):
        print("Soy de la Clase F")

class ClaseG(ClaseE,ClaseF): #De esta forma hacemos que una clase herede de varias clases
    #Pero este prorixara el constructor de la clase que este de prrimero como padre
    #Pero puede acceder a los metodos de todas las clases padre tranquilamente, excepto en aquellas en lass que haya conflicto
    #Se pueden tener cualquier cantidad de padres
    def queSoy(self):
        super().queSoy(self)

        print("Y ademas soy clase G")
    pass

class ClaseH(ClaseF,ClaseE):
    pass

objeto5 = ClaseE()
objeto6 = ClaseF()
objeto7 = ClaseG()
objeto8 = ClaseH()

print(objeto5.nombre)
print(objeto6.nombre)
print(objeto7.nombre)
print(objeto8.nombre)
objeto7.queSoy()



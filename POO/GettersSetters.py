class Empleado:
    pass

empleado1 = Empleado()

empleado1.nombre = "Kevin"
empleado1.apellido =  "Ramirez"
empleado1.edad = 19
empleado1.activo = True

#De esta forma se crea un registro, que es como una clase basica de toda la vida, sin metodos, se usa mucho ya que
#su sintaxis es muy comoda

class Empleado1 :
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad #Haciendo esto protegemos edad

    @property
    def edad(self): #Asi protegemos de una forma los datos, haciendo un metodo con el nombre del atrbuto, y que esta
                    #devuelva el valor deseado, pero no permitira cambiarlo de nuevo, primero protegemos el atributo con
                    #los __ y despues creamos el metodo con el nombre que queremos, y que este devuelva el atributo
        return(self.__edad) #Asi se hace un getter

    @property   #Siempre si necesitamos usar un decorador, hay que ponerlo antes de donde lo necesitamos usar, con uno
                #no funciona
    def nombre(self):
        return (self.__nombre)

    @edad.setter
    def edad(self,nuevaEdad): #Asi se crea un setter
        self.__edad = nuevaEdad

#Aqui para hacer los getters/setters se suele usa el mismo nombre del atributo, aunque como hemos visto, es practicamnte
#innesesario ya que siempre se pueden acceder a los datos

empleado2 = Empleado1("Kevin", 19)
print(empleado2.edad) #Aqui los metodos se pueden tratar como si fueran atributos

print(empleado2.nombre)

empleado2.edad = 99
print(empleado2.edad)

#empleado2.edad = 99

#DEstructores

x = 5
print(x)
del x #De esta forma eliminamos una variable por compreto
#print(x) #Al intentarla usar falla ya que no existe

del empleado1

#empleado1.activo #Generalmente los usamos en casos muy concretos, cuando necesitamos que un proyecto mejore su rendimiento





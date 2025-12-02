from abc import abstractmethod, ABCMeta


class ClaseAbstracta(metaclass=ABCMeta): #Si hacemos que herede de la clase ABCMeta, ya se porta correctamente:

    def metodoNormal(self):
        print("Holiiiiiiiiiiiii")

    @abstractmethod #COn este decorador creamos un metodo abstracto, y volvemos una clase abstracta
    def metodoAbstracto(self):
        pass
#Auque como es python, por defecto nos va a dejar crear instancias de ella y no deberia ser asi

#objetoAbstracto = ClaseAbstracta()
#Al heredaar de esa clase, ahora si no podemos usar la clase
#objetoAbstracto.metodoNormal()

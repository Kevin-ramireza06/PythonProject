import random

class Pokemon:

    def __init__(self,codigo,nombre,tipo1, tipo2 = None):
        if codigo in range(1,152):
            self.__codigo = codigo
        else:
            raise Exception("El codigo es invalido")
        self.__nombre= nombre

        if tipo1 in {"Normal", "Agua", "Fuego", "Planta", "Volador", "Lucha", "Veneno", "Eléctrico", "Tierra", "Roca", "Psíquico", "Hielo", "Bicho", "Fantasma" , "Dragón"}:
            self.__tipo1 = tipo1
        else:
            raise Exception("El primer tipo es invalido")

        if tipo2 in {"Normal", "Agua", "Fuego", "Planta", "Volador", "Lucha", "Veneno", "Eléctrico", "Tierra", "Roca", "Psíquico", "Hielo", "Bicho", "Fantasma" , "Dragón", None}:
            self.__tipo2 = tipo2
        else:
            raise Exception("El segundo tipo es invalido")

        self.__evolucion = None
        self.salud = random.randint(50,100)

    def setEvolucion(self, pokemon):
        self.__evolucion = pokemon

    def evoluciona(self):
        evo = self
        if self.__evolucion == None:
            print("El Pokemon no ha evolucionado")
        else:
            evo = self.__evolucion

        return evo

    #Getters

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def tipo1(self):
        return self.__tipo1

    @property
    def tipo2(self):
        return self.__tipo2

    @property
    def evolucion(self):
        return self.__evolucion

    def atacar(self, pokemonRival):
        daño = random.randint(0,35)
        match self.__tipo1:
            case "Normal":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Roca", "Acero"]:
                    daño *= 0.5
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) == "Fantasma":
                    daño = 0

            case "Fuego":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Planta", "Hielo", "Bicho", "Acero"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Fuego", "Agua", "Roca", "Dragon"]:
                    daño *= 0.5

            case "Agua":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Fuego", "Tierra", "Roca"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Agua", "Planta", "Dragon"]:
                    daño *= 0.5

            case "Planta":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Agua", "Tierra", "Roca"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Fuego", "Planta", "Veneno", "Volador", "Bicho", "Dragon", "Acero"]:
                    daño *= 0.5

            case "Electrico":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Agua", "Volador"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Electrico", "Planta", "Dragon"]:
                    daño *= 0.5
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) == "Tierra":
                    daño = 0

            case "Hielo":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Planta", "Tierra", "Volador", "Dragon"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Fuego", "Agua", "Hielo", "Acero"]:
                    daño *= 0.5

            case "Lucha":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Normal", "Hielo", "Roca", "Siniestro", "Acero"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Veneno", "Volador", "Psiquico", "Bicho", "Hada"]:
                    daño *= 0.5
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) == "Fantasma":
                    daño = 0

            case "Veneno":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Planta", "Hada"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Veneno", "Tierra", "Roca", "Fantasma"]:
                    daño *= 0.5
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) == "Acero":
                    daño = 0

            case "Tierra":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Fuego", "Electrico", "Veneno", "Roca", "Acero"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Planta", "Bicho"]:
                    daño *= 0.5
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) == "Volador":
                    daño = 0

            case "Volador":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Planta", "Lucha", "Bicho"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Electrico", "Roca", "Acero"]:
                    daño *= 0.5

            case "Psiquico":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Lucha", "Veneno"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Psiquico", "Acero"]:
                    daño *= 0.5
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) == "Siniestro":
                    daño = 0

            case "Bicho":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Planta", "Psiquico", "Siniestro"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Fuego", "Lucha", "Veneno", "Volador", "Fantasma", "Acero", "Hada"]:
                    daño *= 0.5

            case "Roca":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Fuego", "Hielo", "Volador", "Bicho"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Lucha", "Tierra", "Acero"]:
                    daño *= 0.5

            case "Fantasma":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Psiquico", "Fantasma"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) == "Siniestro":
                    daño *= 0.5
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) == "Normal":
                    daño = 0

            case "Dragon":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) == "Dragon":
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) == "Acero":
                    daño *= 0.5
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) == "Hada":
                    daño = 0

            case "Siniestro":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Psiquico", "Fantasma"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Lucha", "Siniestro", "Hada"]:
                    daño *= 0.5

            case "Acero":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Hielo", "Roca", "Hada"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Fuego", "Agua", "Electrico", "Acero"]:
                    daño *= 0.5

            case "Hada":
                if (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Lucha", "Dragon", "Siniestro"]:
                    daño *= 2
                elif (pokemonRival.__tipo1 or pokemonRival.__tipo2) in ["Fuego", "Veneno", "Acero"]:
                    daño *= 0.5

        pokemonRival.salud -= daño
        print(self.__nombre , "Ha atacado a", pokemonRival.__nombre , " y le quito " , daño , "de salud")
        print(pokemonRival.__nombre , "Tiene", pokemonRival.salud , "De salud")
        print("*****************")

    def combate(self, pokemonRival):
        print("--------------------------------------------------------------")
        print(self.__nombre, "Tiene" , self.salud , "Puntos de salud inical")
        print(pokemonRival.__nombre, "Tiene" , pokemonRival.salud , "Puntos de salud inical")
        print("--------------------------------------------------------------")
        print("")

        continuar = True

        mensaje = ""
        while continuar :
            self.atacar(pokemonRival)
            if pokemonRival.salud > 0:
                pokemonRival.atacar(self)
            else:
                mensaje =  "Ha ganado " + self.__nombre
                continuar = False

            if self.salud < 0:
                mensaje = "Ha ganado " + pokemonRival.__nombre
                continuar = False

        print(mensaje)

class Equipo:
    def __init__(self,codigo,nombreEquipo):
        self.__codigo = codigo


class PokemonLegendario:
    def __init__(self,codigo,nombre, tipo,nivel):
        self.__codigo = codigo




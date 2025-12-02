
personas = ["Pepe", "Pepa", "Sisas"]

iterador = iter(personas) # asi se crea un iterador, este recorre la lista, y al tocar el final suelta una excepcion

print(next(iterador)) #Cada uso del next apunta a un elemento, y avanza, empieza por fuera del bucle, y en el primer
                    #next, toca el elemento 0 y asi
print(next(iterador))
print(next(iterador))
print(next(iterador, "Ya no hay mas gente")) #EL segunbdo parametro deja mostrar un mensaje, si ya toco el final

#------------------------EJEMPLOO-----------------------------
print("-----------------------------------------------------------------")

class DiasDeLaSemana :
    def __init__(self, dia):
        self.dias = ["Lunes", "Martes" , "Miercoles" , "Jueves" , "Viernes" , "Sabado" , "Domingo"]
        self.indice = dia

    def mostrarDia(self):
        print(self.dias[self.indice])

    def __iter__(self): #De este modo redefinimos el metodo iter en nuestra clase
        return self

    #SE puede hacer el getter y seter con el atajo prop(crea el getter) o props(crea el getter y setter)

    def __next__(self): #Asi se redifine el metodo next

        diaActual = self.dias[self.indice]
        if self.indice == len(self.dias)-1 :
            self.indice = 0
        else:
            self.indice += 1
        return diaActual

dia = DiasDeLaSemana(2)
#dia.mostrarDia()

iteradorDias = iter(dia)

for i in range(0,10) :
    print(next(iteradorDias))



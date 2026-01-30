class Tarea:
    def __init__(self, titulo, prioridad, estaRealizada, diccionario):
        if type(titulo) == str:
            self._titulo = titulo
        else:
            raise Exception("titulo invalido")
        if type(prioridad) == int and prioridad in range(0,9):
            self._prioridad = prioridad
        else:
            raise Exception(" prioridad invalida")
        if type(estaRealizada) == bool:
            self._estaRealizada = estaRealizada
        else:
            raise Exception(" esta realizado invalido")

        self._diccionario = diccionario


    def __str__(self):
        return f"Tarea: {self.__titulo}"

    def agregarTarea(self, id, titulo, prioridad, diccionario):
        tarea = Tarea(titulo, prioridad, False)
        if tarea not in diccionario:
            tarea = Tarea(titulo, prioridad, False)
            diccionario[id] = tarea
            print(f"Tarea: {titulo} ({id}) añadida")
        else:
            print(f"{id} ya existe")

    def eliminarTarea(self,id):
        tarea = self.__diccionario.get(id,f"No se encontro una tarea con {id}")
        if tarea in self.__diccionario:
            self.__diccionario.remove(id)

    def marcarComoCompletada(self, id):
        tarea = self.__diccionario.get(id, f"No se encontro una tarea con {id}")
        self.__diccionario.get(id)._estaRealizada = True

    def mostrarTareasCompletadas(self, id):
        tarea = self.__diccionario.get(id, f"No se encontro una tarea con {id}")
        self.__diccionario.get(id)



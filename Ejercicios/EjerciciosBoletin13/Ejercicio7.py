# Crea un sistema de biblioteca con:
# Clases:
# Libro → atributos: titulo, autor, prestado (bool)
# Usuario → atributos: nombre, libros_prestados (lista)
# Biblioteca → mantiene listas de libros y usuarios
# Reglas:
# Métodito prestar_libro(usuario, libro):
# Solo si el libro no está prestado
# Añade el libro a usuario.libros_prestados
# Marca el libro como prestado
# Métodito devolver_libro(usuario, libro):
# Solo si el libro está prestado por ese usuario
# Quita el libro de usuario.libros_prestados
# Marca el libro como no prestado
# Métodito __str__() para cada clase mostrando su estado
# Desde el programa principal:
# Crea varios libros y usuarios
# Prueba prestar y devolver libros
# Muestra el estado final de la biblioteca y los usuarios

class Libro:
    def __init__(self, titulo, autor, prestado):
        self.__titulo = titulo
        self.__autor = autor
        if type(prestado) == bool :
            self.__prestado = prestado

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def prestado(self):
        return self.__prestado

    @titulo.setter
    def titulo(self,newTitulo):
        self.__titulo = newTitulo

    @autor.setter
    def autor(self, newAutor):
        self.__autor = newAutor

    @prestado.setter
    def prestado(self, newPrestado):
        self.__prestado = newPrestado

    def __str__(self):
        return f"Titulo: {self.__titulo}, Autor: { self.__autor}, Prestado: {self.__prestado}"

class Usuario:
        def __init__(self, nombre, libros_prestados):
            self.__nombre = nombre
            if type(libros_prestados) == list:
                self.__libros_prestados = libros_prestados
            else:
                raise Exception("Tipo de dato invalido para 'libros_prestados'")

        def recibirLibro(self, libro):
            self.libros_prestados.append(libro)

        @property
        def nombre(self):
            return self.__nombre

        @property
        def libros_prestados(self):
            return self.__libros_prestados

        @nombre.setter
        def nombre(self, newNombre):
            self.__nombre = newNombre

        @libros_prestados.setter
        def libros_prestados(self, newlibros):
            self.__libros_prestados = newlibros

        def __str__(self):
            texto = f"Nombre {self.__nombre}, Libros: "
            for i in self.__libros_prestados:
                texto += f"{i.titulo} ,"

class Biblioteca:
        def __init__(self, libros, usuarios):
            if type(libros) == list:
                self.__libros = libros
            else:
                raise Exception("Tipo de dato invalido para 'libros'")
            if type(usuarios) == list:
                self.__usuarios = usuarios
            else:
                raise Exception("Tipo de dato invalido para 'usuarios'")

        def prestar_libro(self, usuario, libro):
            if usuario in self.__usuarios and libro in self.__libros:
                if libro.prestado == False:
                    libro.prestado = True
                    usuario.recibirLibro(libro)
                else:
                    raise Exception("El libro ya esta prestado")
            else:
                raise Exception("No existe el ususario o no existe el libro")

        def devolver_libro(self, usuario, libro):
            if usuario in self.__usuarios and libro in self.__libros:
                if libro in usuario.libros_prestados :
                    usuario.libros_prestados.remove(libro)
                    libro.prestado = False
                else:
                    raise Exception("El usuario no tiene el libro")

            else:
                raise Exception("No existe el ususario o no existe el libro")
# Libros
libro1 = Libro("1984", "George Orwell", True)
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", True)
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", True)
libro4 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", False)
libro5 = Libro("La Sombra del Viento", "Carlos Ruiz Zafón", False)

lista_libros = [libro1, libro2, libro3, libro4, libro5]

# Usuarios con lista de libros prestados directamente en el constructor
usuario1 = Usuario("Ana", [libro1, libro3])  # Ana ya tiene "1984" y "El Principito"
usuario2 = Usuario("Luis", [libro2])         # Luis ya tiene "Cien Años de Soledad"
usuario3 = Usuario("María", [])              # María sin libros
usuario4 = Usuario("Carlos", [])             # Carlos sin libros

lista_usuarios = [usuario1, usuario2, usuario3, usuario4]

# Biblioteca
biblioteca = Biblioteca(lista_libros, lista_usuarios)

# Prestar libros
#biblioteca.prestar_libro(usuario1, libro1)  # Ana toma "1984"
#biblioteca.prestar_libro(usuario2, libro2)  # Luis toma "Cien Años de Soledad"
#biblioteca.prestar_libro(usuario1, libro3)  # Ana toma "El Principito"
biblioteca.prestar_libro(usuario1, libro4)  # Ana toma "El Principito"


# Intentar prestar un libro ya prestado
#biblioteca.prestar_libro(usuario3, libro1)  # María intenta "1984", debería fallar

# Devolver libros
biblioteca.devolver_libro(usuario1, libro1)  # Ana devuelve "1984"

# Intentar devolver libro que no tiene
#biblioteca.devolver_libro(usuario3, libro2)  # María intenta devolver "Cien Años de Soledad", debería fallar

# Prestar nuevamente
biblioteca.prestar_libro(usuario3, libro1)  # María toma "1984" ahora que está disponible








class Manga:

    def __init__(self, mangaka,tituloColeccionJapones,generoPrincipal,numeroPublicado ):
        generos = {"shonen", "shojo", "seinen", "josei", "kodomo", "yuri", "spokon", "isekai", "hentai"}

        self.__mangaka = mangaka
        self.__tituloColeccionJapones = tituloColeccionJapones

        self.__tituloColeccionEspañol = None

        if generoPrincipal in generos:
            self.__generoPrincipal = generoPrincipal
        else:
            raise Exception("El genero principal no es valido")

        self.__numeroPublicado = numeroPublicado

        @property
        def mangaka(self):
            return self.__mangaka

        @property
        def tituloColeccionJapones(self):
            return self.__tituloColeccionJapones

        @property
        def generoPrincipal(self):
            return self.__generoPrincipal

        @property
        def numeroPublicado(self):
            return self.__numeroPublicado

        def setTitulo





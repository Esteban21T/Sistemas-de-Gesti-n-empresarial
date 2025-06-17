class Libro:
    def __init__(self, titulo, autor, genero, anio):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anio = anio

    def to_dict(self):
        return {
            "titulo": self.__titulo,
            "autor": self.__autor,
            "genero": self.__genero,
            "anio": self.__anio
        }

    def __str__(self):
        return f"{self.__titulo} - {self.__autor} ({self.__anio}) [{self.__genero}]"

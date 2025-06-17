from libro import Libro
from almacenamiento import ArchivoJSON

class GestorLibros:
    def __init__(self, ruta_archivo):
        self.ruta = ruta_archivo
        self.libros = []
        self.cargar_libros()

    def registrar_libro(self, titulo, autor, genero, anio):
        nuevo_libro = Libro(titulo, autor, genero, anio)
        self.libros.append(nuevo_libro)
        self.guardar_libros()

    def buscar(self, criterio, valor):
        resultados = []
        for libro in self.libros:
            if getattr(libro, f"_Libro__{criterio}").lower() == valor.lower():
                resultados.append(libro)
        return resultados

    def mostrar_catalogo(self):
        if not self.libros:
            print("Catálogo vacío.")
        for libro in self.libros:
            print(libro)

    def guardar_libros(self):
        ArchivoJSON.guardar(self.ruta, [libro.to_dict() for libro in self.libros])

    def cargar_libros(self):
        try:
            datos = ArchivoJSON.cargar(self.ruta)
            self.libros = [Libro(**d) for d in datos]
        except Exception as e:
            print(f"Error al cargar libros: {e}")

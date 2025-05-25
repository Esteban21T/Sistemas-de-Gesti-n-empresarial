def registrar_libro(libros):
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    anio = input("Año de publicación: ")
    nuevo = {"titulo": titulo, "autor": autor, "genero": genero, "anio": anio}
    return libros + [nuevo]

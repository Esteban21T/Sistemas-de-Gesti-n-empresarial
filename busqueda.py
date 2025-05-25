def buscar_por_titulo(libros):
    titulo = input("Ingrese el título: ")
    resultados = list(filter(lambda x: titulo.lower() in x['titulo'].lower(), libros))
    imprimir_resultados(resultados)

def buscar_por_autor(libros):
    autor = input("Ingrese el autor: ")
    resultados = list(filter(lambda x: autor.lower() in x['autor'].lower(), libros))
    imprimir_resultados(resultados)

def buscar_por_genero(libros):
    genero = input("Ingrese el género: ")
    resultados = list(filter(lambda x: genero.lower() in x['genero'].lower(), libros))
    imprimir_resultados(resultados)

def imprimir_resultados(resultados):
    if resultados:
        for libro in resultados:
            print(libro)
    else:
        print("No se encontraron resultados.")

import json

def cargar_datos():
    try:
        with open("datos_libros.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def guardar_datos(libros):
    with open("datos_libros.json", "w") as archivo:
        json.dump(libros, archivo, indent=4)

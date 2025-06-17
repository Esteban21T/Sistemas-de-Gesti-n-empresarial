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

import json

class ArchivoJSON:
    @staticmethod
    def guardar(ruta, datos):
        try:
            with open(ruta, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=4)
        except IOError as e:
            print(f"Error al guardar archivo: {e}")

    @staticmethod
    def cargar(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error al leer el archivo JSON.")
            return []

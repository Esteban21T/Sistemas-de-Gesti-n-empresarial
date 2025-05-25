from registro import registrar_libro
from busqueda import buscar_por_titulo, buscar_por_autor, buscar_por_genero
from visualizacion import mostrar_libros
from almacenamiento import cargar_datos, guardar_datos

def menu():
    libros = cargar_datos()
    while True:
        print("\n--- Menú ---")
        print("1. Registrar libro")
        print("2. Buscar por título")
        print("3. Buscar por autor")
        print("4. Buscar por género")
        print("5. Mostrar catálogo")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            libros = registrar_libro(libros)
        elif opcion == '2':
            buscar_por_titulo(libros)
        elif opcion == '3':
            buscar_por_autor(libros)
        elif opcion == '4':
            buscar_por_genero(libros)
        elif opcion == '5':
            mostrar_libros(libros)
        elif opcion == '6':
            guardar_datos(libros)
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()

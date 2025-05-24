
from utilidades import registrar_huesped, crear_reserva, mostrar_reservas, mostrar_huespedes
#Creamos la función para crear el menú y dentro de cada opción llamamos a las debidas funciones del archivo utilidades.py
def menu_principal():
    while True:
        print("Menú de opciones para reservas de hotel")
        print("1. Registrar nuevo huésped")
        print("2. Crear una reserva")
        print("3. Mostrar todas las reservas")
        print("4. Mostrar todos los huéspedes")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "1":
            registrar_huesped()
        elif opcion == "2":
            crear_reserva()
        elif opcion == "3":
            mostrar_reservas()
        elif opcion == "4":
            mostrar_huespedes()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    menu_principal()

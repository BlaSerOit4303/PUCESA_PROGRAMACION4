#Importar las métodos o funciones necesarias desde el módulo funciones
from funciones import registrar_paciente, mostrar_pacientes, registrar_consulta, mostrar_historial_paciente

#Funcion menú
def menu():
    #While para mostrar el menú de opciones y evitar que se cierre el programa
    while True:
        print("Menú de opciones para consultas médicas")
        print("1. Registrar nuevo paciente")
        print("2. Registrar una consulta médica a un paciente existente ")
        print("3. Mostrar los datos de un paciente y su historial de consultas")
        print("4. Mostrar los pacientes registrados")
        print("5.Salir ")
        opcion= input("Seleccione una opción (1-5): ")
        #Menú de opciones creado con ifs y elifs
        if opcion == "1":
            print("\t\t\t\tUsted eligió la opción 1")
            print("1. Registrar nuevo paciente")
            #Llamar a la función desde el módulo de funciones
            registrar_paciente()
        elif opcion == "2":
            print("\t\t\t\tUsted eligió la opción 2")
            print("2. Registrar una consulta médica a un paciente existente ")
            #Llamar a la función desde el módulo de funciones
            registrar_consulta()
        elif opcion == "3":
            print("\t\t\t\tUsted eligió la opción 3")
            print("3. Mostrar los datos de un paciente y su historial de consultas ")
            #Llamar a la función desde el módulo de funciones
            mostrar_historial_paciente()
        elif opcion == "4":
            print("\t\t\t\tUsted eligió la opción 4")
            print("4. Mostrar los pacientes registrados")
            #Llamar a la función desde el módulo de funciones
            mostrar_pacientes()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

#Esta parte del código se ejecuta solo si el archivo se ejecuta directamente desde el main  
if __name__ == "__main__":
    menu()
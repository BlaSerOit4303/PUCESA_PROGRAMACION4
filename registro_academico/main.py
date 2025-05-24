from herramientas import registrar_estudiante,mostrar_todos,mostrar_estudiante, agregar_nota_estudiante
def menu():
    while True:
        print("\t\t\t\tMenú de registro académico")
        print("1. Registrar estudiante.")
        print("2. Asignar calificación por materia a un estudiante")
        print("3. Mostrar información completa del estudiante")
        print("4. Mostrar todos los estudiantes registrados.")
        print("5. Salir del programa.")
        opcion= input("Ingrese la opción deseada: ")
        if opcion == "1":
            print("\t\t\tUsted eligió la opción Registrar estudiante\n")
            registrar_estudiante()
        elif opcion =="2":
            print("\t\t\tUsted eligió la opción Asignar calificación por materia\n")
            agregar_nota_estudiante()

        elif opcion =="3":
            print("\t\t\tUsted eligió la opción Mostrar Información completa del estudiante\n")
            mostrar_estudiante()
        elif opcion =="4":
            print("\t\t\tUsted eligió la opción Mostrar todos los estudiantes registrados\n")
            
            mostrar_todos()
        elif opcion =="5":
            print("Gracias por usar el programa...\n")
            break
        else:
            print("Opción inválida ingrese una opción correcta del 1-5\n")
#Esta parte del código se ejecuta solo si el archivo se ejecuta directamente desde el main  
if __name__ == "__main__":
    menu()
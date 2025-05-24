from estudiante import Estudiante
from calificacion import Calificacion

# Lista global para guardar estudiantes
estudiantes = []
calificaciones= []

def registrar_estudiante():
    while True:
        matricula = input("Matrícula: ")
        # Recorrer la lista de estudiantes para verificar si la matrícula ya existe
        repetida = False
        for est in estudiantes:
            if est.matricula == matricula:
                print("La matrícula ya está registrada. Intente con otra.\n")
                repetida = True
                break  # Salimos del ciclo si encontramos la matrícula repetida
        if not repetida:
            break  # Si la matrícula es válida, salimos del bucle

    nombre = input("Nombre del estudiante: ")
    carrera = input("Carrera: ")
    # Crear y agregar el estudiante a la lista
    estudiante = Estudiante(nombre, matricula, carrera)
    estudiantes.append(estudiante)
    print("Estudiante registrado con éxito.\n")


def buscar_estudiante(matricula):
    for est in estudiantes:
        if est.matricula == matricula:
            return est
    return None

#Función para mostrar estudiante, primero usamos la función buscar estudiante para verificar que si existe o está registrado.
def mostrar_estudiante():
    matricula = input("Ingrese la matrícula del estudiante a buscar: ")
    estudiante = buscar_estudiante(matricula)
    #Si existe el estudiante vamos a mostrar todos los datos del mismo.
    if estudiante:
        print("\nNombre: ",estudiante.nombre)
        print("Matrícula: ", estudiante.matricula)
        print("Carrera: ",estudiante.carrera)
        print("Calificaciones:")
        notas_estudiante = [c for c in calificaciones if c.matricula == estudiante.matricula]  
        if notas_estudiante:
            for calificacion in notas_estudiante:
                print("-",calificacion.mostrar_calificacion())
        else:
            print("No tiene calificaciones registradas.")
    else:
        print("Estudiante no encontrado.\n")

#Función para agregar notas del estudiante, antes de llegar al if y agregar, usamos la otra función buscar estudiante para verificar si también existe o no 
def agregar_nota_estudiante():
    matricula = input("Ingrese la matrícula del estudiante: ")
    estudiante = buscar_estudiante(matricula)
    if estudiante:
        materia = input("Ingrese la materia: ")
        while True:
            try:
                nota = input("Ingrese la nota (0-50): ").replace(",", ".")  # Reemplazamos coma por punto si es necesario
                nota = float(nota)  # Convertimos a flotante
                if 0 <= nota <= 50:  # Validamos el rango
                    nueva_calificacion = Calificacion(matricula, materia, nota)
                    calificaciones.append(nueva_calificacion)
                    print("Calificación agregada con éxito.\n")
                    break  # Salimos del bucle una vez ingresada correctamente
                else:
                    print("La nota debe estar entre 0 y 50.\n")
            except ValueError:
                print("Nota inválida. Debe ser un número. Ejemplo válido: 85.5\n")
    else:
        print("Estudiante no encontrado.\n")

#FUnción que muestra todos los estudiantes y valida si existe o no alguno registrado
def mostrar_todos():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
    for est in estudiantes:
        est.mostrar_datos()
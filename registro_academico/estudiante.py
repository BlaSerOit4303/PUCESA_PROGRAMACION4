from calificacion import Calificacion

class Estudiante:
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.calificaciones = []  # Lista de calificaciones

#Función para agregar calificaciones, usamos .append para agregarlos a la lista 
    def agregar_calificacion(self, materia, nota):
        nueva_calificacion = Calificacion(materia, nota)
        self.calificaciones.append(nueva_calificacion)
        
#Función para mostrar todos los datos del estudiante, incluyendo las calificaciones
    def mostrar_datos(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Matrícula: {self.matricula}")
        print(f"Carrera: {self.carrera}")
        print("Calificaciones:")
        if self.calificaciones:
            for calificacion in self.calificaciones:
                print(f"- {calificacion.mostrar_calificacion()}")
        else:
            print("No tiene calificaciones registradas.\n")
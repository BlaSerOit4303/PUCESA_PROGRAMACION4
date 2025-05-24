class Calificacion:
    
    def __init__(self, matricula, materia, nota):  
        self.matricula = matricula  
        self.materia = materia
        self.nota = nota
#Creamos la función mostrar calificación la cual nos ayuda a visualizar y complementar las otras funciones usando esta.
    def mostrar_calificacion(self):
        return f"Materia: {self.materia}, Nota: {self.nota}"

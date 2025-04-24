class Persona:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        return f"Hola me llamo, {self.nombre} y tengo {self.edad} años"
    
persona1= Persona("Juan", 30)
persona2= Persona("Maria", 25)


class Estudiante(Persona):
    
    def _init_(self, nombre, edad, carrera): #Contructor de la clase hija
        super()._init_(nombre, edad) #Llama al contructor de la clase padre
        
        self.carrear = carrera
        
    def datos_completos(self):
        return f"{self.saludar()} y estudio {self.carrear}"
    
persona3 = Estudiante("Carlos",26, "Sistemas")

print(persona3.datos_completos())
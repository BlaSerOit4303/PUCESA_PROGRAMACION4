
class Huesped:
    def __init__(self, nombre, cedula, correo):
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Cédula:", self.cedula)
        print("Correo:", self.correo)
        print("\n")


class Reserva:
    def __init__(self, huesped, fecha_entrada, fecha_salida, tipo_habitacion):
        self.huesped = huesped
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.tipo_habitacion = tipo_habitacion

    def mostrar_reserva(self):
        print("Reserva de:", self.huesped.nombre)
        print("Cédula:", self.huesped.cedula)
        print("Correo:", self.huesped.correo)
        print("Fecha de entrada:", self.fecha_entrada.strftime("%d/%m/%Y"))
        print("Fecha de salida:", self.fecha_salida.strftime("%d/%m/%Y"))
        print("Tipo de habitación:", self.tipo_habitacion)
        print("---------------------------------------------------\n")
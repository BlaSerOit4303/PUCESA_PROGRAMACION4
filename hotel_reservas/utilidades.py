#Importamos la librería  datetime para controlar los formatos de fecha
from datetime import datetime
from huesped import Huesped
from reserva import Reserva

huespedes = {}
reservas = []
#Función para validar cédulas tanto que sea dígitos y no letras, como también cumpla los 10 dígitos
def validar_cedula(cedula):
    return cedula.isdigit() and len(cedula) == 10

#Función para pedir cédula y dentro de ella llamamos a otra función llamada validar_cédula la cual podemos usar en otras partes y usar modularización
def pedir_cedula():
    while True:
        cedula = input("Ingrese la cédula (10 dígitos): ")
        if validar_cedula(cedula):
            return cedula
        else:
            print("Error: La cédula debe tener 10 dígitos numéricos.")
#Función para verificar si la fecha tiene como formato el Día/Mes/Año
def pedir_fecha(mensaje):
    while True:
        fecha_str = input(mensaje)
        try:
            #Usamos el strptime para verificar si cumple el formato, la variable fecha_str es la que ingresa con imput mensaje, el mensaje viene de la función 
            # crear_reserva , ingresa por texto de las variables fecha_entrada, fecha_salida para validar
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("Error: Ingrese la fecha en formato DD/MM/AAAA.\n")
            
#Función para registrar los huéspedes, estos elementos almacenamos en huespedes{}
def registrar_huesped():
    print("\nRegistrar nuevo huésped")
    nombre = input("Nombre completo: ")
    cedula = pedir_cedula()
    correo = input("Correo electrónico: ")
    #Validamos que la cédula ingresada no esté ya registrada en el diccionario huespedes{}
    if cedula in huespedes:
        print("Ya existe un huésped con esa cédula.\n")
    else:
        nuevo = Huesped(nombre, cedula, correo)
        huespedes[cedula] = nuevo
        print(" Huésped registrado correctamente.\n")
        
#Función usada para crear reservas, tiene validación de cédula llamando a otra función en este archivo llamada validar_cedula, tiene ingreso de fechas y 
# validación usando la librería date.time y darle formato
def crear_reserva():
    print("\n Crear nueva reserva")
    cedula = pedir_cedula()
    if cedula not in huespedes:
        print("No hay huésped con esa cédula. Regístrelo primero.\n")
        return
    fecha_entrada = pedir_fecha("Fecha de entrada (DD/MM/AAAA): ")
    fecha_salida = pedir_fecha("Fecha de salida (DD/MM/AAAA): ")
    if fecha_salida <= fecha_entrada:
        print("Error: La fecha de salida debe ser posterior a la de entrada.")
        return
    tipo = input("Tipo de habitación (Simple / Doble / Suite): ")
    nueva = Reserva(huespedes[cedula], fecha_entrada, fecha_salida, tipo)
    reservas.append(nueva)
    print("Reserva creada correctamente.\n ")

#Mostrar los datos del huésped, usando un for y variable h para recorrer los huespedes, llamando a la función mostrar_información que está en el archivo huesped.py
def mostrar_huespedes():
    print("\nLista de huéspedes:")
    if not huespedes:
        print("No hay huéspedes registrados.\n")
    else:
        for h in huespedes.values():
            print("------------------")
            h.mostrar_informacion()

#Función mostrar reserva que usamos for y la variable r para recorrer todas las reservas que estén guardadas, usamos la función mostrar_reserva que está en el archivo reserva.py
def mostrar_reservas():
    print("\nLista de reservas:")
    if not reservas:
        print("No hay reservas registradas.\n")
    else:
        for r in reservas:
            
            r.mostrar_reserva()

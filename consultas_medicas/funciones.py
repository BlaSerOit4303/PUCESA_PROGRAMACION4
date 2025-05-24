#Importamos la clase paciente desde el archivo para usar las funciones de la clase
from paciente import paciente
#Importamos la librería datetime para validar la fecha de la consulta y dar formato
from datetime import datetime
#Creamos la lista vacía para guardar los pacientes registrados
pacientes = []	
#Función para registrar un nuevo paciente
def registrar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    while True:
        cedula = input("Ingrese el número de cédula (10 dígitos): ")
        try:
            # Validar si tiene solo números
            int(cedula)  
            # Validar si tiene 10 dígitos
            if len(cedula) != 10:
                print("La cédula debe tener exactamente 10 dígitos.")
                continue
            # Validar si ya existe
            repetida = False
            #Recorremos la lista de pacientes para ver si ya existe
            for p in pacientes:
                if p.cedula == cedula:
                    repetida = True
                    break
            if repetida == True:
                print("Ya existe un paciente con esta cédula.")
                continue
            break  # Todo correcto, sale del while
        except ValueError:
            print("La cédula debe contener solo números.")
            
    #ciclo para validar el tipo de sangre
    while True:
        #Usamos Try y except para validar los tipos de valores sean correctos y no se cuelgue el programa si ingresan mal
        try:
            #Mostrar tipos de sangre en numeros para hacer fácil la selección
            print("Tipos de sangre:")
            print("1. O+")
            print("2. O-")
            print("3. A+")
            print("4. A-")
            print("5. B+")
            print("6. B-")
            print("7. AB+")
            print("8. AB-")

            tipo_sangre = int(input("Ingrese el tipo de sangre: "))
            # Validar si el tipo de sangre es válido (1-8) 
            if tipo_sangre < 1 or tipo_sangre > 8:
                print("Tipo de sangre no válido. Debe ser un número entre 1 y 8.")
                continue
            # Asignar el tipo de sangre correspondiente
            if tipo_sangre == 1:
                tipo_sangre = "O+"
            elif tipo_sangre == 2:
                tipo_sangre = "O-"
            elif tipo_sangre == 3:
                tipo_sangre = "A+"
            elif tipo_sangre == 4:
                tipo_sangre = "A-"
            elif tipo_sangre == 5:
                tipo_sangre = "B+"
            elif tipo_sangre == 6:
                tipo_sangre = "B-"
            elif tipo_sangre == 7:
                tipo_sangre = "AB+"
            elif tipo_sangre == 8:
                tipo_sangre = "AB-"
            break  #  Todo correcto, sale del while
        except ValueError:
            print("Por favor ingrese un número válido para el tipo de sangre.")
            
    #Ciclo para validar edad
    while True:
        #Usamos otra vez Try y Except para evitar valores no válidos
        try:
            edad = int(input("Ingrese la edad del paciente: "))
            #Controlamos que ingresen números entre 1 y 120, teniendo en cuenta que edad no es negativa o 0 años, y el más longevo creo tiene 120 años
            if edad >=1 and edad <= 120:
                print("Edad válida.")
                break
            else:
                print("La edad debe estar entre 1 y 120 años.")
        except ValueError:
            print("Por favor ingrese un número válido para la edad.")
    
    #Creamos la variable new_paciente y le asignamos la clase paciente con los datos ingresados anteriormente por el usuario
    new_paciente = paciente(nombre, apellido, edad,cedula, tipo_sangre)
    #usamos .append para agregar el nuevo paciente a la lista pacientes
    pacientes.append(new_paciente)
    print("Paciente registrado con éxito.\n")

#Función para mostrar todos los pacientes registrados
def mostrar_pacientes():
    #Controlamos si no hay pacientes muestre mensaje, si no, mostramos todos los pacientes registrados usando el método mostrar_datos de la clase paciente
    if not pacientes:
        print("No hay pacientes registrados.")
        print("---------------------------------------------------------------\n\n")
    else:
        print("Pacientes registrados:")
        for p in pacientes:
            p.mostrar_datos()
        
#Función para registrar una consulta médica a un paciente existente
def registrar_consulta():
    while True:
        cedula = input("Ingrese el número de cédula (10 dígitos): ")
        #Aquí usamos el mismo formato para validar la cédula que usamos en la función registrar_paciente
        try:
            # Validar si tiene solo números
            int(cedula)  
            # Validar si tiene 10 dígitos
            if len(cedula) != 10:
                print("La cédula debe tener exactamente 10 dígitos.")
                continue
            for p in pacientes:
                if p.cedula == cedula:
                    print(f"Paciente encontrado: {p.nombre} {p.apellido}")
                    # Validar si la fecha es válida
                    while True:
                        try:
                            #Validar formato de fecha
                            fecha = input("Ingrese la fecha de la consulta (Día/Mes/Año): ")
                            datetime.strptime(fecha, "%d/%m/%Y")
                            break #Si la fecha es válida, salimos del while
                        except ValueError:
                            print("Fecha no válida, Use el formato Día/Mes/Año")
                            continue
                    #Solicitamos los datos de la consulta al usuario
                    diagnostico = input("Ingrese la nota de la consulta: ")
                    tratamiento = input("Ingrese el tratamiento: ")
                    #Llamamos al método agregar_consulta de la clase paciente para agregar la consulta a la lista de consultas del paciente
                    p.agregar_consulta(fecha, diagnostico, tratamiento)
                    print("Consulta registrada con éxito.\n")
                    return
            print("Paciente no existe o no encontrado.\n")
            break #salimos del while si no encuentra el paciente 
        except ValueError:
            print("La cédula debe contener solo números.")

#Llamamos a la función mostrar_historial_paciente
def mostrar_historial_paciente():
    cedula = input("Ingrese la cédula del paciente: ")
    #recorremos una variable P en la lista pacientes 
    for p in pacientes:
        #Usamos un if para preguntar a la variable P que recorre en la lista pacientes para verificar si el valor cedula es igual o existe
        if p.cedula == cedula:
            #Si existe entonces llamamos a las funciones mostrar_datos y mostrar_consultas e imprimir en un solo bloque
            p.mostrar_datos()
            p.mostrar_consultas()
            print("---------------------------------------------------------------\n")
            return
    print("Paciente no existe o no encontrado.\n")
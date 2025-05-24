class paciente:
    def __init__(self, nombre, apellido, edad, cedula, tipo_sangre):
        # Inicialización de atributos
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad
        self.tipo_sangre = tipo_sangre
        self.consultas = []  # Lista vacía para guardar consultas
        
    #Función para agregar una consulta
    def agregar_consulta(self, fecha, diagnostico, tratamiento):
        # Agrega un diccionario con los datos de una consulta
        consulta = {
            'fecha': fecha,
            'diagnostico': diagnostico,
            'tratamiento': tratamiento
        }
        self.consultas.append(consulta)
    #Función para mostrar el historial de consultas
    def mostrar_consultas(self):
        if not self.consultas:
            print("No hay consultas registradas para este paciente.")
        else:
            print(f"Historial de Consultas de {self.nombre} {self.apellido}:")
            #Contador para mostrar el número de la consulta
            contador = 1
            #For para recorrer la lista de consultas
            for  consulta in self.consultas:
                print(f"\nConsulta #{contador}:")
                print(f"  Fecha: {consulta['fecha']}")
                print(f"  Diagnóstico: {consulta['diagnostico']}")
                print(f"  Tratamiento: {consulta['tratamiento']}")
                #Aumentar el contador para la siguiente consulta
                contador+=1
                
    #Función para mostrar los datos del paciente            
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Cedula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de sangre: {self.tipo_sangre}")
        print("-------------------------------------------------")
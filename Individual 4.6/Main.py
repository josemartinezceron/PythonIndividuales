""" la solución presentada es una aplicación para toma de citas para un centro de terapias"""
import csv
import os


class Cita:
    def __init__(self, fecha, hora, paciente):
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.reservada = False
    
    def reservar(self):
        # Lógica para reservar la cita
        if self.reservada:
            print("La cita ya está reservada.")
        else:
            self.reservada = True
            print(f"Cita reservada para el paciente {self.paciente} el {self.fecha} a las {self.hora}.")
    
    def cancelar(self):
        # Lógica para cancelar la cita
        if self.reservada == False:
            print("La cita no se puede cancelar porque aún no ha sido reservada.")
        else:
            self.reservada = False
            print(f"Cita cancelada para el paciente {self.paciente} el {self.fecha} a las {self.hora}.")
    
    def modificar(self, fecha, hora):
        self.fecha=fecha
        self.hora=hora
        # Lógica para modificar la cita
    
    def obtener_informacion(self):
        print(f"La cita está programada para el día {self.fecha} a las {self.hora}. ")
        # Lógica para obtener información de la cita

class CitaMedicoGeneral(Cita):
    def __init__(self, fecha, hora, paciente, medico):
        super().__init__(fecha, hora, paciente)
        self.medico = medico
    
    def obtener_informacion(self):
        # Lógica para obtener información de la cita con médico general
        print(f"La cita con el médico general {self.medico} está programada para el día {self.fecha} a las {self.hora}. ")
    
    def cancelar(self):
        super().cancelar()
        

class CitaOdontologica(Cita):
    def __init__(self, fecha, hora, paciente, odontologo):
        super().__init__(fecha, hora, paciente)
        self.odontologo = odontologo
    
    def obtener_informacion(self):
        print(f"La cita con el Odontólogo {self.odontologo} está programada para el día {self.fecha} a las {self.hora}. ")
        # Lógica para obtener información de la cita odontológica

class CitaGinecologica(Cita):
    def __init__(self, fecha, hora, paciente, ginecologo):
        super().__init__(fecha, hora, paciente)
        self.ginecologo = ginecologo
    
    def obtener_informacion(self):
        print(f"La cita con el Ginecólogo {self.ginecologo} está programada para el día {self.fecha} a las {self.hora}. ")
        # Lógica para obtener información de la cita ginecológica

class CitaManager(): 
    def __init__(self):
        self.citas = []
        self.cargar_citas()
        self.opciones = [
            ("Reservar cita con Médico general", self.reservar_cita_medico_general),
            ("Reservar cita Odontológica", self.reservar_cita_odontologica),
            ("Reservar cita Ginecológica", self.reservar_cita_ginecologica),
            ("Cancelar cita con médico general", self.cancelar_cita_medico_general),
            ("Cancelar cita Odontológica", self.cancelar_cita_odontologica),
            ("Cancelar cita Ginecológica", self.cancelar_cita_ginecologica),
            ("Ver lista de citas", self.ver_lista_citas),
            ("Salir", None)
        ]

    def cargar_citas(self):
        citas = []  
        
        try:
            with open("citas.csv", "r") as archivo:
                lector = csv.DictReader(archivo)
                citas_dict = list(lector)
            cita = None  
            for cita_dict in citas_dict:
                tipo_cita = cita_dict.pop("tipo")
                if tipo_cita == "medico_general":
                    cita = CitaMedicoGeneral(**cita_dict)
                elif tipo_cita == "odontologica":
                    cita = CitaOdontologica(**cita_dict)
                elif tipo_cita == "ginecologica":
                    cita = CitaGinecologica(**cita_dict)
                self.citas.append(cita)
            print(f"Citas cargadas: {self.citas}") 
        except FileNotFoundError:
            pass  
        
        return citas  

    def guardar_citas(self):
        citas_dict = []
        for cita in self.citas:
            cita_dict = cita.__dict__
            cita_dict["tipo"] = type(cita).__name__.lower()
            citas_dict.append(cita_dict)
        with open("citas.csv", "w") as archivo:
            campos = ["tipo", "fecha", "hora", "paciente", "medico", "odontologo", "ginecologo", "reservada"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(citas_dict)
    
    def ver_lista_citas(self):
        for cita in self.citas:
            cita.obtener_informacion()1
    
    def reservar_cita_medico_general(self):
        paciente = input("Ingrese el nombre del paciente: ")
        fecha = input("Ingrese la fecha (formato dd/mm/aaaa): ")
        hora = input("Ingrese la hora (formato hh:mm): ")
        medico = input("Ingrese el nombre del médico: ")
        cita = CitaMedicoGeneral(fecha, hora, paciente, medico)
        cita.reservar()
        self.citas.append(cita)
        self.guardar_citas()
    
    def reservar_cita_odontologica(self):
        fecha = input("Ingrese la fecha de la cita (DD/MM/AAAA): ")
        hora = input("Ingrese la hora de la cita (HH:MM): ")
        paciente = input("Ingrese el nombre del paciente: ")
        odontologo = input("Ingrese el nombre del médico general: ")
        cita = CitaOdontologica(fecha, hora, paciente, odontologo)
        cita.reservar()
        self.citas.append(cita)
        self.guardar_citas()
    
    def reservar_cita_ginecologica(self):
        fecha = input("Ingrese la fecha de la cita (DD/MM/AAAA): ")
        hora = input("Ingrese la hora de la cita (HH:MM): ")
        paciente = input("Ingrese el nombre del paciente: ")
        ginecologo = input("Ingrese el nombre del médico general: ")
        cita = CitaGinecologica(fecha, hora, paciente, ginecologo)
        cita.reservar()
        self.citas.append(cita)
        self.guardar_citas()

    # Los tres metodos que siguen tiene el manejo de error try - except
    
    def cancelar_cita_medico_general(self):
         # Pedir el nombre del paciente
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        
        # Buscar las citas asociadas con el paciente
        citas_paciente = []
        for cita in self.citas:
            if isinstance(cita, CitaMedicoGeneral) and cita.paciente == nombre_paciente:

                citas_paciente.append(cita)
        
        # Mostrar las citas y solicitar la selección del usuario
        if len(citas_paciente) == 0:
            print("No se encontraron citas asociadas con ese paciente.")
            return
        
        print(f"Citas para {nombre_paciente}:")
        for i, cita in enumerate(citas_paciente):
            print(f"{i+1}. Fecha: {cita.fecha}, Hora: {cita.hora}, Doctor: {cita.medico}")
        
        seleccion = input("Seleccione el número de la cita que desea eliminar: ")
        try:
            seleccion = int(seleccion)
        except ValueError:
            print("La selección debe ser un número.")
            return
        
        if seleccion < 1 or seleccion > len(citas_paciente):
            print("Selección inválida.")
            return
        
        # Eliminar la cita seleccionada
        cita_seleccionada = citas_paciente[seleccion-1]
        self.citas.remove(cita_seleccionada)
        
        print("Cita eliminada exitosamente.") 

    def cancelar_cita_odontologica(self):
        try:
            if self.cita is None:
                print("No hay citas reservadas.")
            elif isinstance(self.cita, CitaOdontologica):
                self.cita.cancelar()
                self.cita = None
            else:
                print("La cita no es una cita con Odontólogo.")
        except Exception as e:
            print(f"Error al cancelar la cita: {e}")
    
    def cancelar_cita_ginecologica(self):
        try:
            if self.cita is None:
                print("No hay citas reservadas.")
            elif isinstance(self.cita, CitaGinecologica):
                self.cita.cancelar()
                self.cita = None
            else:
                print("La cita no es una cita con Ginecologo.")
        except Exception as e:
            print(f"Error al cancelar la cita: {e}")
        
    def mostrar_menu(self):
        print("Menú de opciones:")
        for i, opcion in enumerate(self.opciones):
            print(f"{i+1}. {opcion[0]}")
        
        seleccion = int(input("Seleccione una opción: "))
        return seleccion
    
    def run(self):
        seleccion = self.mostrar_menu()
        while seleccion != 8:
            if seleccion > 8 or seleccion < 1:
                print("Opción no válida.")
            else:
                opcion = self.opciones[seleccion - 1]
                opcion[1]()
            
            seleccion = self.mostrar_menu()
        print("Saliendo del programa...")

if __name__ == '__main__':
    cita_manager = CitaManager()
    cita_manager.run()

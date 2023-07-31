# Importamos módulos necesarios
import random
import string
import time

# Definimos la clase Cliente
class Cliente:
    def __init__(self, nombre, telefono=None):
        self.nombre = nombre
        self.telefono = telefono
        self.username = ""
        self.password = ""

    def asignar_cuenta(self):
        # Generamos el username basado en el nombre del cliente
        self.username = self.nombre.lower().replace(' ', '.') + "@awakelab.com"
        # Generamos la contraseña
        self.password = self.genera_pass()
        # Si el cliente no tiene teléfono, solicitamos ingresarlo
        if self.telefono is None:
            self.telefono = self.ingresa_telefono()

    def genera_pass(self):
        while True:
            # Creamos un string con todos los caracteres que queremos incluir: minúsculas, mayúsculas y números
            caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits
            # Generamos la contraseña eligiendo al azar 15 caracteres del string
            password = ''.join(random.choice(caracteres) for i in range(15))
            # Si incluye al menos una mayúscula, una minúscula y un número, la retornamos; si no, volvemos a generar
            if any(map(str.isupper, password)) and any(map(str.islower, password)) and any(char.isdigit() for char in password):
                return password

    def ingresa_telefono(self):
        while True:
            telefono = input(f'La cuenta de {self.nombre} no tiene teléfono, ingréselo: ')
            if len(telefono) == 8:
                return telefono
            else:
                print('Ha ingresado un teléfono no válido, intente nuevamente')
                time.sleep(2)

# Creamos una lista de clientes
clientes = [
    Cliente('Alberto García'),
    Cliente('Jose Martínez'),
    Cliente('Steffania Schweikart'),
    Cliente('Marcos Alarcón'),
    Cliente('Luis Martínez'),
    Cliente('Baltasar Fernández'),
    Cliente('Hugo González'),
    Cliente('Iván Hernández'),
    Cliente('Daniel López'),
    Cliente('Fernando Herrera')
]

# Asignamos una cuenta a cada cliente
for cliente in clientes:
    cliente.asignar_cuenta()
    print(f"Nombre: {cliente.nombre}")
    print(f"Username: {cliente.username}")
    print(f"Password: {cliente.password}")
    print(f"Teléfono: {cliente.telefono}")
    print()
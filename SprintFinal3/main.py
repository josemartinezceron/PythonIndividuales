# Importamos módulos necesarios
import random, string, time

# Lista con 10 clientes
clientes = {
    '1' : {'nombre' : 'Alberto García'},
    '2' : {'nombre' : 'Jose Martínez'},
    '3' : {'nombre' : 'Steffania Schweikart'},
    '4' : {'nombre' : 'Marcos Alarcón'},
    '5' : {'nombre' : 'Luis Martínez'},
    '6' : {'nombre' : 'Baltasar Fernández'},
    '7' : {'nombre' : 'Hugo González'},
    '8' : {'nombre' : 'Iván hernández'},
    '9' : {'nombre' : 'Daniel López'},
    '10' : {'nombre' : 'Fernando Herrera'}}

# Función que generará contraseñas con minúsculas, mayúsculas y números
def genera_pass():
    while True:
        # Creamos un string con todos los caracteres que queremos incluir, minúsculas, mayúsculas y números
        caracteres = string.ascii_lowercase+string.ascii_uppercase+string.digits
        # Generamos la contraseña eligiendo al azar 15 caracteres del string
        password = ''.join(random.choice(caracteres) for i in range(15))
        # Si incluye al menos una mayúscula, una minúscula y un número, la retornamos; si no, volvemos a generar
        if any(map(str.isupper, password)) and any(map(str.islower, password)) and any(char.isdigit() for char in password):
            return password

def ingresa_telefono(nombre_cliente):
    while True:
        telefono = input(f'La cuenta de {nombre_cliente} no tiene teléfono, ingréselo: ')
        if len(telefono) == 8:
            return telefono
        else:
            print('Ha ingresado un teléfono no válido, intente nuevamente')
            time.sleep(2)

# Función que aisgnará una cuenta a cada cliente
def asigna_cuenta():
    # Recorremos la lista de clientes, asignándole un username basado en su nombre, pasándolo a minúsculas, sustituyendo espacios por puntos, y concatenando "@awakelab.com"
    for key in clientes:
        username = clientes[key]['nombre'].lower().replace(' ','.') + "@awakelab.com"
        password = genera_pass()
        telefono = ingresa_telefono(clientes[key]['nombre'])
        clientes[key].update({'username' : username, 'password' : password, 'telefono' : telefono})
    print(clientes)

# A partir de la llamada a la función "asisgna_cuenta" se realizarán los bucles necesarios
asigna_cuenta()
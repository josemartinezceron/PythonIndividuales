
import time

def obtener_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            return edad
        except ValueError:
            print("Error: ingrese un número entero para la edad.")

def imprimir_datos(usuario):
    print("Edad: ", usuario["edad"])
    time.sleep(5)
    print("Contraseña: ", usuario["password"])
    time.sleep(5)

def agregar_usuario():
    # Preguntar nombre de usuario y contraseña
    nombre = input("Ingrese su nombre de usuario: ")
    if nombre == "salir":
        return False
    password = input("Ingrese su contraseña: ")
    # Obtener la edad del usuario
    edad = obtener_edad()
    # Almacenar los datos del usuario
    usuario = {"nombre": nombre, "password": password, "edad": edad}
    usuarios.append(usuario)
    # Imprimir los datos del usuario
    imprimir_datos(usuario)
    return True

usuarios = []
while True:
    if not agregar_usuario():
        break

print("Usuarios registrados:")
print(usuarios)

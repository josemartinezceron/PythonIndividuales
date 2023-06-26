'''# Diseñar diccionarios para cada usuario
usuario1 = {"nombre": "Juan", "edad": 25, "genero": "masculino", "direccion": "Calle 1 #123", "telefono": "555-1234", "ocupacion": "estudiante"}
usuario2 = {"nombre": "Maria", "edad": 35, "genero": "femenino", "direccion": "Avenida 2 #456", "telefono": "555-5678", "ocupacion": "abogada"}
usuario3 = {"nombre": "Pedro", "edad": 42, "genero": "masculino", "direccion": "Calle 3 #789", "telefono": "555-9012", "ocupacion": "ingeniero"}
usuario4 = {"nombre": "Sofia", "edad": 28, "genero": "femenino", "direccion": "Avenida 4 #1011", "telefono": "555-3456", "ocupacion": "psicologa"}
usuario5 = {"nombre": "Luis", "edad": 50, "genero": "masculino", "direccion": "Calle 5 #1213", "telefono": "555-7890", "ocupacion": "contador"}
usuario6 = {"nombre": "Ana", "edad": 31, "genero": "femenino", "direccion": "Avenida 6 #1415", "telefono": "555-2345", "ocupacion": "programadora"}
usuario7 = {"nombre": "Carlos", "edad": 45, "genero": "masculino", "direccion": "Calle 7 #1617", "telefono": "555-6789", "ocupacion": "medico"}

# Guardar los diccionarios en una lista
usuarios = [usuario1, usuario2, usuario3, usuario4, usuario5, usuario6, usuario7]

# Recorrer la lista e imprimir la información de cada usuario
for usuario in usuarios:
    print("Nombre: " + usuario["nombre"])
    print("Edad: " + str(usuario["edad"]))
    print("Género: " + usuario["genero"])
    print("Dirección: " + usuario["direccion"])
    print("Teléfono: " + usuario["telefono"])
    print("Ocupación: " + usuario["ocupacion"])
    print()'''
# Diseñar una estructura de datos unificada para todas las juntas de vecinos
juntas_vecinos = [
    {
        "nombre_usuario": "Junta de Vecinos 1",
        "id_unico": 1001,
        "antigüedad": 5,
        "fecha_incorporacion": "01/01/2016",
        "edad_promedio": 35,
        "genero": "mixto",
        "direccion": "Calle 1 #123",
        "telefono": "555-1234",
        "presidente": "Juan Perez",
        "secretario": "Maria Lopez",
        "tesorero": "Pedro Ramirez"
    },
    {
        "nombre_usuario": "Junta de Vecinos 2",
        "id_unico": 1002,
        "antigüedad": 3,
        "fecha_incorporacion": "01/01/2018",
        "edad_promedio": 40,
        "genero": "femenino",
        "direccion": "Avenida 2 #456",
        "telefono": "555-5678",
        "presidente": "Sofia Rodriguez",
        "secretario": "Luisa Martinez",
        "tesorero": "Ana Perez"
    },
    {
        "nombre_usuario": "Junta de Vecinos 3",
        "id_unico": 1003,
        "antigüedad": 7,
        "fecha_incorporacion": "01/01/2014",
        "edad_promedio": 45,
        "genero": "masculino",
        "direccion": "Calle 3 #789",
        "telefono": "555-9012",
        "presidente": "Carlos Sanchez",
        "secretario": "Pedro Garcia",
        "tesorero": "Luis Ramirez"
    }
]

# Imprimir la fecha de incorporación de todos los usuarios
for junta in juntas_vecinos:
    print("Fecha de incorporación de la junta " + junta["nombre_usuario"] + ": " + junta["fecha_incorporacion"])
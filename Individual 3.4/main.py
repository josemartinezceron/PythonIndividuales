# Opcion1 con ciclo while
contrasena = ""
while True:
    contrasena = input("Ingrese su contraseña: ")
    # Verificar que la contraseña cumpla con los criterios de seguridad
    tiene_mayusculas = False
    tiene_minusculas = False
    tiene_cifras = False
    tiene_longitud = len(contrasena) >= 8
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayusculas = True
        elif caracter.islower():
            tiene_minusculas = True
        elif caracter.isdigit():
            tiene_cifras = True
    # Mostrar los criterios aún incumplidos al usuario
    if not tiene_mayusculas:
        print("- La contraseña debe tener al menos una letra mayúscula.")
    if not tiene_minusculas:
        print("- La contraseña debe tener al menos una letra minúscula.")
    if not tiene_cifras:
        print("- La contraseña debe tener al menos una cifra.")
    if not tiene_longitud:
        print("- La contraseña debe tener al menos 8 caracteres.")
    # Verificar si la contraseña cumple con los criterios de seguridad
    if tiene_mayusculas and tiene_minusculas and tiene_cifras and tiene_longitud:
        print("¡La contraseña es segura!")
        break
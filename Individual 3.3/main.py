# Pedir al usuario sus características
lugar_de_origen = input("¿De dónde eres? ")
edad = int(input("¿Cuál es tu edad? "))
afinidad_deportes = input("¿Te gustan los deportes? (Sí/No) ")

# Determinar los cuestionarios a responder
cuestionarios = []
if edad >= 18 and edad <= 29:
    cuestionarios.append("Empleabilidad")
if lugar_de_origen == "América Latina":
    cuestionarios.append("Hábitos alimenticios")
    if edad >= 30 and edad <= 59:
        cuestionarios.append("Experiencia laboral")
    elif edad >= 60:
        cuestionarios.append("Actividades recreativas")
if afinidad_deportes == "Sí":
    if edad < 60:
        cuestionarios.append("Atletismo")
    elif lugar_de_origen == "América Latina" and edad >= 60:
        cuestionarios.append("Natación")
    else:
        cuestionarios.append("Deportes en general")

# Mostrar los resultados al usuario
num_cuestionarios = len(cuestionarios)
if num_cuestionarios == 0:
    print("No tienes cuestionarios que responder.")
elif num_cuestionarios == 1:
    print("Tienes que responder 1 cuestionario:")
else:
    print("Tienes que responder", num_cuestionarios, "cuestionarios:")
for cuestionario in cuestionarios:
    print("- " + cuestionario)
    
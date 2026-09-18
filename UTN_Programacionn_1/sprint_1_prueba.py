# DATOS DE ENTRADA
dias_de_viaje = int(input("Ingrese la cantidad de días del viaje: "))
while dias_de_viaje <= 0:
    print("La cantidad de días debe ser mayor a cero.")
    dias_de_viaje = int(input("Ingrese la cantidad de días del viaje: "))
tiene_menores = input("¿Viaja con menores de edad? (si/no): ")
tiene_mayores = input("¿Viaja con mayores de edad (60+ años)? (si/no): ")
cantidad_horas_disponibles = float(input("Ingrese la cantidad de horas diarias disponibles: "))
clima = input("Ingrese el clima del destino (frío, templado, cálido): ")
estación_de_año = input("Ingrese la estación del año (verano, otoño, invierno, primavera): ")
difucultad_actividad = input("Ingrese la dificultad de actividad que desea(leve, moderada, alta)): ")
score = 0
recomendacion_edad = ""
recomendacion_estacion = ""
recomendacion_horas = ""
mensaje_general = ""
# REGLAS DE LA EDAD
if tiene_menores == "si" and tiene_mayores == "si":
    if difucultad_actividad == "leve":
        score += 10
        recomendacion_edad = "Actividades culturales y recreativas para todas las edades."
    else:
        score -= 5
        recomendacion_edad = "Incompatibilidad de actividades para todas las edades. Se recomienda dividir el grupo para actividades especificas."
elif tiene_menores == "si":
    if difucultad_actividad == "leve":
        score += 10
        recomendacion_edad = "Museos interactivos de ciencia y funciones de teatro infantil."
    elif difucultad_actividad == "moderada":
        score += 5
        recomendacion_edad = "Caminatas guiadas cortas o alquiler de bicicletas en circuitos cerrados."
    else:
        score -= 10
        recomendacion_edad = "ADVERTENCIA: Reducir la exigencia física."    
elif tiene_mayores == "si":
    if difucultad_actividad == "leve":
        score += 10
        recomendacion_edad = "Visitas a museos, parques y actividades culturales."
    elif difucultad_actividad == "moderada":
        score += 5
        recomendacion_edad = "Caminatas a ritmo pausado con paradas frecuentes y visitas a ferias."
    else:
        score -= 10
        recomendacion_edad = "ADVERTENCIA: Reducir la exigencia física."
else:
    if difucultad_actividad == "alta":
        score += 10
        recomendacion_edad = "Rafting, ascenso a montañas y actividades de aventura."
    elif difucultad_actividad == "moderada":
        score += 10
        recomendacion_edad = "Caminatas, ciclismo y actividades al aire libre."
    else:
        score += 5
        recomendacion_edad = "Visitas a museos, bodegones y tardes de playa o spa."

#REGLA ESTACION + CLIMA
if estación_de_año == "verano" and clima == "cálido":
    if difucultad_actividad == "leve":
        score += 10
        recomendacion_estacion = "Ideal para balnearios, piletas y actividades acuáticas."
    elif difucultad_actividad == "moderada":
        score += 5
        recomendacion_estacion = "Caminatas y depeortes acuaticos evitando actividades físicas intensas durante las horas de mayor calor."
    else:
        score -= 10
        recomendacion_estacion = "ALERTA CLIMÁTICA. Esfuerzo físico alto bajo calor extremo. Reprogramar actividades para horarios nocturnos o zonas de sombra."

elif estación_de_año == "invierno" and clima == "frío":
    if difucultad_actividad == "leve":
        score += 10
        recomendacion_estacion = "Actividades indoor y centros culturales. Llevar abrigo térmico."
    elif difucultad_actividad == "moderada":
        score += 5
        recomendacion_estacion = "Senderismo invernal bajo áreas boscosas o treekking liviano con calzado antideslizante."
    else:
        score -= 10
        recomendacion_estacion = "ALERTA CLIMÁTICA. Riesgo por bajas temperaturas en montañas o al aire libre."

elif (estación_de_año == "primavera" or estación_de_año == "otoño") and clima == "templado":
    if difucultad_actividad == "leve":
        score += 5
    elif difucultad_actividad == "moderada":
        score += 10
    else:
        score += 10

#REGLA DIAS Y HORAS
if dias_de_viaje <= 3:
    if cantidad_horas_disponibles <= 2:
        recomendacion_horas = "\nViaje con un ritmo ajustado, se recomienda planificar horarios con anticipacion"
        score -= 5
    elif cantidad_horas_disponibles >= 4:
        recomendacion_horas = "\nViaje corto pero con jornadas largas, se puede aprovechar cada día para actividades más extensas"
        score += 3
elif dias_de_viaje >= 4:
    if cantidad_horas_disponibles <= 2:
        recomendacion_horas = "\nViaje extendido con poco tiempo libre diario, conviene espaciar las actividades a lo largo de los días."
        score -= 3
    elif cantidad_horas_disponibles >= 4:
        recomendacion_horas = "\nViaje con amplio margen de tiempo, se pueden combinar varias actividades por día sin apuro"
        score += 5

# EVALUACION FINAL DEL SCORE 
if score >= 20:
    diagnostico = "Compatibilidad Óptima (Plan Altamente recomendado)"
    mensaje_general = "La dificultad y el perfil del grupo están perfectamente alineados."
elif score >= 10:
    diagnostico = "Compatibilidad Moderada (Plan Viable)"
    mensaje_general = "El plan es adecuado, pero se sugiere ajustar algunas actividades para mejorar la experiencia."
else:
    diagnostico = "Compatibilidad Baja (Plan No Recomendado)"
    mensaje_general = "El plan no es adecuado para el grupo. Se recomienda reconsiderar las actividades y la dificultad."

# ==========================================
# SALIDA DE RESULTADOS UNIFICADA
# ==========================================

print("\n" + "=" * 65)
print("             DIAGNÓSTICO FINAL DEL SISTEMA DE VIAJES            ")
print("=" * 65)

print(f"\n---> Puntaje de Adecuación (Score): {score} pts")
print(f"---> Diagnóstico General: {diagnostico}")
print(f"---> Evaluación del Perfil: {mensaje_general}")

print("\n" + "-" * 65)
print("RECOMENDACIONES Y SUGERENCIAS DETALLADAS:")
print("-" * 65)

if recomendacion_edad == "":
    print("- No se activaron sugerencias específicas para los datos ingresados.")
else:
    print(recomendacion_edad)
if recomendacion_estacion == "":
    print("- No se activaron sugerencias específicas para los datos ingresados.")
else:
    print(recomendacion_estacion)
if recomendacion_horas == "":
    print("- No se activaron sugerencias específicas para los datos ingresados.")
else:
    print(recomendacion_horas)

print("=" * 65)
print("¡Gracias por utilizar el Asistente de Planificación de Viajes!")
print("=" * 65)
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
recomendacion = ""
mensaje_general = ""
# REGLAS DE LA EDAD
if tiene_menores == "si":
    if difucultad_actividad == "leve":
        score += 10
        recomendacion = "Museos interactivos de ciencia y funciones de teatro infantil."
    elif difucultad_actividad == "moderada":
        score += 5
        recomendacion = "Caminatas guiadas cortas o alquiler de bicicletas en circuitos cerrados."
    else:
        score -= 10
        recomendacion = "ADVERTENCIA: Reducir la exigencia física."    
elif tiene_mayores == "si":
    if difucultad_actividad == "leve":
        score += 10
        recomendacion = "Visitas a museos, parques y actividades culturales."
    elif difucultad_actividad == "moderada":
        score += 5
        recomendacion = "Caminatas a ritmo pausado con paradas frecuentes y visitas a ferias."
    else:
        score -= 10
        recomendacion = "ADVERTENCIA: Reducir la exigencia física."
elif tiene_menores == "si" and tiene_mayores == "si":
    if difucultad_actividad == "leve":
        score += 10
        recomendacion = "Actividades culturales y recreativas para todas las edades."
    else:
        score -= 5
        recomendacion = "Incompatibilidad de actividades para todas las edades. Se recomienda dividir el grupo para actividades especificas."
else:
    if difucultad_actividad == "alta":
        score += 10
        recomendacion = "Rafting, ascenso a montañas y actividades de aventura."
    elif difucultad_actividad == "moderada":
        score += 10
        recomendacion = "Caminatas, ciclismo y actividades al aire libre."
    else:
        score += 5
        recomendacion = "Visitas a museos, bodegones y tardes de playa o spa."


# EVALUACION FINAL DEL SCORE 
if score >= 10:
    diagnostico = "Compatibilidad Óptima (Plan Altamente recomendado)"
    mensaje_general = "La dificultad y el perfil del grupo están perfectamente alineados."
elif score >= 5:
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

if recomendacion == "":
    print("- No se activaron sugerencias específicas para los datos ingresados.")
else:
    print(recomendacion)

print("=" * 65)
print("¡Gracias por utilizar el Asistente de Planificación de Viajes!")
print("=" * 65)





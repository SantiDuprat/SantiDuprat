# Desafío: Encuesta Tecnológica en UTN Technologies 

# UTN Technologies, una reconocida software factory, está en la búsqueda de ideas para su próximo desarrollo en Python, con el objetivo de revolucionar el mercado. 

# Las tecnologías en evaluación son: 
# 🔹 Inteligencia Artificial (IA) 
# 🔹 Realidad Virtual/Aumentada (RV/RA) 
# 🔹 Internet de las Cosas (IOT) 

# Para tomar una decisión informada, la empresa ha lanzado una encuesta entre sus empleados con el propósito de analizar ciertas métricas. 

# 🔹 Recolección de Datos 

# Cada empleado encuestado deberá proporcionar la siguiente información: 
# ✔️ Nombre 
# ✔️ Edad (debe ser 18 años o más) 
# ✔️ Género (Masculino, Femenino, Otro) 
# ✔️ Tecnología elegida (IA, RV/RA, IOT) 

# El sistema deberá permitir ingresar los datos de 10 empleados mediante la terminal. 

# 🔹 Análisis de Datos 

# A partir de las respuestas, se deben calcular las siguientes métricas: 

# Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años (inclusive). 

# Porcentaje de empleados que NO votaron por IA, siempre y cuando su género no sea femenino y su edad está entre los 33 y 40 años. 

# Nombre y apellido del empleado de menor edad. 

# Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó. 

# Realizar un gráfico de barras verticales para visualizar la cantidad de empleados que eligió cada tecnología. Por ejemplo: 



# Realizar un gráfico de termómetro para determinar el porcentaje total de empleados de género masculino, sobre el total. Por ejemplo: 



# 🔹 Requisitos del Programa 

#  ✔️ Los datos deben solicitarse y validarse correctamente. 
# ✔️ Utilizar variables adecuadas para almacenar la información y facilitar su análisis. 
# ✔️ Presentar los resultados de manera clara y organizada. 

i = 0
cantidad_masculinos = 2
cantidad_empleados_no_ia = 3
cantidad_IA = 2
cantidad_RV_RA = 5
cantidad_IOT = 3
cantidad_empleados_masculinos_IA_IOT = 4
bandera_masculino = True
nombre_menor = "juan"
minimo = 18
nombre_mayor = "pedro"
maximo = 50
tecnologia_mayor = "IA"

while i > 10:
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        print("La edad debe ser mayor o igual a 18 años.")
        edad = int(input("Reingrese su edad: "))
    genero = input("Ingrese su género (masculino - femenino - otro): ")
    while genero != "masculino" and genero != "femenino" and genero != "otro":
        print("Género no válido.")
        genero = input("Reingrese su género (masculino - femenino - otro): ")
    tecnologia = input("Ingrese tecnología que prefiere (IA - RV/RA - IOT): ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        print("Tecnología no válida.")
        tecnologia = input("Reingrese tecnología que prefiere (IA - RV/RA - IOT): ")

    if genero == "masculino":
        
        if (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50:
            cantidad_empleados_masculinos_IA_IOT += 1
        if bandera_masculino or edad > maximo:
            maximo = edad
            nombre_mayor = nombre 
            tecnologia_mayor = tecnologia
        cantidad_masculinos += 1
        bandera_masculino = False
    if genero != "femenino" and tecnologia != "IA" and edad >= 33 and edad <= 40:
        cantidad_empleados_no_ia += 1 
        
    if i == 0 or edad < minimo:
        minimo = edad 
        nombre_menor = nombre

    if tecnologia == "IA":
        cantidad_IA += 1
    elif tecnologia == "RV/RA":
        cantidad_RV_RA += 1
    else:
        cantidad_IOT += 1
    i += 1
porcentaje = (cantidad_empleados_no_ia / 10) * 100

print (f"Cantidad de empleados masculinos que votaron por IA o IOT: {cantidad_empleados_masculinos_IA_IOT}")
print (f"Porcentaje de empleados que no votaron por IA: {porcentaje}")
print (f"Empleado de menor edad: {nombre_menor} con {minimo} años")
print (f"Empleado masculino de mayor edad: {nombre_mayor} con {maximo} años y eligio {tecnologia_mayor}") 


# Gráfico de barras verticales

mayor = cantidad_IA

if cantidad_RV_RA > mayor:
    mayor = cantidad_RV_RA

if cantidad_IOT > mayor:
    mayor = cantidad_IOT

while mayor > 0:
    if cantidad_IA >= mayor:
        print("  *  ", end="")
    else:
        print("     ", end="")

    if cantidad_RV_RA >= mayor:
        print("  *  ", end="")
    else:
        print("     ", end="")

    if cantidad_IOT >= mayor:
        print("  *")
    else:
        print()
    mayor = mayor - 1

print(" IA  RV/RA  IOT")

# Gráfico de termómetro

valor = cantidad_masculinos
valor_max = 10
ancho_escala = 1

escalones = valor_max // (1 * ancho_escala)
nivel_lleno = valor // (1 * ancho_escala)

print(f"\n   Termómetro - Empleados que eligieron IA ({valor}/{valor_max})")
print("   ┌────┐")

nivel = escalones
while nivel > 0:
    etiqueta = f"{nivel:>3}"
    if nivel <= nivel_lleno:
        print(f"{etiqueta}│████│")
    else:
        print("   │    │")
    nivel -= 1

print("   └────┘")
print("    ╲██╱")
print("     ▔▔")
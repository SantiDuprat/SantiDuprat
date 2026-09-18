# ENTRADAS
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura en centimetros: "))
estres = int(input("Ingrese su nivel de estres (1-10): "))
estado_animo = input("Ingrese su estado de animo (feliz, triste, irritable, ansioso): ")

# CALCULOS
altura_metros = altura / 100
imc = edad / (altura_metros ** 2)

# REGLA 1 ESTRES - ESTADO DE ANIMO
if estres <= 2:
    if estado_animo == "feliz":
        print("Regla 1: Estres bajo y estado de animo feliz")
    elif estado_animo == "triste":
        print("Regla 1: Estres bajo y estado de animo triste")
    elif estado_animo == "irritable":
        print("tenes estres muy bajo y estado de animo irritable")
    else:
        print("hola")
# ESTRUCTURA while
# while <condición>:
#     <bloque de código>

# CONTADORES
# x = 0              # Inicialización de la variable x
# while True:        # Condición de la estructura while
#     x += 1         # Incremento de la variable x              

# ACUMULADORES
# acumulador = 0
# contador = 0
# while True:                                       # Bucle infinito
#     valor = int(input("Ingrese un valor: "))      # Inicialización de la variable valor
#     acumulador += valor
#     contador += 1
# print("El acumulador es:", acumulador)             # Muestra del valor del acumulador

# VALIDACIÓN DE CLAVE
# while True:                                         # Bucle infinito
#     x = int(input("Ingrese su clave: "))            # Inicialización de la variable x
#     if x == 1234:                                   # Condición de salida del bucle
#         print("Clave correcta")                     # Bloque de código que se ejecuta cuando la condición es verdadera
#         break                                       # Salida del bucle
#     else:
#         print("Clave incorrecta")                   # Bloque de código que se ejecuta cuando la condición es falsa

# PROMEDIO
# nota_parcial = int(input("Ingrese la nota parcial: "))          # Inicialización de la variable nota_parcial
# cantidad_parciales = 1                                          # Inicialización de la variable cantidad_parciales
# while cantidad_parciales < 5:                                   # Suponiendo que queremos ingresar 5 notas parciales
#     cantidad_parciales += 1                                     # Incremento de la variable cantidad_parciales
#     nota_parcial += int(input("Ingrese la nota parcial: "))     # Bloque de código que se ejecuta mientras la condición sea verdadera
# promedio = nota_parcial / cantidad_parciales                    # Cálculo del promedio de las notas parciales
# print("El promedio de las notas parciales es:", promedio)       # Muestra del promedio de las notas parciales 

# MAXIMO Y MINIMO (CAMBIANDO EL IF A MENOR QUE)
# i = 0
# maximo = 0
# while i < 10:
#     numero = float(input("Ingrese un número: "))
#     if i == 0 or numero > maximo:
#         maximo = numero
#     i += 1
# print("Máximo:", maximo)

# Ingrese numeros indeterminadamente
# seguir = "si"
# suma = 0
# while seguir == "si":
#     numero = int(input("Ingrese un número: "))
#     suma += numero
#     seguir = input("¿Desea ingresar otro número? (si/no): ")
# print(f"La suma es: {suma}")


# suma = 0
# while True:
#     numero = int(input("Ingrese un número: "))
#     suma += numero
#     seguir = input("¿Desea ingresar otro número? (si/no): ")
#     if seguir == "no":
#         break
# print(f"La suma es: {suma}")
'''
Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
Calcular la suma de los números positivos y el producto de los negativos. 
'''
# suma_positivos = 0
# producto_negativos = 1
# while True:
#     numero = int(input("Ingrese un número: "))
#     if numero > 0:
#         suma += numero
#     elif numero < 0:
#         producto *= numero
#     seguir = input("¿Desea ingresar otro número? (si/no): ")
#     if seguir == "no":
#         break
# print(f"La suma es: {suma}")
# print(f"El producto de los números negativos es: {producto}")
####################################################################
# seguir = "si"
# suma = 0
# bandera = False
# while seguir == "si":
#     numero = int(input("Ingrese un número: "))
#     if bandera == False or numero > maximo:
#         maximo = numero
#         bandera = True
#     seguir = input("¿Desea ingresar otro número? (si/no): ")
#  print (f"El número máximo ingresado es: {maximo}")


# suma_negativos = 0
# suma_positivos = 0
# cantidad_negativos = 0
# cantidad_positivos = 0
# cantidad_total = 0
# numero_menor = 0
# numero_positivo_mayor = 0

# while True:

#     numero = int(input("Ingrese un número: "))

#     cantidad_total += 1

#     # Números positivos
#     if numero > 0:
#         suma_positivos += numero
#         cantidad_positivos += 1

#         if numero_positivo_mayor == 0 or numero > numero_positivo_mayor:
#             numero_positivo_mayor = numero

#     # Números negativos
#     elif numero < 0:
#         suma_negativos += numero
#         cantidad_negativos += 1

#     # Número más chico
#     if numero_menor == 0 or numero < numero_menor:
#         numero_menor = numero

#     seguir = input("¿Desea ingresar otro número? (si/no): ")

#     if seguir == "no":
#         break


# # Promedio de los números positivos
# if cantidad_positivos > 0:
#     promedio_positivos = suma_positivos / cantidad_positivos
# else:
#     promedio_positivos = 0

# # Porcentaje de números negativos
# porcentaje_negativos = (cantidad_negativos * 100) / cantidad_total


# print(f"Suma de los negativos: {suma_negativos}")
# print(f"Suma de los positivos: {suma_positivos}")
# print(f"Cantidad de negativos: {cantidad_negativos}")
# print(f"Promedio de los positivos: {promedio_positivos}")
# print(f"Número más chico: {numero_menor}")
# print(f"Número positivo más grande: {numero_positivo_mayor}")
# print(f"Porcentaje de negativos: {porcentaje_negativos}%")

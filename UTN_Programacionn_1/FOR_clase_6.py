# r = range(5)
# print(list(r))
# range(inicializacion, condicion, incremento)
# for i in range(5):
#     print(i)    

# suma = 0
# CANTIDAD = 5
# for i in range(0, CANTIDAD, 1):
#     numero = int(input("Ingrese un numero: "))
#     suma += numero
# promedio = suma / CANTIDAD
# print(promedio)

# numero = int(input("Ingrese un numero: "))
# for i in range(1, 11, 1):
#     print(f"{numero} x {i} = {numero * i}")

# for i in range(0, 11, 1):
#     numero = int(input("Ingrese un numero: "))

#     if numero % 5 == 0:
#         continue

# # Ingresar 10 números. Solo sumar los que estén fuera del rango 50-100. 
# suma = 0
# for i in range(1, 11, 1):
#     numero = int(input("Ingrese un numero: "))

#     if numero >= 50 and numero <= 100:
#         continue
    
#     suma += numero

# print(f"La suma de los numeros es: {suma}")

n = int(input("Ingrese un número: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # Salto de línea al terminar cada fila
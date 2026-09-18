
numero = int(input("Ingresa un número : "))
cantidad_primos = 0
contador_divisores = 0

for i in range(1, numero + 1, 1):
    es_primo = True
    
    for j in range(1, i + 1, 1):
        if i % j == 0:
            contador_divisores += 1

    if contador_divisores == 2:
        print(f"El número {i} es primo")
        cantidad_primos += 1
    contador_divisores = 0  

print(f"Cantidad total de números primos encontrados: {cantidad_primos}")
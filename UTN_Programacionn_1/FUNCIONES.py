# Escribir una función que calcule el área de un rectángulo. 
# La función recibe la base y la altura y retorna el área. 

# def calcular_area_rectangulo(base, altura):
#     return base * altura

# print(calcular_area_rectangulo(5, 10)) 

# Diseña una función que calcule la potencia de un número. 
# La función debe recibir la base y el exponente como argumentos y devolver el resultado. 

def calcular_potencia_numero(base: int, exponente: int):
    potencia = base ** exponente
    return potencia

potencia = calcular_potencia_numero(2, 3)
print(potencia)
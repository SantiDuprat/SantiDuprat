# Welcome to your project

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a / b


while True:
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "5":
        print("Cerrando calculadora...")
        break

    if opcion in ["1", "2", "3", "4"]:

        num1 = float(input("Ingresá el primer número: "))
        num2 = float(input("Ingresá el segundo número: "))

        if opcion == "1":
            resultado = sumar(num1, num2)

        elif opcion == "2":
            resultado = restar(num1, num2)

        elif opcion == "3":
            resultado = multiplicar(num1, num2)

        elif opcion == "4":
            resultado = dividir(num1, num2)

        print("Resultado:", resultado)

    else:
        print("Opción inválida.")

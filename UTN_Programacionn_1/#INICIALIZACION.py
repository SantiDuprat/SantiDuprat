#INICIALIZACION
CARGO_FIJO = 7000
COSTO_METRO = 200
# ENTRADAS
metros_consumidos = int(input("Ingrese los metros cúbicos consumidos: "))
tipo_cliente = input("Ingrese el tipo de cliente (residencial, comercial, industrial): ")
# PROCESOS
subtotal_consumo = (metros_consumidos * COSTO_METRO) + CARGO_FIJO

if tipo_cliente == "residencial" and metros_consumidos < 30:
    descuento = subtotal_consumo * 0.10
else:
    if metros_consumidos > 80:
        recargo = 15
    else:
        if metros_consumidos > 150:
            recargo = 15
        else:
            if metros_consumidos > 300:
                recargo = 25
else:
    if tipo_cliente == "comercial" and metros_consumidos < 50:
        recargo = 25
else:
    if tipo_cliente == "industrial" and metros_consumidos > 500 and metros_consumidos < 1000:
        recargo = 35
    else:
        if tipo_cliente == "industrial" and metros_consumidos > 1000:
            recargo = 50
        else:
            if tipo_cliente == "industrial" and metros_consumidos < 200:
                recargo = 50

# SALIDAS
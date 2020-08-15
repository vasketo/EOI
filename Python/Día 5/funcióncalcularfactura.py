#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad
# sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle
# el porcentaje de IVA, deberá aplicar un 21%.

def calcularPrecioFinal(precio, iva=21):
    """Función de aplica el IVA a una factura.
    Parametros
    precio: Es la cantidad sin IVA
    iva: Es el porcentaje de IVA
    Devuelve el total de la factura una vez aplicado el IVA.
    """
    try:

        return precio + precio*iva/100

    except Exception as mensaje_de_error:
        print(str(mensaje_de_error))

print(f"El importe total de una factura de 50€ con un 10% de IVA es {calcularPrecioFinal(50,10)}€.")
print(f"El importe total de una factura de 225€ con el 21% de IVA es {calcularPrecioFinal(225)}€.")
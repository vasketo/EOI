#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Muestra el funcionamiento de una función en python. Se establece un parámetro con un valor por defecto.

def calcular_potencia(num,potencia=2):

    try:
        return num**potencia

    except Exception as mensaje_de_error:

        print(str(mensaje_de_error))

try:

    num=int(input("Dime un número: "))

    total = calcular_potencia(num)
    print(f"El resultado de {num}² es {total}.")

    total = calcular_potencia(num,3)
    print(f"El resultado de {num}³ es {total}.")

except Exception as mensaje_de_error:

    print(str(mensaje_de_error))
#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos
# los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación.
# Por ejemplo 5! = 1x2x3x4x5=120). Utiliza una función para realizar el cálculo.

def factorial(num):

    resultado = 1
    contador = 1
    while contador <= num:
        resultado = resultado * contador
        contador += 1

    return resultado

try:

    num=int(input("Dime un número:"))
    resultado = factorial(num)
    print(f"El factorial de {num} da como resultado {resultado} ")

except Exception as mensaje_de_error:

    print(str(mensaje_de_error))
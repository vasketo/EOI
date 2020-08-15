#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Crea una función “obtenerMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
# Crea un programa que genere 10 números aleatorios entre 1 y 100 y muestre el máximo y el mínimo,
# utilizando la función anterior.

import random

# Procedimiento ObtenerMaxMin: recibe una lista de enteros  y devuelve el máximo y el mínimo de los números guardados
# en el vector.
# Parámetros de entrada: lista de enteros
# Valores de salida: valor máximo y mínimo

def obtenermaxmin(lista):
    return max(lista), min(lista)


# Crea una función "calcularMaxMin" que recibe una lista con valores numéricos y
# devuelve el valor máximo y el mínimo.

try:

    numeros = []
    # Incializo la lista con valores aleatorios
    for i in range(10):
        numeros.append(random.randint(1, 100))

    numeros.sort()
    vmax, vmin = obtenermaxmin(numeros)
    print("La lista de números generada es:", ",".join(str(numero) for numero in numeros))
    print("El valor mínimo es ", vmin)
    print("El valor máximo es ", vmax)

except Exception as mensaje_de_error:
    print(str(mensaje_de_error))
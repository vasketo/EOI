#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima
# de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

# Función calcularTemperaturaMedia: Recibe dos números reales que representan
# dos temperaturas y devuelve la temperatura media.
# Parámetros de entrada: dos temperaturas (real)
# Dato devuelto: La temperatura media (real)

def calcularTemperaturaMedia(temp_max,temp_min):
    return (temp_max + temp_min)/2


cantidad=int(input("¿Cuántas temperaturas vas a calcular?:"))

for indice in range(cantidad):

    try:
        temp_min = float(input("Introduce temperatura mínima:"))
        temp_max = float(input("Introduce temperatura máxima:"))
        print("Temperatura media:", calcularTemperaturaMedia(temp_min,temp_max))

    except Exception as mensaje_de_error:
        print(str(mensaje_de_error))

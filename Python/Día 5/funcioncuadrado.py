#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Muestra el funcionamiento de una función en python.

def cuadrado(num):
    return num**2

try:
    num=int(input("Dime un número:"))
    total = cuadrado(num)
    print(f"El resultado de {num}² es {total}")

except Exception as mensaje_de_error:
    print(str(mensaje_de_error))

# -*- encoding: utf-8 -*-

# Escribe un programa que, dada una frase por el usuario, muestre la cantidad total de vocales
# (tanto mayúsculas como minúsculas) que contiene.

frase = input("Introduce una frase:")

vocales="aeiouAEIOU"

cantidad=0

for letra in frase:
    if letra in vocales:
        cantidad += 1

print("La frase",frase,"tiene",cantidad,"vocales", end=".")
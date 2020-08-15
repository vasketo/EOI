# -*- encoding: utf-8 -*-

# Escribe un programa que pida al usuario una frase y muestre por pantalla el número de veces que contiene cada vocal.

frase = input("Introduce frase: ").lower()
vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:

    print("La vocal", vocal, "aparece", frase.count(vocal), "veces.")
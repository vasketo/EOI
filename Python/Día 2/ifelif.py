#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Este programa muestra el funcionamiento de de la estructura de control: if elif else

nota = float(input("Dime tu nota:"))

if nota >=0 and nota < 5:
    print("Suspenso")
elif nota == 5:
    print("Suficiente")
elif nota <= 7:
    print("Bien")
elif nota <= 8:
    print("Notable")
elif nota <= 10:
    print("Sobresaliente")
else:
    print("Nota incorrecta")

print("Programa terminado")
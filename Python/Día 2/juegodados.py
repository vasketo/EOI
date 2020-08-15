#!/usr/bin/env python

# -*- encoding: utf-8 -*-

#Juego dados

import random

print("JUEGO DE DADOS")

num1 = random.randrange(1, 7)
num2 = random.randrange(1, 7)

print("Usuario 1 ha sacado un", num1)
print("Usuario 2 ha sacado un", num2)

if num1 == num2:
    print("Han empatado.")
elif num1 > num2:
    print("Ha ganado el Usuario 1.")
else:
    print("Ha ganado el Usuario 2.")
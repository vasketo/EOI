#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Este programa muestra el funcionamiento de de la estructura de control: if

salario = int(input("Introduce tu salario anual: "))

if salario >= 30000:
    impuestos = salario * 0.3 #Si el salario es igual o superior a 30k se paga un 30%
    print ("Impuestos:", impuestos)


if salario < 30000:
    impuestos = salario * 0.2  # Si el salario es inferior a 30k se paga un 20%
    print("Impuestos:", impuestos)

print ("Salario real:", salario-impuestos)
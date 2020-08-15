#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Este programa muestra el funcionamiento de de la estructura de control: if

salario = int(input("Introduce tu salario anual: "))

if salario >= 30000 or salario <= 40000:
    impuestos = salario * 0.3 #Si el salario es igual o superior a 30k y menor o igual a 40k se paga un 30%
    print ("Impuestos:", impuestos)

print ("Salario real:", salario-impuestos)
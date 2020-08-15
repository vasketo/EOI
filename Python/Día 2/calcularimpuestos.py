#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Preguntar por pantalla el salario anual y si el salario es superior a 30.000€ calcular el
# porcentaje de impuestos a pagar siendo este de un 30%. Si el salario es superior a
# 20.000€ pero inferior a 30.000€ calcular el porcentaje de impuestos a pagar siendo
# este de un 20%. Si el salario es inferior a 20.000€ calcular el porcentaje de impuestos
# a pagar siendo este de un 10%.


salario = int(input("Introduce tu salario anual: "))

if salario > 30000:
    impuestos = salario * 0.3  # Si el salario es superior a 30k se paga un 30%
    print ("Impuestos:", impuestos)
elif salario > 20000:
    impuestos = salario * 0.2  # Si el salario es superior a 20k se paga un 20%
    print("Impuestos:", impuestos)
else:
    impuestos = salario * 0.1  # Si el salario no es superior a 20k se paga un 10%
    print ("Impuestos:", impuestos)

print ("Salario real:", salario-impuestos)

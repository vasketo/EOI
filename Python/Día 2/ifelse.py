#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Este programa calcula la cantidad de impuestos a pagar anualmente en base al salario.

salario = int(input("Introduce tu salario anual: "))

if salario > 30000:

    impuestos = salario * 0.3 #Si el salario es superior a 30k se paga un 30%
    print ("Impuestos:", impuestos)
	
else:

    impuestos = salario * 0.1 #Si el salario no es superior a 30k se paga un 10%
    print ("Impuestos:", impuestos)

print ("Salario real:", salario-impuestos)
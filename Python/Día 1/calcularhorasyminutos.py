#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos = int(input("Introduce la cantidad de minutos:"))
res_horas = minutos // 60
res_min = minutos % 60
print(res_horas,"horas y",res_min,"minutos.")

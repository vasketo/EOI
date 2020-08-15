#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Algoritmo que muestre la tabla de multiplicar de los números del 1 al 10.

for tabla in range(1, 11):
    for num in range(1, 11):
        print("%d * %d = %d" % (tabla,num,num*tabla))


#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas.

nombre = input("Dime tu nombre:")
apellido1 = input("Dime tu primer apellido:")
apellido2 = input("Dime tu segundo apellido:")

iniciales = nombre[0]
iniciales = iniciales + apellido1[0]
iniciales = iniciales + apellido2[0]

iniciales = iniciales.upper()
print("Las iniciales son:", iniciales)

#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Solicitar a un usuario la temperatura por pantalla y convertirla a celsius.

fahrenheit = float(input("Introduce la temperatura en ºF:"))
celsius = (fahrenheit - 32) * 5 / 9
print("La temperatura es", celsius, "ºC")

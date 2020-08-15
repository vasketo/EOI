#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Este programa pregunta por tu nombre y apellidos
# y muestra un mensaje para saludar

print('Escribe tu nombre y 2 apellidos')
nombre = input()
print('Encantado de saludarte ' + nombre)
print('Encantado de saludarte', nombre)
print("Encantado de saludarte %s" % nombre)
print ("Encantado de saludarte {}".format(nombre))
print(f"Encantado de saludarte {nombre}")



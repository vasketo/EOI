#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Programa que pide un usuario y una contraseña, de forma repetitiva mientras que no introduzca “123456”.
# Cuando finalmente escriba la contraseña correcta, se le dirá “Bienvenido Usuario” y terminará el programa.

secreto = "123456"
nombre = input("Introduce el nombre de usuario:")
clave = input("Dime la clave:")

while clave != secreto:
    print("Clave incorrecta!!!")
    clave = input("Dime la clave:")

print("Bienvenido", nombre)

print("Programa terminado")
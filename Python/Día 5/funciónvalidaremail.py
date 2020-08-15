#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no,
# valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".

def validar(email):
    if "@" in email:
        return True
    else:
        return False


direccion = input("Tu email: ")

if validar(direccion):
    print("Dirección válida")
else:
    print("Dirección inválida")
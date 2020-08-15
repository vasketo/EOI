#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Este programa muestra el funcionamiento de de la estructura de control: while

num = int(input("Introduce el número con el que quieres iniciar la cuenta atrás: "))

contador = 0
while (num > contador):
    print('Cuenta atrás:', num - contador)
    contador = contador + 1
else:
	print('Fin del programa.')
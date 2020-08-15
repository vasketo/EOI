#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Este programa muestra el funcionamiento de la estructura de control: while

while True:
    print('Escribe tu nombre')
    nombre = input()
    if nombre != 'Pedro':
        continue

    print('Hola Pedro. ¿Cuál es tu contraseña?')
    password = input()
    if password == '123456':
        break

print('Acceso autorizado.')
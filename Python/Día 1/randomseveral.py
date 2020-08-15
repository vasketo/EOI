#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Ejemplo de la librería random

import random

# Genero número float aleatorio
print ('random float entre 0 y 1 : ', random.random())
# Genero número float entre 1 y 100
print ('random float entre 0 y 100 : ', random.random()*100)

# Genero número entero aleatorio entre 0 y 5
print ('randint(0,5) : ', random.randint(0, 5))

# Seleccione una opción aleatoria.
print('Selecciono opción aleatoria entre uno, dos y tres:', random.choice(["uno", "dos", "tres"]))

# Obtiene un número aleatorio entre 1 y 99
print ("randrange(100) : ", random.randrange(100))

# Obtiene aleatoriamente un número impar entre 1 y 100
print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))



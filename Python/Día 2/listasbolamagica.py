#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Ejemplo de programa de bola mágica

import random

pregunta = input("escribe una pregunta")

mensajes = ['Es cierto',
'Es decididamente así',
'Sí definitivamente',
'Respuesta confusa, intenta otra vez',
'Pregunta de nuevo más tarde',
'Concéntrate y pregunta otra vez',
'Mi respuesta es no',
'Perspectivas no tan buenas',
'Muy dudoso']

print(mensajes[random.randint(0, len(mensajes) - 1)])
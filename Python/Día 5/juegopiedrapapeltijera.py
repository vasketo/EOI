#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Juego de piedra, papel y tijera.

import random

while (True):

    aleatorio = random.randrange(0, 3)
    elige_pc = ""

    print ("")
    print("1)Piedra")
    print("2)Papel")
    print("3)Tijera")
    print("4)Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        elige_usuario = "piedra"
    elif opcion == 2:
        elige_usuario = "papel"
    elif opcion == 3:
        elige_usuario = "tijera"
    else:
        break

    print("Has elegido: ", elige_usuario)

    if aleatorio == 0:
        elige_pc = "piedra"
    elif aleatorio == 1:
        elige_pc = "papel"
    elif aleatorio == 2:
        elige_pc = "tijera"

    print("PC eligió: ", elige_pc)
    print("...")

    if elige_pc == "piedra" and elige_usuario == "papel":
        print("Ganaste, papel envuelve a piedra")
    elif elige_pc == "papel" and elige_usuario == "tijera":
        print("Ganaste, Tijera corta papel")
    elif elige_pc == "tijera" and elige_usuario == "piedra":
        print("Ganaste, Piedra aplasta tijera")
    if elige_pc == "papel" and elige_usuario == "piedra":
        print("perdiste, papel envuelve piedra")
    elif elige_pc == "tijera" and elige_usuario == "papel":
        print("perdiste, Tijera corta papel")
    elif elige_pc == "piedra" and elige_usuario == "tijera":
        print("perdiste, Piedra aplasta tijera")
    elif elige_pc == elige_usuario:
        print("empate")
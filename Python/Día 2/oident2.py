#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Ejercicio con operadores de identidad y tipos de variables

var1 = "Python 3 para impacientes"
var2 = 3
var3 = 3.14
var4 = True
var5 = [1, 2, 3]
var6 = ('a', 'b', 'c')
var7 = {'a':1, 'b':2, 'c':3}

if type(var1) is str:
    print(f"'var1:' {var1}, es una cadena.")

if type(var2) is int:
    print(f"'var2:' {var2},  es un número entero.")

if type(var3) is float:
    print(f"'var3:' {var3}, es un número con decimales.")

if type(var4) is bool:
    print(f"'var4:' {var4},  es un booleano.")

if type(var4):
    print(f"'var4:' {var4}, es un booleano.")

if type(var5) is list:
    print(f"'var5:' {var5}, es una lista.")

if type(var6) is tuple:
    print(f"'var6:' {var6}, es una tupla.")

if type(var7) is dict:
    print(f"'var7:' {var7}, es un diccionario.")
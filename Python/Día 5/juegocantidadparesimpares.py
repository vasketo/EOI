#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Programa que pregunta cuántos números se van a introducir, pide esos números, y dice al final cuántos han sido pares y cuántos impares.

print("CONTADOR DE PARES E IMPARES")

valores = int(input("¿Cuántos valores vas a introducir? "))

if valores <= 0:
  print("Debes introducir enteros positivos.")
else:
  pares = 0
  for i in range(1, valores + 1):
      numero = int(input('Escribe el valor: '))
      if numero % 2 == 0:
          pares += 1

  print('Has escrito', pares,  'números pares y', valores - pares, 'números impares.')


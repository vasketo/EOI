#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Muestra el funcionamiento de los iteradores.

# Recorrer los caracteres de una cadena:

cadena = "Python"
for caracter in cadena:
    print("\t ", caracter, end = ' ')

# Recorrer caracteres de cadena anterior, en sentido inverso.

print ("\n")

for caracter in cadena[::-1]:
    print("\t", caracter, end = ' ')

# Recorrer los elementos de una lista

lista = ['una', 'lista', 'es', 'un', 'iterable']
for palabra in lista:
    print("\n", palabra)

# Recorrer los elementos de la lista anterior, al revés

for palabra in lista[::-1]:
    print(palabra)

# Obtener índice para recorrer todos los elementos de la lista

for indice in range(len(lista)):
    print (indice, lista[indice])

# Recorrer las claves de un diccionario

artistas = { 'Lorca' : 'Escritor', 'Goya' : 'Pintor'}
for clave, valor in artistas.items():
    print(clave ,':' ,valor)

# Itero entre un rango de números de 1 al 10
for elemento in range(1, 11):
    print(elemento, end=' ')  # 1 2 3 4 5 6 7 8 9 10

print ("\n")

# Itero entre un rango de números de 1 al 10 inverso
for elemento in range(10, 0, -1):
    print(elemento, end=' ')  # 10 9 8 7 6 5 4 3 2 1
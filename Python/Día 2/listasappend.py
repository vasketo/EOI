#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Este programa muestra cómo añadir un elemento de una lista.

country_names = []

while True:
    print('Introduce el nombre del país que deseas añadir la lista o no introduzcas nada para finalizar:')
    country = input()
    if country == '':
        break
    country_names.append(country) # Agrego el elemento a la lista.
print('Los países introducidos son:')
for country in country_names:
    print(' ' + country)
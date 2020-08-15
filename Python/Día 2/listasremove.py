#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Este programa muestra cómo eliminar un elemento de una lista.

country_names = ['España', 'Francia', 'Italia', 'Alemania', 'Noruega', 'Suecia', 'Canadá']

print('Los países disponibles son:')
for country in country_names:
    print(' ' + country)

while True:
    print('Introduce el nombre del país que deseas eliminar de la lista o no introduzcas nada para finalizar:')
    country = input()
    if country == '':
        break
    country_names.remove(country) # Elimino el elemento de la lista.

print('Los países restantes son:')
for country in country_names:
    print(' ' + country)
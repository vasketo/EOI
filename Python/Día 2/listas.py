#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Este programa muestra cómo utilizar las listas.

countries = ['Mexico', 'Colombia', 'Uruguay', 'Panama', 'Ecuador', 'Bolivia', 'Argentina']

print ('Los valores de la lista son:', countries)

print ('La lista tiene', len(countries), 'elementos.')

print (countries[0])
print (countries[1])
print (countries[-2])
print (countries[-1])
print (countries[6])

countries.append('Nicaragua') #Añado un elemento a la lista.

print (countries)

countries.sort() # Ordeno la lista.
print ('Los valores de la lista ordenada son:', countries)








#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Este programa muestra cómo utilizar las tuplas.

countries = ('Mexico', 'Colombia', 'Uruguay', 'Panama', 'Ecuador', 'Bolivia', 'Argentina')

print ('Los valores de la tupla son:', countries)
print ('La tupla tiene', len(countries), 'elementos.')

print('El último elemento de la tupla es: ', countries[-1])  # Para acceder al último elemento de la tupla
print('El peúltimo elemento de la tupla es: ', countries[-2])  # Para acceder al penúltimo elemento de la tupla
print('Los 3 primeros elementos de la tupla son: ', countries[:3])  # Para mostrar los 3 primeros elementos de la tupla
print('Los elementos de la tupla del tercero en adelante son: ', countries[2:])  # Para mostrar los elementos desde el tercer elemento hasta el final

# Convierto la tupla en una lista para que sea mutable.
print (type(countries))
countries = list(countries)
print (type(countries))
countries.append('Nicaragua') #Agrego un elemento a la lista.
print ('Los valores de la lista son:', countries)
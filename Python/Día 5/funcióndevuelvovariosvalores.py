#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Muestra el funcionamiento de una función en python. La función devuelve 2 valores.

def elemento_quimico(simbolo):
    # Devuelve número atómico y denominación del elemento

    elementos = {'H': '1-Hidrógeno', 'He': '2-Helio', 'Li': '3-Litio'}
    elemento = elementos[simbolo]
    lista = elemento.split('-')
    return lista[0], lista[1]

try:
    num_atomico, nombre = elemento_quimico('He')
    print('Núm. Atómico:', num_atomico)
    print('Denominación:', nombre)

except Exception as mensaje_de_error:
    print(str(mensaje_de_error))

#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# El DNI (Documento Nacional de Identidad) en España está formada por 8 números y una letra. La letra nos sirve para
# verificar que el número es correcto, por lo tanto la letra se calcula a partir del número. Busca información de cómo
# se realiza el calculo y crea una función CalcularLetra que recibe un número y devuelva la letra que le corresponde.
#
# La función anterior la podemos utiliza para crear una nueva función ValidarDNI que recibe un DNI (cadena de caracteres
# con 8 números y una letra) que valida el DNI, es decir comprueba si la letra del DNI ces igual a la letra calculada
# a partir del número.
#
# Realiza un programa principal que lea un DNI y valide que es correcto (se debe comprobar también que tiene
# 9 caracteres).

# Función CalcularLetra: Recibe un número de DNI, devuelve la letra correspondiente.
# Para calcular la letra se divide el número entre 23 y el resto indica la posición
# de una lista de letras que hemos guardado en una cadena.
# Parámetros de entrada: Número de dni
# Dato devuelto: La letra calculada

def CalcularLetra(num):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[num % 23]

# Función ValidarDNI: Recibe un DNI cadena de caracteres (números y letra), devuelve
# si el DNI es valido o no. Para saber si el válido se utiliza la función
# CalcularLetra con el número del DNI y se comprueba si la letra calculada coincide
# con la letra del DNI.
# Parámetros de entrada: DNI
# Dato devuelto: Valor lógico Verdadero si el DNI es válido o Falso en caso contrario.

def ValidarDNI(dni):
    letra = dni[8]
    num = int(dni[:8])
    return letra.upper() == CalcularLetra(num)

# Realiza un programa principal que lea un DNI y valide que es correcto (se debe
# comprobar también que tiene 9 caracteres).

try:

    midni = input("DNI:")
    # Mienstras el dni sea inválido o su longitud no sea de 9 caracteres,
    # vuelvo a pedirlo.
    while not ValidarDNI(midni) or len(midni) != 9:
        print("Error en el DNI")
        midni = input("DNI:")
    print("DNI correcto")

except Exception as mensaje_de_error:
    print(str(mensaje_de_error))
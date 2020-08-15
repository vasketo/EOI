#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Realice un programa que pregunte aleatoriamente una multiplicación entre 2 números entre 1 y 9.
# El programa debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea incorrecta el programa
# debe indicar cuál es la correcta).
# El programa preguntará 5 multiplicaciones, y al finalizar mostrará el número de aciertos.

# Hacemos un bucle con 5 iteraciones, en cada iteración se inicializan dos
# números con un valor aleatorio (de 1 a 9). Se calcula la multiplicación.
# Mostramos la multiplicación, y pedimos por teclado el resultado. Si coincide
# con la multiplicación calculada cuento un acierto, sino escribimos un mensaje
# de error mostrando el resultado correcto. Cuando salimos del bucle mostramos
# el número de aciertos x 2.

import random

aciertos = 0

for indice in range(1,6):

    # Genero dos números aleatorios
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)

    # Calculo la multiplicación
    resultado = num1*num2

    # Mostramos la operación de multiplicar y pedimos al usuario que indique el resultado.
    print("Multiplicación ",indice)
    print(f"{num1} * {num2} = ", end='')
    num_usuario = int(input())

    # Si acierta incrementamos el número de aciertos.
    if num_usuario == resultado:
        aciertos += 1
    else:
        # Si no acierta muestro la respuesta correcta.
        print("No has acertado. La respuesta es ",resultado)

# Mostramos el número de aciertos
print("Tu nota ha sido: ",aciertos * 2)

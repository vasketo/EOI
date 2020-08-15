# -*- encoding: utf-8 -*-

# Ejercicio que a partir de un mensaje lo cifra utilizando el cifrado césar.

# Abecedario a utilizar en el cifrado
abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

texto  = input("Introduce el texto a cifrar: ").upper()
desplazamiento = int(input("Valor de desplazamiento: "))
texto_cifrado = ""

for letra in texto:

    if letra in abc:

        # Buscamos la posición en la que se encuentra la letra que queremos cifrar.
        pos_letra = abc.index(letra)

        # Sumamos para movernos a la derecha del abc.
        nueva_pos = (pos_letra + desplazamiento) % len(abc)

        #Concatenamos cada una de las letras del mensaje una vez cifradas.
        texto_cifrado += abc[nueva_pos]
    else:
        texto_cifrado += letra

print("Texto cifrado: ", texto_cifrado)


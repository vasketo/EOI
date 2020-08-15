# -*- encoding: utf-8 -*-

# Ejercicio que a partir de un mensaje lo descifra utilizando el cifrado césar.

# Abecedario a utilizar en el cifrado
abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

texto  = input("Introduce el texto a descifrar: ").upper()
desplazamiento = int(input("Valor de desplazamiento: "))
texto_descifrado = ""

for letra in texto:

    if letra in abc:

        # Buscamos la posición en la que se encuentra la letra que queremos cifrar.
        pos_letra = abc.index(letra)

        # Restamos para movernos a la izquierda del abc.
        nueva_pos = (pos_letra - desplazamiento) % len(abc)

        #print("COMPRUEBO LETRA", letra)
        #print ("Pos Actual", pos_letra)
        #print ("Desplazamiento", desplazamiento)
        #print ("Nueva pos", nueva_pos)
        #print ("Nueva letra", abc[nueva_pos])

        #Concatenamos cada una de las letras del mensaje una vez cifradas.
        texto_descifrado += abc[nueva_pos]
    else:
        texto_descifrado += letra

print("Texto descifrado: ", texto_descifrado)


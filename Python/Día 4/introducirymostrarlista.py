# -*- encoding: utf-8 -*-

# Pide por teclado los números de una lista de uno en uno hasta que se introduzca la S de salir.
# Introducir en la lista únicamente aquellos números que no hayan sido previamente introducidos.
# En el caso de que haya sido previamente introducido, el programa debe indicar que el número ya está en la lista,
# indicando en qué posición.

numeros = []

while True:

    num = input("Escribe un número (Para dejar de introducir números escribir S): ").upper()

    if num == "S":
        break
    else:

        if int(num) not in numeros:
            numeros.append(int(num))
        else:
            print("El número", num, "ya se encuentra en la lista en la posición", numeros.index(int(num)), end=".\n")

print ("La lista contiene", len(numeros),  "números:", ",".join(str(num) for num in numeros), end=".")
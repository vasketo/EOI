# -*- encoding: utf-8 -*-

# Escribe un programa que pregunte por una muestra de números, separados por comas, los guarde en una tupla
# y muestre por pantalla su media. Posteriormente, que solicite otro número por pantalla, lo añada a la tupla
# y vuelva a calcular la media.


numeros = input("Introduce una muestra de números separados por comas: ")
numeros = numeros.split(',')
cantidad = len(numeros)

for i in range(cantidad):
    numeros[i] = int(numeros[i])

numeros = tuple(numeros)

print('La media de sumar', "+".join(str(num) for num in numeros),'y dividirlo entre', len(numeros), 'es', sum(numeros)
      / len(numeros), end=".")

num = int(input("\nIntroduce un número para añadir a la tupla: "))

# Convierto la tupla a lista.
print (type(numeros))
numeros = list(numeros)
print (type(numeros))
numeros.append(num)

print('La media de sumar', "+".join(str(num) for num in numeros),'y dividirlo entre', len(numeros), 'es', sum(numeros)
      / len(numeros), end=".")
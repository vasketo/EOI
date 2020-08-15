# -*- encoding: utf-8 -*-

# Escribe un programa que pregunte al usuario los números ganadores de la lotería primitiva (6),
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numpremiados = []
for i in range(6):
    numpremiados.append(input("Introduce el número {}: ".format(i+1)))
numpremiados.sort()
print("Los números ganadores ordenados de menor a mayor son", " ".join(numpremiados) + ".")
numpremiados.sort(reverse=True)
print("Los números ganadores ordenados de mayor a menor son", " ".join(numpremiados) + ".")
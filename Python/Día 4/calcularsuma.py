# -*- encoding: utf-8 -*-

# Escribe un programa que muestre el sumatorio de todos los números entre el 0 y un número introducido
# por el usuario por pantalla.

num = int(input("Introduce un número para calcular la suma de todos los números comprendindos entre 0 \
y el número indicado: "))

suma = 0

for i in range(num+1):
    suma += i

print("El sumatorio de los números comprendidos entre 0 y",num,'es',suma, end=".")
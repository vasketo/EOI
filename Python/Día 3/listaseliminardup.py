# -*- encoding: utf-8 -*-

# Escribe un programa que a partir de una lista con 10 elementos numéricos, elimine los duplicados y muestre
# los elementos únicos por pantalla, indicando previamente la cantidad de elementos de la lista y la cantidad una vez
# que se hayan eliminado los duplicados. Así mismo, se debe mostrar el elemento mayor y menor de la lista, y mostrar
# el valor de la suma de todos los elementos y el valor medio. Finalmente, en el caso de que el valor medio sea mayor
# que 30 se mostrará un mensaje, en el caso de que sea mayor 20 se mostrará otro mensaje, en el caso de que sea mayor
# que 10 se mostrará otro mensaje y finalmente si es menor o igual que 10 se mostrará otro mensaje.

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print ("La lista inicial tiene", len(nums), "elementos.")
nums_final = (list(set(nums)))
print ("Una vez eliminados los elementos duplicados la lista tiene", len(nums_final), "elementos.")

# Muestro el número mayor y menor de la lista.
print("El número mayor de la lista es", max(nums))
print("El número menor de la lista es", min(nums))

# Calculo la suma de todos los elementos y la media.
print ("La suma de los elementos de la lista es:", sum(nums))
print ("La media de los elementos de la lista es:", sum(nums)/len(nums))


if sum(nums)/len(nums) > 30:
    print("La media es mayor que 30.")
elif sum(nums)/len(nums) > 20:
    print("La media es mayor que 20.")
elif sum(nums)/len(nums) > 10:
    print("La media es mayor que 10.")
else:
    print("La media es menor o igual que 10")
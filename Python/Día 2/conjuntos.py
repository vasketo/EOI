#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Muestra el funcionamiento de los conjuntos.

# Declaro un conjunto de elementos.
countries = {"Mexico", "Colombia", "Uruguay", "Panama"}

print(countries) # Muestro todos los elementos del conjunto.

# Compruebo si un elemento existe en el conjunto.
print("Colombia" in countries)
print("Holanda"  in countries)

countries.add("Costa Rica") # Añado un elemento al conjunto.
countries.add("Panama") # Añado un elemento al conjunto.
print(countries)

# Añado varios elementos a la vez al conjunto.
countries.update(["Brasil", "Argentina", "Chile", "Bolivia"])
print(countries)

# Obtengo el número de elementos del conjunto.
print("El conjunto tiene", len(countries), "elementos.")

# Elimino un elemento del conjunto.
#countries.remove("Perú") # Si el elemento no existe, el método remove devolverá un error.
countries.discard("Perú") # Si el elemento no existe, el método discard no devolverá un error.

# Vacío el conjunto.
countries.clear()
print(countries)

# Elimino completamente el conjunto.
del countries

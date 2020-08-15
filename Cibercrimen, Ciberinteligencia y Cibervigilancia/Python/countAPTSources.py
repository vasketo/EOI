# -*- coding: utf-8 -*-

# Count APT Notes' Sources.

import requests

URL_DATA = "https://raw.githubusercontent.com/aptnotes/data/master/APTnotes.json"

resp = requests.get(URL_DATA)

informes = resp.json()

# Extraigo los Sources
list_sources = []
for informe in informes:
    list_sources.append(informe["Source"])

# Obtengo los Sources únicos
set_sources = set(list_sources)

# Inicializo el array bidimensional que los elementos que contendrá.
w, h = 2, len(set_sources)
sources = [[0 for x in range(w)] for y in range(h)]

# Reemplazo los valores inicializados con los valores reales.
pos = 0
for source in set_sources:
    cantidad = list_sources.count(source)
    sources[pos][0] = source
    sources[pos][1] = cantidad
    pos += 1

# Ordeno el array bidimensional por el segundo campo de manera inversa.
sources.sort(key = lambda x: x[1], reverse=True)

# Muestro por pantalla.
for pos, source in enumerate(sources):
    print(f"{pos+1}. {' '.join(str(campo) for campo in source)}")

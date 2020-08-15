# -*- coding: utf-8 -*-

# GET URLHaus Labels.

import requests

URL_DATA = "https://urlhaus.abuse.ch/downloads/csv_online/"

resp = requests.get(URL_DATA)

urls = list(resp.text.split("\n"))
del urls[:9] # Elimino los elementos de la cabecera.

labels = []

for url in urls:

    try:

        campos = url.split("\",\"")

        labels_aux = campos[5].split(",")

        for label_aux in labels_aux:

            if label_aux.strip() not in labels:
                labels.append(str(label_aux).strip())
    except:
        pass

labels = sorted(labels, key=str.casefold)

for label in labels:
    print(label)


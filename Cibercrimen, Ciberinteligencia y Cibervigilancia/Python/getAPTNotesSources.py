# -*- coding: utf-8 -*-

# GET APT Notes' Sources.

import requests

URL_DATA = "https://raw.githubusercontent.com/aptnotes/data/master/APTnotes.json"

resp = requests.get(URL_DATA)

informes = resp.json()

sources = []

for informe in informes:

    if informe["Source"] not in sources:
        sources.append(informe["Source"])

sources = sorted(sources, key=str.casefold)

for source in sources:
    print(source)

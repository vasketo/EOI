# -*- coding: utf-8 -*-

# GET Emotet URLs from URLHaus.

import requests

URL_DATA = "https://urlhaus.abuse.ch/downloads/csv_online/"

resp = requests.get(URL_DATA)

urls = list(resp.text.split("\n"))

print(f"Hay {len(urls)} de malware.")

for url in urls:
    if url.find("emotet") != -1:
        campos = url.split("\",\"")
        print(campos[1].split()[0],campos[2].replace("http","hxxp").replace(".","[.]"), campos[5])
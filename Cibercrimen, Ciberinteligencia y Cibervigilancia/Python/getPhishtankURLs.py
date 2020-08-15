# -*- coding: utf-8 -*-

# GET URLs from Phishtank.

import requests

URL_DATA = "http://data.phishtank.com/data/online-valid.json"

resp = requests.get(URL_DATA)

urls = resp.json()

print(f"Hay {len(urls)} urls de phishing.")

targets = []

for url in urls:
    if url['target'].capitalize() not in targets:
        targets.append(url['target'].capitalize())

targets.sort()

print("\n".join(target for target in targets))
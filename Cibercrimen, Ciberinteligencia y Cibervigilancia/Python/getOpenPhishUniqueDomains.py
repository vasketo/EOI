# -*- coding: utf-8 -*-

# GET Unique hostnames from OpenPhish

import requests

URL_DATA = "https://openphish.com/feed.txt"

resp = requests.get(URL_DATA)

urls = list(resp.text.split("\n"))

print(f"Hay {len(urls)} urls de phishing.")

urls_unicas = []

for url in urls:

    url = url.replace("https://","")
    url = url.replace("http://", "")
    url = str(url).lower()
    url = url.split("/")

    if url[0] not in urls_unicas:
        urls_unicas.append(url[0])

urls_unicas.sort()

print("Hay", len(urls_unicas), "urls únicas.")

print("\n".join(url_unica.replace(".", "[.]") for url_unica in urls_unicas))



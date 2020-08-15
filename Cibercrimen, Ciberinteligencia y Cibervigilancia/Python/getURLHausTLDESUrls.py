# -*- coding: utf-8 -*-

# GET TLD .ES Phishing URLs

import requests

URL_DATA = "https://urlhaus.abuse.ch/downloads/text_online/"

resp = requests.get(URL_DATA)

urls = list(resp.text.split("\n"))

print(f"Hay {len(urls)} de phishing.")

for url in urls:
    if url.find(".es/") != -1 or url.find(".es\n") != -1:
        print(url.replace("http","hxxp").replace(".","[.]"))


# -*- coding: utf-8 -*-

# GET Last 24 hour hashes from Malshare.

import requests

URL_DATA = "https://www.malshare.com/daily/malshare.current.txt"

resp = requests.get(URL_DATA)

print("\n".join(linea for linea in resp.text.split("\n")))






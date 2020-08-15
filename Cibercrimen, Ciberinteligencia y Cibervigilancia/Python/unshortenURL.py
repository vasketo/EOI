# -*- coding: utf-8 -*-

# Unshort URL

import requests
url = "shorturl.at/dzIUV"
url_check = "https://unshorten.me/json/" + url
resp = requests.get(url_check)

info = resp.json()

print (f"El enlace {url} redirige a {info['resolved_url']}.")
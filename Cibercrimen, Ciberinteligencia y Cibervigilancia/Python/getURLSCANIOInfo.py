# -*- coding: utf-8 -*-

# GET URL Analysis from urlscan.io.

import requests
import json

# Compruebo si la URL ha sido analizada.
url = "secure.runescape.com-as.ru"
url_check = "https://urlscan.io/api/v1/search/?q=domain:" + url
resp = requests.get(url_check)

print (json.dumps(resp.json(), indent=2, sort_keys=True))

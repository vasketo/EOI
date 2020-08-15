# -*- coding: utf-8 -*-

# GET HIBP verified entries.

import requests

URL_DATA = "https://haveibeenpwned.com/api/v2/breaches"

resp = requests.get(URL_DATA)

leaks = resp.json()

pos = 0
for leak in leaks:

    if leak['IsVerified']:
        print(f"{pos+1}. {leak['Title']} ({leak['BreachDate']}): {leak['PwnCount']} afectados.")
        pos += 1

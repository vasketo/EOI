# -*- coding: utf-8 -*-

# Get Get URL report.

import requests

url = 'https://www.virustotal.com/vtapi/v2/url/report'
url_analizar = 'https://www.phishtank.com'

params = {'apikey': '', 'resource':url_analizar}

response = requests.get(url, params=params)

info = response.json()

print (f"La url {url} fue analizada por última vez el {info['scan_date']}, siendo detectada por un "
       f"{round(info['positives']/info['total'],2)}% de los antivirus ({info['positives']} de {info['total']}).")

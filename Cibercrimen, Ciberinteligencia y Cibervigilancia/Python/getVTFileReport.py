# -*- coding: utf-8 -*-

# Get VT File Report.

import requests

url = 'https://www.virustotal.com/vtapi/v2/file/report'

params = {'apikey': '', 'resource': 'cf9c74ed67a4fbe89ab77643f3acbd98b14d5568'}

response = requests.get(url, params=params)
info = response.json()

print (f"El fichero con md5 {info['md5']} tiene {info['positives']} detecciones.")

for scan in info['scans']:
    print (f"{scan}: {info['scans'][scan]['result']}")


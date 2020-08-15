# -*- coding: utf-8 -*-

# Get ReAnalyze and VT File Report.

import requests
import time

url = 'https://www.virustotal.com/vtapi/v2/file/rescan'

params = {'apikey': '', 'resource': '99017f6eebbac24f351415dd410d522d'}

response = requests.post(url, params=params)

time.sleep(30)

url = 'https://www.virustotal.com/vtapi/v2/file/report'

params = {'apikey': '', 'resource': '99017f6eebbac24f351415dd410d522d'}

response = requests.get(url, params=params)
info = response.json()

print (f"El fichero con md5 {info['md5']} y sha1 {info['sha1']} tiene {info['positives']} detecciones.")



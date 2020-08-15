# -*- coding: utf-8 -*-

# Send file

import requests

url = 'https://www.virustotal.com/vtapi/v2/file/scan'

params = {'apikey': ''}

files = {'file': ('nohat3-190920073429.pdf', open('nohat3-190920073429.pdf', 'rb'))}

response = requests.post(url, files=files, params=params)

print(response.json())
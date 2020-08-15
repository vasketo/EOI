# -*- coding: utf-8 -*-

# GET Report from Hybrid Analysis

import requests
import json

sha256 = '4170f59814766a19c5fbfe38043e4562e26a402382ff0ec78a05b228988547cc'
url = 'https://www.hybrid-analysis.com/api/v2/overview/' + sha256

headers = {'api-key': '', 'user-agent': 'Falcon'}

response = requests.get(url, headers=headers)

print (json.dumps(response.json(), indent=2, sort_keys=True))

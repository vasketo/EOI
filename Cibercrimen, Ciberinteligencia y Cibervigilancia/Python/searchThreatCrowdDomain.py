# -*- coding: utf-8 -*-

# Search domain info in ThreatCrowd.

import requests, json

domain = 'aoldaily.com'
result =  requests.get('https://www.threatcrowd.org/searchApi/v2/domain/report/', params = {"domain": domain})

info = json.loads(result.text)

print(f"El dominio {domain} tiene {len(info['subdomains'])} subdominios asociados:")

if info['response_code'] == '1':
    print("\n".join(subdomain.replace("http","hxxp").replace(".","[.]") for subdomain in info['subdomains']))
# -*- coding: utf-8 -*-

# Search MD5 info in ThreatCrowd.

import requests, json

#https://www.threatcrowd.org/searchApi/v2/file/report/?resource=ec8c89aa5e521572c74e2dd02a4daf78
result =  requests.get('https://www.threatcrowd.org/searchApi/v2/file/report/', params = {"resource": 'ec8c89aa5e521572c74e2dd02a4daf78'})

info = json.loads(result.text)

if info['response_code'] == '1':

    print("Número de detecciones", len(info['scans']))
    print ("\n".join(scan for scan in info['scans']))

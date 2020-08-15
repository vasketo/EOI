# -*- coding: utf-8 -*-

# Search IP info in ThreatCrowd.

import requests, json

ip = '188.40.75.132'
result =  requests.get('https://www.threatcrowd.org/searchApi/v2/ip/report/', params = {"ip": ip})

info = json.loads(result.text)

if info['response_code'] == '1':

    print (f"La ip: {ip} tiene los siguientes ficheros asociados:")

    for fichero in info['hashes']:

        result = requests.get('https://www.threatcrowd.org/searchApi/v2/file/report/', params={"resource": fichero})

        info = json.loads(result.text)

        if info['response_code'] == '1':
            print (f"El fichero: {fichero} tiene {len(info['scans'])} detecciones:", ", ".join(scan for scan in info['scans']))


# -*- coding: utf-8 -*-

# GET LAST 10 Vulnerabilities from CIRCL list.

import requests

URL_DATA = "http://cve.circl.lu/api/last/10"
resp = requests.get(URL_DATA)

vulnerabilities = resp.json()

for pos, vulnerability in enumerate(vulnerabilities):
    print(f"{pos+1}. {vulnerability['id']} ({vulnerability['cvss']}): {vulnerability['summary']}.")



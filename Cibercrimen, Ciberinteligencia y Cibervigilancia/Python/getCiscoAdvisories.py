# -*- coding: utf-8 -*-

# GET Cisco Advisories.

import requests
import xml.etree.ElementTree as ET

def normalizar (text):
    return text.replace("\n","").strip()

URL_DATA = "https://tools.cisco.com/security/center/psirtrss20/CiscoSecurityAdvisory.xml"
resp = requests.get(URL_DATA)

advisories = ET.fromstring(resp.text)

for pos, advisory in enumerate(advisories.iter('item')):
    print(f"{pos+1}. {advisory.find('title').text} ({advisory.find('pubDate').text}): {normalizar(advisory.find('description').text)}")





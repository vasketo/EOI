# -*- coding: utf-8 -*-

# GET Zero Day Initiative Advisories.

import requests
import xml.etree.ElementTree as ET

URL_DATA = "https://www.zerodayinitiative.com/rss/upcoming/"
resp = requests.get(URL_DATA)

advisories = ET.fromstring(resp.text)

for pos, advisory in enumerate(advisories.iter('item')):
    print(f"{pos+1}. {advisory.find('title').text}: {advisory.find('description').text.split('<')[0][-4:]}")

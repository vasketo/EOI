# -*- coding: utf-8 -*-

# Crawl INCIBE Alerts.

import requests
from bs4 import BeautifulSoup

url_page = 'https://www.incibe.es/protege-tu-empresa/avisos-seguridad'

page = requests.get(url_page).text
soup = BeautifulSoup(page, "lxml")

titulos = soup.find_all(attrs={"class": "node-title"})

for titulo in titulos:
    print(titulo.text.strip())
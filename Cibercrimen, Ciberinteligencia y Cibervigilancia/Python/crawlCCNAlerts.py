# -*- coding: utf-8 -*-

# Crawl CCN-CERT Alerts.

import requests
from bs4 import BeautifulSoup

url_page = 'https://www.ccn-cert.cni.es/seguridad-al-dia/alertas-ccn-cert.html'

page = requests.get(url_page).text
soup = BeautifulSoup(page, "lxml")

tabla = soup.find("table", attrs={"class": "category table table-striped table-bordered table-hover"})

tabla_contenido = tabla.find('tbody')

filas = tabla_contenido.find_all('tr')

for fila in filas:
    print(fila.find_all('td')[0].text.strip())

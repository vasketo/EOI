# -*- coding: utf-8 -*-

# Crawl US-CERT Alerts.

import requests
from bs4 import BeautifulSoup

url_page = 'https://us-cert.cisa.gov/ncas/alerts'

page = requests.get(url_page).text
soup = BeautifulSoup(page, "lxml")

div = soup.find("div", attrs={"class": "item-list"})
div_ul = div.find_all("ul")

for li in div_ul[0].find_all("li"):
    print(li.text.replace("\n",""))


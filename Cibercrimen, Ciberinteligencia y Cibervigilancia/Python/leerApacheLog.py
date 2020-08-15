# -*- coding: utf-8 -*-

# Read Apache Log

with open('logs/apache.log', 'r') as f:
    for linea in f:
        if linea.find("q123wdesadas") != -1:
            linea = linea.split("\"")
            fecha = linea[0].split("-")[2][2:-2]
            url = linea[1].split()[1]
            print(f"{fecha} : {url}")

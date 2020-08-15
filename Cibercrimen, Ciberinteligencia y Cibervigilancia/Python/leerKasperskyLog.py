# -*- coding: utf-8 -*-

# Read Kaspersky Log
with open('logs/scan_report.txt', 'r') as f:
    for linea in f:
        if linea.find("Infected: ") != -1:
            linea = linea.split("	")
            print(f"Ruta: {linea[0]} - {linea[1].replace('Infected: ','Malware: ')}")
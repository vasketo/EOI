# -*- coding: utf-8 -*-

# Read Port Scanner Log

with open('logs/portscanner.log', 'r') as f:
    for linea in f:
        registro = linea.split(":")
        print(f"La IP {registro[0]} tiene el puerto {registro[1]} abierto.")
# -*- coding: utf-8 -*-

# Read Apache Log

with open('logs/apache.log', 'r') as f:
    for linea in f:
        if linea.find("wp-admin") != -1 and linea.find("GET") != -1 and linea.find("200") != -1:
            print(linea)
            break
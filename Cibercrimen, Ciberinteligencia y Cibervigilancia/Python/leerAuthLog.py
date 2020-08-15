# -*- coding: utf-8 -*-

# Read Auth Log

with open('logs/auth.log', 'r') as f:
    for linea in f:
        campos = linea.split()

        if campos[4].find("useradd") != -1 and campos[5].find("new") != -1 and campos[6].find("user:") != -1:
            # Manera 1
            print(" ".join(campo for campo in campos[:3]), end=" ")
            print (" ".join(campo for campo in campos[4:]))

            # Manera 2
            #print(linea.replace("ubuntu1604",""))

            # Manera 3
            #print("".join(valor for valor in linea.split("ubuntu1604")))


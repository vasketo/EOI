# -*- coding: utf-8 -*-

# Read SysLog

estados = ['<emerg>', '<alerta>', '<crit>', '<err>', '<warn>']

with open('logs/syslog', 'r') as f:
    for linea in f:
        campos = linea.split()

        if campos[5] in estados:

            print(" ".join(campo for campo in campos[5:]))



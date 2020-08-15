# -*- coding: utf-8 -*-

# Read IP Tables Log

from datetime import datetime
ips = []

# Obtengo el listado único de direcciones IP a las que ha habido conexiones desde nuestra infraestructura.

ipmaliciosa = "95.169.186.78"

with open('logs/iptables.log', 'r') as f:
    for linea in f:
        campos = linea.split()

        if "output" in campos[7]:
            dst = campos[11][5:]
            #dst = linea[linea.find("DST=")+4:linea.find(" ", linea.find("DST="))]
            if dst not in ips:
                ips.append(dst)

ips.sort()

print("Ha habido conexiones a las siguientes direcciones IP:")
print("\n".join(ip for ip in ips))

print("======================================")

# Comprueblo las conexiones que ha habido a esa IP maliciosa.

with open('logs/iptables.log', 'r') as f:
    for linea in f:
        campos = linea.split()

        if "output" in campos[7]:
            if ipmaliciosa in campos[11]:
                fecha = linea[:15]
                fecha = datetime.strptime(fecha, '%b %d %H:%M:%S').strftime("%d del %m a las %H:%M:%S")
                src = campos[10][5:]
                #src = linea[linea.find("SRC=") + 4:linea.find(" ", linea.find("SRC="))]
                print("El", fecha ,"se realizó conexión a la IP maliciosa", ipmaliciosa, "desde la IP", src)

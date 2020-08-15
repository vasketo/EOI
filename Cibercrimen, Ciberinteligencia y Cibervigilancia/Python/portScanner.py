# -*- encoding: utf-8 -*-

# Simple Port Scanner

from logging import getLogger, ERROR

getLogger("scapy.runtime").setLevel(ERROR)  # Oculto posibles errores
from scapy.all import *
import sys
from time import strftime


target = "192.168.1.1"
min_port = 20
max_port = 200

ports = range(int(min_port), int(max_port) + 1)  # Creo una lista con todos los puertos posibles.
SYNACK = 0x12 # Flag Puerto abierto.
RSTACK = 0x14 # Flag Puerto cerrado.


def checkhost(ip):  # Compruebo si la IP está en funcionamiento y activa.
    conf.verb = 0  # Oculto el output.
    try:
        ping = sr1(IP(dst=ip) / ICMP())  # Hago un ping.
        print("\n[*] La IP está asignada, Comienzo el análisis...")
    except Exception:  # Si el ping falla.
        print("\n[!] La IP no está asignada.")
        sys.exit(1)


def scanport(port):  # Función para escanear el puerto especificado.
    try:
        srcport = RandShort()  # Genero un número de puerto aleatorio.
        conf.verb = 0  # Oculto el output
        SYNACKpkt = sr1(
            IP(dst=target) / TCP(sport=srcport, dport=port, flags="S"))  # Envío SYN y recibo RST-ACK o SYN-ACK
        pktflags = SYNACKpkt.getlayer(TCP).flags  # Extraigo los flags del paquete recibido.
        if pktflags == SYNACK: # Comprueblo si está abierto o no.
            return True  # Devuelvo que está abierto.
        else:
            return False  # Devuelvo que está cerrado.
        RSTpkt = IP(dst=target) / TCP(sport=srcport, dport=port, flags="R")  # Contruyo un paquete RST en lugar de un ACK.
        send(RSTpkt)  # Envío el paquete RST.
    except Exception:
        sys.exit(1)

checkhost(target)  # Llamo a la función para comprobar si el HOST está activo.

print("[*] Comienzo el análisis a las " + strftime("%H:%M:%S") + "\n")

with open('logs/portscanner.log', 'w') as f: #Abro el fichero que almacenará el resultado.

    for port in ports:  # Recorro los puertos.
        status = scanport(port)  # Escaneo cada puerto.
        if status == True:  # Compruebo el resultado del escaneo.
            print(f"{target}:{port}:Open")  # Muestro por pantalla si el puerto está abierto.
            f.write(f"{target}:{port}:Open\n") # Guardo el resultado en un fichero.

print("\n[*] Escaneo finalizado.")

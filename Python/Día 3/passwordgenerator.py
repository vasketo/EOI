#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Simple generador de contraseñas

import random

caracteres = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
tam = 8
password =  "".join(random.sample(caracteres, tam))

print ("La contraseña generada es:", password)
#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Crear una función llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero
# si el nombre de usuario es “admin” y la contraseña es “123456”. Además recibe el número de intentos que se
# ha intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login,
# solamente tenemos tres oportunidades para intentarlo.

# Función Login: Recibe un nombre de usuario y una contraseña, y devuelve un
# valor lógico: verdadero si se ha introducido el nombre y la contraseña adecuadas.
# Además devuelve el numero de internos
# Parámetros de entrada: nombre y contraseña, y el número de intentos actual
# Datos devueltos: Valor lógico indicando si ha hecho login, e intentos

def Login(nombre,password,intentos):
    intentos += 1
    if nombre == "admin" and password == "123456":
        return True,intentos
    else:
        return False,intentos

intentos = 0

try:

    while True:

        usuario = input("Usuario: ")
        clave = input("Contraseña: ")
        entrar,intentos = Login(usuario,clave,intentos)

        if not entrar:
            print("Error. Nombre de usuario o contraseña incorrecta.")

        if entrar or intentos == 3:
            break
            # Sale si he hecho login o llego a los tres intentos
            # Puedo llegar a esta instrucción por dos razones
            # Si he hecho login muestro mensaje de bienvenida

    if entrar:
        print("Bienvenido al sistema")
    else: # He llegado a los tres intentos
        print("No has entrado en el sistema")

except Exception as mensaje_de_error:
    print(str(mensaje_de_error))
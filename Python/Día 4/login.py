# -*- encoding: utf-8 -*-

# Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “admin”
# y la contraseña es “123456”, mostrar en pantalla “Usuario y contraseña correctos, aunque deberías utilizar una
# contraseña más segura.”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado” y volver a preguntar
# por el nombre de usuario y la contraseña. Realizar el programa con una única condición.

while True:

    nombre = input("Nombre de usuario:")
    password = input("Contraseña:")
    if nombre == "admin" and password == "123456":
        print("\tUsuario y contraseña correctos, aunque deberías utilizar una contraseña más segura.")
        break
    else:
        print("\tAcceso denegado")

# -*- encoding: utf-8 -*-

# Escribe un programa que solicite por pantalla 2 números y realice su división.
# Maneja los errores que se te ocurran que pueden producirse como por ejemplo al introducir un 0 en el segundo número.

dividendo = float(input("Introduce el dividendo: "))
divisor = float(input("Introduce el divisor: "))

try:
    print("El resultado de dividir", dividendo,"entre",divisor,"es",dividendo/divisor)

except Exception as mensaje_de_error:

    print("Se ha producido un error:",str(mensaje_de_error))


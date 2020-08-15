#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# Ejercicio con operadores de identidad

a = 20
b = 10

print( "a =", a )
print( "b =", b )

if  a is b:
    print( "a y b son iguales" )
else:
    print( "a y b no son iguales" )

if  a is not b:
    print( "a es distinto de b" )
else:
    print( "a es igual a b" )

#!/usr/bin/env python

# -*- encoding: utf-8 -*-

#Ejercicio con operadores de membresía

a = 20
b = 10

nums = [1, 2, 3, 4, 5 ]

print ( "a =", a )
print ( "b =", b )
print ( "nums =", nums )

if ( a in nums ):
    print ( "a sí está en nums" )
else:
    print ( "a no está en nums" )
	
if ( b not in nums ):
    print ( "b no está en nums" )
else:
    print ( "b sí está en nums" )
	
c = a / b

if ( c in nums ):
    print ( "El resultado de a / b sí está en nums" )
else:
    print ( "El resultado de a / b no está en nums" )
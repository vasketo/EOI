# Escribe un programa que almacene los módulos que se imparten en un curso en una lista, solicite por pantalla
# 2 nuevos módulos # a añadir, los muestre por pantalla ordenados, solicite por pantalla 1 módulo a eliminar,
# contabilice el número de módulos del curso y los muestre por pantalla, y en el caso de que el módulo de Python
# esté incluido, muestre un mensaje que diga: “Que la fuerza te acompañe.”

# -*- encoding: utf-8 -*-

print ("\tCurso de Especialista en Ciberseguridad\n".upper())

modulos = ['Introducción a la ciberseguridad', 'Python', 'Bastionado de sistemas y gestión de la seguridad',
               'Ciberinteligencia, cibervigilancia y ciberterrorismo', 'Seguridad de sistemas',
               'Seguridad gestionada, threathuntig y pentest', 'Análisis de datos', 'Marco normativo y regulación']

print ("Las asignaturas del curso son", modulos, "\n")

# Solicito los módulos adicionales a incluir en la lista.
modulos_nuevos = [] #Declaro una nueva lista que almacenará los módulos nuevos.

modulo_nuevo1 = str(input("Introduce el primer módulo a añadir en la lista.\n"))
modulos_nuevos.append(modulo_nuevo1.capitalize())
modulo_nuevo2 = str(input("Introduce el segundo módulo a añadir en la lista.\n"))
modulos_nuevos.append(modulo_nuevo2.capitalize())

# Añado los nuevos módulos a la lista de módulos.
modulos.extend(modulos_nuevos)

# Ordeno la lista.
modulos.sort()
print("\n",modulos)

print("\nIntroduce el número del módulo que no quieras cursar.\n")
print("1. ", modulos[0])
print("2. ", modulos[1])
print("3. ", modulos[2])
print("4. ", modulos[3])
print("5. ", modulos[4])
print("6. ", modulos[5])
print("7. ", modulos[6])
print("8. ", modulos[7])
print("9. ", modulos[8])
print("10. ", modulos[9])

modulo_eliminar = int(input("\nMódulo: "))

# Elimino el módulo indicado.
print("\nSe procede a eliminar el módulo de", modulos[modulo_eliminar-1] + ".\n")
modulos.pop(modulo_eliminar-1)

# Contabilizo el número de elementos de la lista.
print("La lista módulos tiene",len(modulos),"elementos.\n")

if "Python" in modulos:
    print("Python es uno de los módulos que se van a impartir: \"Que la fuerza te acompañe\".")

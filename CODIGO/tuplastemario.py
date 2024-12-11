#!/usr/bin/python
#!/usr/bin/env python

import os

# Limpiamos la terminal antes de imprimir

os.system('cls' if os.name == 'nt' else 'clear')

print("TUPLAS")

# Tupla con valores separados por comas
tupla = 1, 2, 3, 4, 5

#Acceso a los valores de la tupla
print("Impresion de elementos de la tupla")
print(tupla[0])
print(tupla[2])

# Tupla con elementos mutables 
# Lista en una tupla
tupla_mutable = (1, 2, [3, 4, 5])
print("Impresion de elementos de la tupla mutable")
print(tupla_mutable)

# Modificamos el valor de la lista dentro de la tupla
tupla_mutable[2][1] = 6 # Se modifica el 4 por el 6
print("Impresion de la tupla mutable modificada")
print(tupla_mutable)

# Creamos una tupla anidada 

    # Tupla con tuplas
tupla_anidada =7, 'hola', (1, 2, (3, 4, 5))
print("Impresion de elementos de la tupla anidada")
print(tupla_anidada)
# IMprimimos 'hola' de la tupla anidada y el valor 4

print("Impresion de 'hola' y el valor 4 de la tupla anidada")

# Se accede a la tupla anidada
print(tupla_anidada[2][2])
print(tupla_anidada[2][2][1])
print(tupla_anidada[1])

# Tupla nueva a partir de otras dos 
tupla1 = 1,2,3,4
tupla2 = 5,6,7,8
tupla_nueva = tupla1 + tupla2
print("Impresion de la tupla1: ", tupla1)
print("Impresion de la tupla2: ", tupla2)
print("Impresion de la tupla nueva")
print(tupla_nueva)

# Crear tupla con un solo elemento
tupla_unica = ("Carmela",)
print("Impresion de la tupla unica: ", tupla_unica)

tupla_falsa = ("Carmela")
print(type(tupla_falsa), type(tupla_unica)) ## Se compueba en el valor de tipo que da el programa

# Convertimos tupla falsa en verdadera

tupla_verdadera = tuple(tupla_falsa)
print(type(tupla_verdadera))
tuplaVerdadera2 = (tupla_falsa, )
print(type(tuplaVerdadera2))

# Ordenamos la tupla 
tupla3 = (5, 2, 8, 1, 3)
tupla3_ordenada = sorted(tupla3)

print("Impresion de la tupla original: ", tupla3)
print("Impresion de la tupla ordenada: ", tupla3_ordenada)

# Usamos compresion para crear una tupla
tupla4 = (3,23,5,7,6,9)
tupla_cuadrados = tuple(x ** 2 for x in tupla4 if x > 3)
print("Resultado tupla cuadrados: ", tupla_cuadrados)

#!/usr/bin/python
#!/usr/bin/env python
# añadimos libreria para las operaciones matematicas

import math

""" probamos identacion en Python"""

A = 1
if A == 1:
    print("A es igual a 1")
    print("Test A es 1")
else:
    print("A no es igual a 1")
    print("Test A no es 1")

# Añadimos un comentario que siempre se imprimira
print("Esto siempre se imprimira")

# Probamos las operaciones en python 

    # Suma
print(2 + 2)

    # Resta
print(2 - 2)

# Creamos variables numericas que despues se utilizaran en operaciones
x = 1
y = 3
z = 5

print("La suma de x y y es: ", x + y)

print("La resta de x y y es: ", x - y)

# Creamos variables mas precisas 

numero = int("123") # Devuelve 123
numero2 = str(123) # Devuelve "123"
decimal = float("123") # Devuelve 123.0
decimal2 = float("123.45") # Devuelve 123.45
lista = list("12345") # Devuelve [1, 2, 3, 4, 5]
tupla = tuple("12345") # Devuelve (1, 2, 3, 4, 5)
diccionario = dict([(index, x) for index, x in enumerate("123")]) # Devuelve {'0': '1', '1': '2', '2': '3'}
bool("123") # Devuelve True

# Mostramos las variables precisas

print("numero: ", numero)
print("numero2: ", numero2)
print("decimal: ", decimal)
print("decimal2: ", decimal2)
print("lista: ", lista)
print("tupla: ", tupla)
print("diccionario: ", diccionario)
print("bool: ", bool)

# Probamos los operadores de comparacion    
print("x es mayor que y: ", x > y)
print("x es menor que y: ", x < y)
print("x es igual a y: ", x == y)
print("x es diferente de y: ", x!= y)

# Redondeamos los valores decimales 
print("Redondeo de 123.45: ", round(decimal2))

# Redondeamos hacia abajo los valores decimales
print("Redondeo hacia abajo de 123.45: ", math.floor(decimal2))

# Redondeamos hacia arriba los valores decimales
print("Redondeo hacia arriba de 123.45: ", math.ceil(decimal2))

# Eliminamos la parte decimal 
print("Eliminamos la parte decimal de 123.45: ", math.trunc(decimal2))

# Calculamos la raiz cuadrada de un numero
print("Raiz cuadrada de 16: ", math.sqrt(16))


# Creamos una cadena con concatenacion 
cadena1 = "Hola "
cadena2 = "Mundo!"
print(cadena1 + cadena2)

# Creamos una lista con concatenacion
lista1 = ["Hola", "Mundo"]
lista2 = ["!", "Hola"]
print(lista1 + lista2)

# Repetimos el valor Hola 5 veces 
print(5 * "Hola")

# Extraccion de caracteres de una cadena
valorcadena1 = "Carmela Hola!"
print("Caracter en la posicion 6: ", valorcadena1[5])
print("Caracter en la posicion 1: ", valorcadena1[0])

# Extraemos rangos de la cadena
print("Rango de la posicion 2 a la 5: ", valorcadena1[1:5])
print("Rango de la posicion 2 a la ultima posicion: ", valorcadena1[1:])
print("Rango de la posicion 0 a la 5: ", valorcadena1[:5])
print("Rango de la posicion 0 a la ultima posicion: ", valorcadena1[:])


# ponemos la cadena valorcadena1 en mayusculas
print("Valor cadena1 en mayusculas: ", valorcadena1.upper())

# ponemos la cadena valorcadena1 en minusculas
print("Valor cadena1 en minusculas: ", valorcadena1.lower())
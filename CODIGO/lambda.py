#!/usr/bin/python
#!/usr/bin/env python
import os

# Limpiamos la terminal antes de imprimir
os.system('cls' if os.name == 'nt' else 'clear')


print("EJEMPLOS LAMBDA")

# Ejemplo: ORDENAR LISTA DE TUPLAS
productos = [('Perro', 100), ('Gato', 50), ('Cerdo', 150)]
# Ordenamos por el segundo elemento de cada tupla (cantidad)
productos.sort(key=lambda x: x[1])

print("Productos ordenados por cantidad:")
print(productos)
# Orden descendente
productos.sort(key=lambda x: x[1], reverse=True)

print("Productos ordenados por cantidad (descendente):")
print(productos)

# Ejemplo filtrar y aplicar operaciones
# CASO DE USO: FILTRAR ELEMENTOS DE UNA LISTA 
# Obtenemos solo los pares 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))

print("Numeros pares:")
print(pares)

# Caso de uso: Realizar operaciones con cada elemento de una lista 
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)
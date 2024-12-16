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

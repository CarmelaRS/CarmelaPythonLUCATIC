#!/usr/bin/python
#!/usr/bin/env python
import os
import random

# Limpiamos la terminal antes de imprimir
os.system('cls' if os.name == 'nt' else 'clear')

# Creamos dos listas la primera con nombres de canciones y la segunda con duraciones de las canciones 

canciones = ['Hasta la próxima', 'Amor en el silencio', 'El amor de mi vida', 'Nunca más']
duraciones = ['4:07', '3:52', '3:50', '3:58']

# Combinamos las listas en un diccionario 
canciones_dict = dict(zip(canciones, duraciones))

print(canciones_dict)

# Ordenamos el diccionario con sorted() y guardamos las 3 con mayor duración 

canciones_dict_ordenadas = dict(sorted(canciones_dict.items(), key=lambda x: x[1], reverse=True)[:3])

print("\nLas 3 películas con mayor duración son:")
print(canciones_dict_ordenadas)

# Creamos un diccionario con una seleccion aleatoria de canciones 
seleccion_aleatoria = random.sample(list(canciones_dict.items()), 2)

print("\nSelección aleatoria de 3 canciones:")
print(seleccion_aleatoria)



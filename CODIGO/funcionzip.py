#!/usr/bin/python
#!/usr/bin/env python
import os

# Limpiamos la terminal antes de imprimir
os.system('cls' if os.name == 'nt' else 'clear')


print("FUNCION ZIP")

# Usamos la funcion ZIP para unir listas, tuplas, diccionarios, etc. 

# Creamos dos listas 
doctores = ['Dr. Alfonso', 'Dr. Maria', 'Dr. Juan']
especialidad = ['Cardiología', 'Neurología', 'Gastroenterología']

# Usamos la funcion zip para unir las listas
ziplist = zip(doctores, especialidad)

# Imprimimos los resultados
print("Doctores y especialidades:")
print("Opcion 1: ", list(ziplist))

# Imprimimos los resultados en otra forma

print("Opcion 2: ")
# Usamos un bucle for para imprimir los resultados (De esta forma recorremos en paralelo los elementos)
for doctor, especialidad in ziplist:
    print(f"{doctor} - Especialidad: {especialidad}")

print("===================================================================")

# Tambien se puede desunir elementos de varios tipos de datos
alimentos = [('Alitas de pollo', 'polleria'), ('Chorizo', 'Charcuteria'), ('Pan', 'panaderia')]

# Usamos la funcion zip para desunir los elementos
alimento, tienda = zip(*alimentos)

# Imprimimos los resultados
print('Alimentos: ', alimento)
print('Tiendas: ', tienda)

# Una vez se usa un zip se debe volver a crear otro, por ejemplo ahora no funcionara el zip de doctores y especialidades

print("Funcion ZIP despues de usarla -- El zip ya esta consumido")
print("Doctores y especialidades:")
print( list(ziplist))

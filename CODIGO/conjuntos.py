#!/usr/bin/python
#!/usr/bin/env python
import os

# Limpiamos la terminal antes de imprimir
os.system('cls' if os.name == 'nt' else 'clear')


print("CONJUNTOS - SETS")

# Conjuntos son colecciones desordenadas de elementos únicos

# Creacion de un conjunto vacío
mi_conjunto = set()

# Creacion de un conjunto con elementos repetidos
conjunto_ejemplo1 = {"Hola", "Mundo", "Hola", "Mundo", 1, 2, 3, 1, 2, 3}
print("Conjunto con repetidos:", conjunto_ejemplo1)

#Creación de un conjunto de helados 
helados = {"Chocolate", "Vainilla", "Fresa", "Nutela", "Chocolate negro"}
helados1 = {"Chocolate", "Vainilla", "Fresa", "Nutela", "Chocolate negro"}

#Copiamos un conjunto a otro
helados2 = helados.copy()

# Imprimimos los conjuntos de helados
print("Helados:", helados)
print("Copia de helados wth copy:", helados2)

# Mostramos los id de los conjuntos
print("ID del conjunto original:", id(helados))
print("ID de la copia:", id(helados2))
print("===================================================================")

# Si asignamos un set a una variale y sera el mismo
helados3 = helados1
print("Copia de helados con = :", helados3)
print("ID del conjunto copia:", id(helados3))
print(" Helados1: ", helados1)
print("ID Helados1: ", id(helados1))
print("===================================================================")

# Comprobamos si un helado está en el conjunto
print("Está 'Nutela' en el conjunto de helados?", "Nutela" in helados)
print("Está 'Vainilla' en el conjunto de helados?", "Vainilla" in helados)
print("===================================================================")

# Añadimos un nuevo helado al conjunto
helados.add("Dulce de leche")
print("Nuevos helados:", helados)

# Usamos update para añadir un nuevo helado si ya está en el conjunto
helados.update(["Fresa", "M&M", "Fudge"])
print("Nuevos helados con update:", helados)
print("===================================================================")

# Eliminamos un helado del conjunto
helados.remove("Fresa")
print("Helados sin 'Fresa':", helados)

# Usamos discard para eliminar un helado si está en el conjunto
helados.discard("Fudge")
print("Helados sin 'Fudge':", helados)

# Eliminamos usando pop para eliminar un helado al azar
helado_eliminado = helados.pop()
print("Helado eliminado:", helado_eliminado)
print("Helados restantes:", helados)
print("===================================================================")

print("IMPRIMIMOS LOS CONJUNTOS DE HELADOS Y HELADOS 2")
print("Helados: ", helados)
print("helados 2: ", helados2)
# UNION DE CONJUNTOS 
unionhelados = helados | helados2
print("Union de helados: ", unionhelados)

# INTERSECCION DE CONJUNTOS 
intersectionhelados = helados & helados2
print("Los helados repetidos son: ", intersectionhelados)

# DIFERENCIA DE CONJUNTOS
diffhelados = helados - helados2
print("Los helados que no están en helados2 son: ", diffhelados)

diffhelados1 = helados2 - helados
print("Los helados que no están en helados son: ", diffhelados1)

# DIFERENCIA SIMÉTRICA DE CONJUNTOS
diffheladosSimetrica = helados ^ helados2
print("Los helados que están en algún conjunto pero no en ambos son: ", diffheladosSimetrica)

print("============================ LIMPIEZAS DE CONJUNTOS ============================")
# Si eliminamos helados 1, helados 3 quedara vacio tambien 
helados1.clear()
print("CLEAR DE ELEMENTOS ASIGNADOS CON =  ")
print(helados1)
print(helados3)

print("CLEAR DE ELEMENTOS ASIGNADOS CON COPY()")
helados.clear()
print("Helados: ", helados)
print("helados 2: ", helados2)

print("===================================================================")
# Volvemos a añadir todos los valores al set helados 
helados = {"Chocolate", "Vainilla", "Fresa", "Nutela", "Chocolate negro"}
print(helados)
# Eliminamos todos los helados del conjunto
helados.clear()
print("Helados vacíos:", helados)






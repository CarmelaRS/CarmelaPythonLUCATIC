#!/usr/bin/python
#!/usr/bin/env python
import os

# Limpiamos la terminal antes de imprimir
os.system('cls' if os.name == 'nt' else 'clear')

# CASOS DE USO LISTAS
print("CASOS DE USO DE LISTAS")
# Creacion de una lista que se puede modificar -- Tema ideas de eventos solidarios
eventos = ["Concierto", "Exposicion", "Torneo"]

# Agregar un elemento a la lista
eventos.append("Recogidas de material")
eventos.append("Torneo de padel")
print("Agregar elemento: ", eventos)

# Eliminar un elemento de la lista con la opcion POP
eventos.pop(1) # Eliminamos primero la que esta mas lejos de la lista para que no cambien las posiciones
eventos.pop(0)
print("Eliminar elemento Concierto porque no cumple con los requisitos: ", eventos)

# Ordenamos la lista de eventos 
eventos.sort()
print("Ordenar eventos: ", eventos)

print("===================================================================")

print("CASOS DE USO DE TUPLAS")

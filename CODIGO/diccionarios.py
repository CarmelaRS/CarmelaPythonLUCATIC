#!/usr/bin/python
#!/usr/bin/env python
import os

# Limpiamos la terminal antes de imprimir
os.system('cls' if os.name == 'nt' else 'clear')

print("DICCIONARIOS")

# Creamos un diccionario con las claves de tallas numericas y valores numericos de cada una clave
tallas = {
    'S': 10,
    'M': 15,
    'L': 20,
    'XL': 25
}

# Imprimimos los valores del diccionario
print("Guia de tallas:", tallas)

# Imprimimos las claves del diccionario
print("ORDEN DE TALLAS:")
for talla, cantidad in tallas.items():
    print(f"Talla {talla}: {cantidad} und")

# Accedemos a un unico valor
print(tallas['S'])

# Añadimos un nuevo valor al diccionario
tallas['XXL'] = 30
# Imprimimos los valores del diccionario despues de añadir un nuevo valor
print("Guia de tallas despues de añadir XXL:", tallas)

# Modificamos un valor del diccionario
tallas['S'] = 12
# Imprimimos los valores del diccionario despues de modificar un valor
print("Guia de tallas despues de modificar S:", tallas)

# utilizamos update para añadir varios valores al diccionario
tallas.update({
    'XXS': 5,
    'XS': 7
})
print("Guia de tallas despues de añadir XXS y XS:", tallas)
print("===================================================================")

# Eliminamos un valor del diccionario
del tallas['L']
print("Guia de tallas despues de eliminar L:", tallas)
print("===================================================================")

# Listamos las claves del diccionario
print("CLAVES DE TALLAS:", tallas.keys())

# Obtenemos uns lista de las claves 
print("LISTA DE CLAVES:", list(tallas.keys()))
print("===================================================================")

# Comprobamos que una talla esta en el diccionario (devuelve True si la clave existe y False si no)
print("COMPROBACIONES DE TALLAS: ")
print("Esta M en el diccionario?", 'M' in tallas)
print("Esta L en el diccionario?", 'L' in tallas)
print("===================================================================")

# Recorremos de el diccionario con items()
print("RECORRIDO DE TALLAS CON ITEMS():")
for talla, cantidad in tallas.items():
    print(talla, cantidad)
print("===================================================================")

# Usamos la funcion enumerate para obtener el indice y el valor de cada clave
print("RECORRIDO DE TALLAS CON ENUMERATE():")
for indice, cantidad in enumerate(tallas):
    print(indice, tallas[cantidad])
print("===================================================================")


#!/usr/bin/python
#!/usr/bin/env python

import os

# Limpiamos la terminal antes de imprimir

os.system('cls' if os.name == 'nt' else 'clear')

print("EJERCICIO 1 SOBRE TUPLAS")

# Creamos una tupla y la modificamos 
mi_tupla = (1, 2, 3)

#Intentamos modificar la tupla aunque no se va a poder 
try: 
    mi_tupla[1] = 45
except TypeError as e: 
    print(f"Error: {e}")
    print("No se pueden modificar las tuplas")

print("Solucion para modificar una tupla: Convertirla en lista:")
listatupla = list(mi_tupla)
listatupla[1] = 44
# Convertimos la lista en tupla 
tuplaModificada = tuple(listatupla)
print("Tupla inicial: ", mi_tupla)
print("Lista de tupla: ", listatupla)
print("Tupla modificada: ", tuplaModificada)

#################################################################

# Creamos una tupla mixta 
tupla_mixta = (1, "dos", [3,4], {5:"cinco"}, (6,7), 8.0, True, None, {9})

print("Tupla mixta: ", tupla_mixta)
#Intentamos modificarlo:
try: 
    tupla_mixta[2][1] = 5
except TypeError as e: 
    print(f"Error: {e}")
    print("No se pueden modificar los elementos de la tupla mixta")

print("Tupla mixta después de intentar modificar: ", tupla_mixta)

# Imprimimos los elementos de al tupla mixta y su tipo 
#Nos recorremos la tupla y la imprimimos con su tipo

for i, elem in enumerate(tupla_mixta):
    print(f"{elem} => <class '{type(elem).__name__}'>")

#################################################################

# Convertimos la tupla mixta en una lista
lista_mixta = list(tupla_mixta)
print("Tupla mixta convertida a lista: ", lista_mixta)

#Modificamos el elemento de la lista

lista_mixta[1] = "hola que tal"
print("Lista tupla: ", lista_mixta)

# Convertimos la lista nuevamente a tupla
tupla_mixta = tuple(lista_mixta)
print("Tupla mixta convertida a tupla: ", tupla_mixta)

#################################################################

# Tupla numerica y operacion que sume el minimo y el maximo
tupla_numerica = (1, 2, 3, 4, 5)
minimo = min(tupla_numerica)
maximo = max(tupla_numerica)
tuplaSuma = (minimo + maximo)
print("La suma del mínimo y el máximo de la tupla numérica es: ", tuplaSuma)

# Creamos los cuadrados de la tupla con una funcion de compresion 
tupla_cuadrados = tuple(x ** 2 for x in tupla_numerica if x > 2)
print("Resultado tupla cuadrados: ", tupla_cuadrados)

# Desempaquetamos la tupla en tantas variables como elementos tenga 
# Creamos un bucle para generar variables dinamicas
for i, valor in enumerate(tupla_numerica):
    globals()[f'var_{i}'] = valor

# Imprimimos las variables generadas
for i in range(len(tupla_numerica)):
    print(f"var_{i} => {globals()[f'var_{i}']}")

########################################################################

print("EJERCICIO 2 SOBRE LISTAS")

# Creamos listas por comprension 
items = [0, 0, 2, 7, 4, 5, 2]
nueva_lista = []
for item in items:
    if(item > 0):
        nueva_lista.append(item*2)

print("Listas antes y después de aplicar la transformación:")
print("Antes: ", items)
print("Después: ", nueva_lista)

########################
print("EJERCICIO DE LISTAS DE COMPRENSION: ESCENARIO CIENTIFICO ")

# Lista de temperaturas en grados Celsius
temperaturas = [20, -150, -100, 25, -196, 30, -180, -220, -300, -195, -197]

# Sacar una lista con las temperaturas en las que el nitrogeno es gaseoso (por encima de -196) y otra para nitrogeno liquido
nitroGas = []
nitroLiquid = []

for item in temperaturas:
    if(item > -196):
        nitroGas.append(item)
    else :
        nitroLiquid.append(item)

# Imprimimos temperaturas y resultados
print("Temperaturas: ", temperaturas)
print("Temperaturas en nitrogeno gaseoso: ", nitroGas)
print("Temperaturas en nitrogeno liquido: ", nitroLiquid)

#!/usr/bin/python
#!/usr/bin/env python
# Importamos las librerias que necesitamos para usar pandas 
import pandas as pd

# Creamos una serie con numeros 
numeros = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Mostramos la serie 
print("SERIE DE NUMEROS:\n", numeros)

# Agregamos un nuevo elemento a la serie 
    # Creamos una nueva serie con los elementos que queremos añadir y lo concatenamso a la numeros 
aniadir = pd.Series([11])
numeros = pd.concat([numeros, aniadir])

# Mostramos 
print("Serie con NUEVOS elementos: \n", numeros)

# QUITAMOS un elemento de la serie
numeros = numeros[numeros!=11] 
print("Lista con ELIMINACION de elementos: \n", numeros)

#OPERACIONES ARITMETICAS 
numeros1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# SUMA 
suma = numeros + numeros1
print("Suma:\n", suma)

# RESTA
resta = numeros - numeros1
print("Resta:\n", resta)

# MULTIPLICACION 
multiplicacion = numeros * numeros1
print("Multiplicación:\n", multiplicacion)
# DIVISION 
division = numeros / numeros1
print("Division:\n", division)

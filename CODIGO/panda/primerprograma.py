#!/usr/bin/python
#!/usr/bin/env python

# Importamos las librerias que necesitamos para usar pandas 
import pandas as pd

# Creamos un dataframe simple con nombres y edades 
data = {'Nombres': ['Juan', 'Pedro', 'Maria', 'Isabella', 'Carlos'], 'Edades': [25, 30, 28, 22, 29]}
df = pd.DataFrame(data) # Creamos el dataframe

# Mostramos el dataframe
print("Hola mundo en PANDAS!")
print(df)

print("===================================================================")

# Creamos una serie de datos 
datos = pd.Series([10, 20, 30, 40])
# Mostramos la serie
print("Serie de datos:")
print(datos)
# Accedemos a un elemento especifico de la serie
print("\nValor en posicion 3", datos[2])

# Creamos otra serie con indices 
datoswthindice = pd.Series([10, 20, 30, 40, 50], index=['a','b','c', 'd', 'e'])
# Accedemos a un valor usando su indice 
print("\n Valor en el indice 'C':", datoswthindice['c'])
print("\n Valor en el indice 'E':", datoswthindice['e'])
print("===================================================================")
# Accedemos a un elelemento especifico del dataframe usando su indice y columna
print("1ºEJ NOMBRES Y EDADES ")
print("Edad de Maria: ", df["Edades"][2])
print("===================================================================")
print("\n SERIES OPERACIONES ")
print("\n OPERACIONES ARITMETICAS")
serie1 = pd.Series([10, 20, 30, 40])
serie2 = pd.Series([1, 2, 3, 4])

# SUMA 
suma = serie1 + serie2
print("Suma:\n", suma)

# RESTA
resta = serie1 - serie2
print("Resta:\n", resta)

# MULTIPLICACION 
multiplicacion = serie1 * serie2
print("Multiplicación:\n", multiplicacion)
# DIVISION 
division = serie1 / serie2
print("Division:\n", division)

# CONCATENACIONES 
serie_concatenada = pd.concat([serie1, serie2])
print("Serie concatenada:\n", serie_concatenada)

print("===================================================================")

print("\n OPERACIONES ESTADISTICAS")

# MEDIA 
media = serie1.mean()
print("Media de la serie1: ", media)

# MEDIANA 
mediana = serie1.median()
print("Mediana de la serie1: ", mediana)

# DESVIACION ESTANDAR
desviacion = serie1.std()
print("Desviacion estandar de serie1: ", desviacion)

# SUMA TOTAL 
suma_total =serie1.sum()
print("Suma total de serie1: ", suma_total)

# MINIMOS Y MAXIMOS 
minimo = serie1.min()
maximos = serie1.max()
print("Minimo de serie1: ", minimo)
print("Maximo de serie1: ", maximo)

# COUNT
conteo = serie1.count()
print("Numero de elementos de serie1: ", conteo)

# UNIQUE
valores_unicos = serie1.unique()
printo("Valores unicos en serie1: ", valores_unicos)

# VALUE_COUNTS
valores_cuenta = serie1.value_counts()
print("Conteo de valores en serie1: ", valores_cuenta)

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

# MODA
moda = serie1.mode()
print("Moda de serie1:", moda)

# VARIANZA
varianza = serie1.var()
print("Varianza de serie1:", varianza)

# DESCIPCION 
descripcion = serie1.describe()
print("Descripción de serie1:\n", descripcion)

# CORRELACION 
corr = serie1.corr(serie2)
print("Correlación entre serie1 y serie2:", corr)

# COVARIANZA
cov = serie1.cov(serie2)
print("Covarianza entre serie1 y serie2:", cov)

# Valores quialitativos a serie1 
cuantil_25 = serie1.quantile(0.25)
cuantil_50 = serie1.quantile(0.50) # == MEDIANA
cuantil_75 = serie1.quantile(0.75)

print("Cuantil 25% de serie1:", cuantil_25)
print("Cuantil 50% (mediana) de serie1:", cuantil_50)
print("Cuantil 75% de serie1:", cuantil_75)

# Creamos una serie de numeros negativos
serie_negativa = pd.Series([-1, -2, -3, 4])
valores_absolutos = serie_negativa.abs()
print("Valores absolutos:", valores_absolutos)

# SUMA ACUMULATIVA
suma_acumulativa = serie1.cumsum()
print("Suma acumulativa de serie1:", suma_acumulativa)

# PRODUCTO ACUMULATIVO
producto_acumulativo = serie1.cumprod()
print("Producto acumulativo de serie1:",
producto_acumulativo)
print("===================================================================")

# Acceso a elementos y slicing 
# Acceso por indice 
elemento = serie1[2]
print("Tercer elemento: ", elemento)

# Slicing por Indice numerico 
sub_serie = serie1[1:4]
print("Slicing del segundo al cuarto elemento: \n", sub_serie)

# Acceso por indice de etiqueta 
serie_con_etiqueta = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
elemento_etiqueta = serie_con_etiqueta['b']
print("Elemento con etiqueta 'b': ", elemento_etiqueta)

# Slicing por Indice de etiqueta 
sub_indice_etiquetas = serie_con_etiqueta['a':'c']
print("Slicing con eltiquetas de 'a' a 'c':\n", sub_indice_etiquetas)

# ACCESO CON .Loc[] y .iloc[]
# Loc[] para acceso basado en etiquetas y .iloc[] para acceso basado en posicion 
elemento_loc = serie_con_etiqueta.loc['c']
elemento_iloc = serie1.iloc[2]

print("Acceso con .loc[]", elemento_loc)
print("Acceso con .iloc[]", elemento_iloc)
print("===================================================================")

# append no funciona en panda por lo que se usa concat para añadir nuevos elementos 
serie_concatenada = pd.concat([serie1, serie2], ignore_index = True)
print("Serie concatenada (AÑADIR ELEMENTOS):\n", serie_concatenada)
print("===================================================================")

# ORDEN ASCENDENTE
ascendente = serie_concatenada.sort_values()
print("ORDEN ASCENDENTE:\n", ascendente)

# ORDEN DESCENDENTE
descendente = serie_concatenada.sort_values(ascending=False)
print("ORDEN DESCENDENTE:\n", descendente)
print("===================================================================")

# ELIMINAR DATOS 
print("ELIMINAR DATOS")

# ELIMINAR DATOS DUPLICADOS 
sinduplicados = serie_concatenada.drop_duplicates()
print("Serie sin duplicados:\n", sinduplicados)
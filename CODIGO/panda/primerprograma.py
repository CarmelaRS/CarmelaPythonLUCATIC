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
maximo = serie1.max()
print("Minimo de serie1: ", minimo)
print("Maximo de serie1: ", maximo)

# COUNT
conteo = serie1.count()
print("Numero de elementos de serie1: ", conteo)

# UNIQUE
valores_unicos = serie1.unique()
print("Valores unicos en serie1: ", valores_unicos)

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

# ELIMINAR VALORES NULOS 
sinnulos = serie_concatenada.dropna()
print("Serie sin nulos: \n", sinnulos)

# ELIMINAR POR INDICE
serie_sin_indice = serie_concatenada.drop(serie_concatenada.index[2])
print("Serie sin el tercer elemento:\n", serie_sin_indice)

# ELIMINAR POR ETIQUETA 
serie3 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
serie_sin_etiqueta = serie3.drop('a')
print("Serie sin el elemento con etiqueta 'a':\n", serie_sin_etiqueta)

# ELIMINAR POR CONDICION
serie_sin_condicion = serie_concatenada.drop(serie_concatenada[serie_concatenada > 5].index)
print("Serie sin elementos mayores a 5:\n", serie_sin_condicion)

print("===================================================================")
print("FUSION")
# Preparacion de df a fusionar 
peliculas_data = {
    'ID': [1,2,3,4,5,6,7,8,9,10,11,12],
    'Película': ['Avatar', 'Vengadores: Endgame', 'Avatar 2', 'Titanic', 'Star Wars: Episodio VII - El despertar de la Fuerza', 'Vengadores: Infinity War', 'Spider-Man: No Way Home',
    'Jurassic World', 'El Rey León', 'Los Vengadores', 'Frozen II', 'La Bella y la Bestia'],
    'Año de Emisión': [2009, 2019, 2022, 1997, 2015, 2018, 2021, 2015, 2019, 2012, 2019, 2017],
    'Género': ['Ciencia ficción', 'Acción', 'Ciencia ficción', 'Drama', 'Ciencia ficción', 'Acción', 'Acción', 'Ciencia ficción', 'Animación', 'Acción', 'Animación', 'Romance'],
    'Duración (minutos)': [162, 181, 190, 195, 138, 149, 148, 124, 89, 143, 103, 129],
    'Calificación IMDB': [7.8, 8.4, 8.1, 7.8, 7.8, 8.4, 8.2, 7.0, 7.1, 8.0, 6.8, 7.1]
}

finanzas_data = {
    'ID': [1,2,3,4,5,6,7,8,9,10,11,12],
    'Recaudación': [ 2923706026, 2799439100, 2320250233, 2264743180, 2071521700 , 2052359754, 1921704167, 1670516444, 1663075439, 1520538515, 1453000000, 1264000000],
    'Presupuesto': [237000000, 356000000, 250000000, 200000000, 245000000, 321000000, 200000000, 150000000, 260000000, 220000000, 150000000, 160000000],
    'Ganancias': [5543706026, 3159439100, 2070250233, 2064743180, 1826521700, 1732359754, 1721704167, 1520516444, 1403075439, 1300538515, 1303000000, 1104000000]
}
#Creamos DF 
dfPeliculas = pd.DataFrame(peliculas_data)
dfFinanzas = pd.DataFrame(finanzas_data)

# CONCATENAR 
dfconcatenar = pd.concat([dfPeliculas, dfFinanzas])
print("Concatenar:\n", dfconcatenar)

# UNIR
dfunir = pd.merge(dfPeliculas, dfFinanzas, on='ID', how="inner", validate="one_to_one")
print("Unir:\n", dfunir) 
print("===================================================================")

# OPCION 1: COMPLETAR DATOS
# dataframe adicional 
df_adicional = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Director': ['James Cameron', 'Anthony y Joe Russo', 'James Cameron', 'James Cameron', 'J.J. Abrams', 'Anthony y Joe Russo', 'Jon Watts', 'Colin Trevorrow', 'Jon Favreau', 'Joss Whedon', 'Chris Buck y Jennifer Lee', 'Bill Condon'],
    'Premios Oscar': [3, 0, 0, 11, 0, 0, 0, 0, 0, 1, 0, 0],
    'Globos de Oro': [2, 0, 0, 4, 0, 0, 0, 0, 0, 0, 1, 1]
})

# Añadimos una nueva clave a DF con la suma de los premios 
df_adicional['Total Premios'] = df_adicional['Premios Oscar'] + df_adicional['Globos de Oro']

# Mostramos datos 
print("TODOS LOS DATOS: \n", df_adicional)

# OPCION 2: COMPLETAR DATOS USANDO MERGE
df_premios = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'Total Premios 2': df_adicional['Premios Oscar'] + df_adicional['Globos de Oro']
})

# Fusion de DF
df_adicional2 = pd.merge(df_adicional, df_premios, on='ID', how='left')
# Mostramos datos 
print("TODOS LOS DATOS 2: \n", df_adicional2)

# Prescindimos de columnas con DROP
df_final = df_adicional.drop(['Premios Oscar', 'Globos de Oro'], axis=1)
print(" RESULTADOS FINALES:\n", df_final)
print("===================================================================")

# ORDENAMOS CON SORT 
df_final.sort_values(by='Total Premios', ascending=False, inplace=True)
print("-------ORDEN POR PREMIOS ----------------")
print(df_final.to_string(index=False))

df_final.sort_values(by='Director', ascending=True, inplace=True)
print("-------ORDEN POR DIRECTOR ----------------")
print(df_final.to_string(index=False))
print("===================================================================")

# FILTROS 
# Creamos un DF (df_dinal1) con los datos de dfunir

df_final1 = pd.merge(df_adicional, dfunir, on='ID', how='left')
print(df_final1)

print('------ Filtro por Género: Acción --------')
df_accion = df_final1[df_final1['Género'] == 'Acción']
print(df_accion.head(3).to_string(index=False))

print('------ Filtro por Ganancia: Mayor de 2000M --------')
df_filtrado_presupuesto = df_final1[df_final1['Ganancias'] > 2_000_000_000]
print(df_filtrado_presupuesto.to_string(index=False))

print("===================================================================")

# COLUMNA CALCULADA: rentabilidad%
print('------ Rentabilidad% --------')
df_final1['Rentabilidad%'] = round(df_final1['Ganancias'] / df_final1['Presupuesto'] * 100, 2)
print(df_final1.to_string(index=False))
print("===================================================================")

# AGRUPACION 
# Agrupamos directores por recaudacion y premios 
print('------ Agrupación Director por recaudación y premios --------')
df_agrupado_directores = df_final1.groupby('Director').agg({
    'Recaudación': 'mean', 
    'Total Premios': 'sum'
}).reset_index()

print(df_agrupado_directores.to_string(index=False))

# Ordenamos por total premios 
df_agrupado_directores.sort_values(by=['Total Premios', 'Recaudación'], ascending=[False, False], inplace=True)

print('------ Agrupación Director por recaudación y premios (Ordenados) --------')
print(df_agrupado_directores.to_string(index=False))
print("===================================================================")

# ACCESO 
# con .loc mas conciso 
df_james_cameroloc = df_agrupado_directores.loc[df_agrupado_directores['Director'] == 'James Cameron']

print('------ Director James Cameron con LOC--------')
print(df_james_cameroloc.to_string(index=False))

# Sin loc, menos conciso
df_james_camero = df_agrupado_directores[df_agrupado_directores['Director'] == 'James Cameron']

print('------ Director James Cameron sin LOC--------')
print(df_james_camero.to_string(index=False))

# DIRECTOR COMO INDEX

df_agrupado_directores.set_index('Director', inplace=True)

print('\nLa recaudación de James Cameron: ' + str(df_agrupado_directores.loc['James Cameron', 'Recaudación'])+'\n')
print("===================================================================")
print(df_final1)
# APLICAMOS UNA FUNCION A UNA COLUMNA 
# RENTABILIDAD EN MILLONES DE DOLARES POR MINUTOS DE PELICULA 
df_final1['Rentabilidad por minuto'] = df_final1.apply(lambda x: round((x['Ganancias']/x['Duración (minutos)'])/1_000_000, 2), axis=1)

print('------ Rentabilidad por minuto --------')
print(df_final1[['Película', 'Rentabilidad por minuto']].to_string(index=False))

# Agrupar y realizar una operacion de agregacion 
df_grouped = df_final1.groupby('Género')['Rentabilidad por minuto'].mean().reset_index()
df_grouped.sort_values('Rentabilidad por minuto', ascending=False, inplace=True)

print('------ Rentabilidad por género --------')
print(df_grouped.to_string(index=False))

print("===================================================================")

# ITERACION 

print("-------- ITERROWS() --------")
# Itera sobre filas del DF como pares (indice, serie)
for index, row in df_final1.iterrows():
    print( index,"\n", row) ## NO LO MUESTRA EN TABLA
    print("------------------------------------------------------------------------------------------------")
   # print(f'Indice: {index}, Pelicula: {row["Película"]}, Recaudación: {row["Recaudación"]}')

# OPCION 2
for index, row in df_final1.iterrows():
    print(f'Indice: {index}, Pelicula: {row["Película"]}, Recaudación: {row["Recaudación"]}') ## SI QUIERO MOSTRAR MAS DATOS LOS AÑADO UNO A UNO 
    print("------------------------------------------------------------------------------------------------")

print("--------- ITERTUPLES() --------")
# iteracion sobre filas del df como tuplas nombradas 
for row in df_final1.itertuples():
    print(row)
    print("\n*****************************************************************************************************\n")
    print(row.Película)
    print("\n------------------------------------------------------------------------------------------------\n")

print("------ APPLY() ------")
# Mas rapido para ciertas cosas 
df_final1.apply(lambda row:print(row), axis=1)

print("------ BUCLE FOR DIRECTO (COLUMNAS) ------")
# iTERA DIRECTAMENTE CON LAS COLUMNAS 
for column in df_final1: 
    print(df_final1[column])

print("\n*****************************************************************************************************\n")
print("------ REPLACE ------")
# NUEVOS DF
nuevodf_peliculas = {
    'ID': [1,2,3,4,5,6,7,8,9,10,11,12],
    'Película': ['Avatar', 'Vengadores: Endgame', 'Avatar 2', 'Titanic','Star Wars: Episodio VII - El despertar de la Fuerza','Vengadores: Infinity War', 'Spider-Man: No Way Home','Jurassic World', 'El Rey León', 'Los Vengadores','...', 'La Bella y la Bestia'],
    'Año de Emisión': [2009, 2019, 2022, 1997, 2015, 2018, 2021, 2015, 2019, 2012, 2019, 2017],
    'Género': ['Ciencia ficción', 'Acción', 'Ciencia ficción', 'Drama', 'Ciencia ficción','Acción', 'Acción', 'Ciencia ficción', 'Animación', 'Acción','Animación', 'Romance'],
    'Duración (minutos)': [162, 181, 190, 195, 138, 149, 148, 124, 89, 143, 103, 129],
    'Calificación IMDB': [7.8, 8.4, 8.1, 7.8, 7.8, 8.4, 8.2, 7.0, 7.1, 8.0, 6.8, 7.1],
}

# Creamos un nuevo DF con los datos de nuevodf_peliculas
df_peliculas_info = pd.DataFrame(nuevodf_peliculas)
print ("NUEVO DF PELICULAS: \n", df_peliculas_info)

# Reemplazamos valores en las columnas
df_peliculas_info.replace('...', 'Desconocida', inplace=True)

print("\nNUEVO DF PELICULAS CAMBIANDO POR DESCONOCIDAS:   \n", df_peliculas_info)
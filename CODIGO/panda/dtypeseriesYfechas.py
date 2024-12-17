#!/usr/bin/python
#!/usr/bin/env python
# Importamos las librerias que necesitamos para usar pandas 
import pandas as pd

# CREACION DE SERIES DE NUMEROS CON UN NULO
serie_con_none = pd.Series([1, 2, 3, None])
print("Serie con None:")
print(serie_con_none)

# CREACION DE SERIE CON VALOR NaN
serie_con_nan = pd.Series([1, float('nan'), 3, None])
print("Serie con NaN:")
print(serie_con_nan)

# MOSTRAMOS EL TIPO DE DATOS 
print("\nTipo de dato:", serie_con_nan.dtype) 

# REALIZAMOS OPERACIONES ESTADISTICAS 
print("\nMedia (ignorando NaN):", serie_con_nan.mean()) 

# Cambio de tipo de dato con NaN
try:
    serie_convertida = serie_con_nan.astype('int')
except Exception as e:
    print("\nError al convertir a entero:", e)
print("===================================================================")

# FECHAS Y HORAS 
# CONVERSION DE FECHAS A HORAS 
fechas = pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03'])
print("Fechas convertidas:", fechas)


# RANGO DE FECHAS
rango_fechas = pd.date_range(start='2023-01-01', end='2023-01-07',
freq='D')
print("Rango de fechas diarias:", rango_fechas)
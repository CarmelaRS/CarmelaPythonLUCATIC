#!/usr/bin/python
#!/usr/bin/env python
# Importamos las librerias que necesitamos para usar pandas 
import pandas as pd

# CREACION DE SERIES 
#   A. TEMPERATURAS 
#   B. PECIPICACIONES
temperaturas = pd.Series([22, 24, 26, 28, 30, 32, 34], index=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])
precipitaciones = pd.Series([5, 10, 15, 0, 2, 7, 9], index=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])

# Mostramos las dos series 
print(" TEMPERATURAS: \n", temperaturas)
print(" PRECIPITACIONES:\n", precipitaciones)

# OPERACIONES CON SLICING
slicing_A = temperaturas["Miercoles":"Viernes"]
slicing_B = precipitaciones["Miercoles":"Viernes"]

print("\nSlicing de Temperaturas de Miércoles a Viernes:")
print(slicing_A)
print("\nSlicing de Precipitación de Miércoles a Viernes:")
print(slicing_B)

# Slicing por indice
slicingAetiqueta = temperaturas['Lunes']
print("Slicing de la temperatura del lunes: \n", slicingAetiqueta)
slicingBetiqueta = precipitaciones['Martes':'Viernes']
print("Slicing de las precipitaciones del Martes al Viernes: \n", slicingBetiqueta)

# COMBINAR SERIES RESULTANTES DEL SLICING 
df_combinado = pd.DataFrame({
    "Temperatura: ": slicing_A,
    "Precipitacion: ": slicing_B
})

print("Dataframe combinado de slicing:\n", df_combinado)

# OPERACIONES BASICAS 
media_Temp = df_combinado["Temperatura: "].mean()
media_Prec = df_combinado["Precipitacion: "].mean()
# Suma de temp y precip
df_combinado["Suma: "] = df_combinado["Temperatura: "] + df_combinado["Precipitacion: "]

# Mostrar datos 
print("\n Media de Temperatura: ", media_Temp)
print("\n Media de Precipitación: ", media_Prec)
print("\nDataFrame con la suma de Temperatura y Precipitación:\n", df_combinado)
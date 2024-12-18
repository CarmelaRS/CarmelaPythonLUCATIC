#!/usr/bin/python
#!/usr/bin/env python
# Importamos las librerias que necesitamos para usar pandas 
import pandas as pd

# Creamos una DF  de datos con nombre, edad y ciudad 
data = {
    'Nombre': ['Juan', 'Pedro', 'Maria', 'Isabella', 'Carlos', 'Ana'],
    'Edad': [25, 30, 28, 22, 29,-1],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao', 'Madrid']
}
#Convertimos a DF 
df = pd.DataFrame(data)

# Mostramos los datos del DF 
                   
print("Dataframe:")
print(df)

# SELECCIONAMOS COLUMNAS NUMERICAS 
numeric_columnas=df.select_dtypes(include=['number'])
print("Numero:\n", numeric_columnas)

# VALORES NEGATIVOS DE LAS COLUMNAS NUMERICAS
count_negativos = numeric_columnas.apply(lambda x: (x<0).sum())
print("Numeros negativos:\n", count_negativos)
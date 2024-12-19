#!/usr/bin/python
#!/usr/bin/env python

# Importamos las librerias que necesitamos para usar pandas 
import pandas as pd
# Libreria NumPy
import numpy as np

# PYTHON LIST 
movie_ratings = [88, 73, 92, 90, 62, 23]

movie_ratings_updated = [x + 2 for x in movie_ratings]
print(movie_ratings)
print("=================================================================")

# PANDAS 
movie_ratingspanda = pd.Series([88, 73, 92, 90, 62, 23])
movie_ratingspanda_updated = movie_ratingspanda +2
print(movie_ratings_updated)
print("=================================================================")

# NUMPY
movie_ratingsnp = np.array([88, 73, 92, 90, 62, 23])
movie_ratingsnp_updated = movie_ratingsnp + 2
print(movie_ratingsnp_updated)
print("=================================================================")

print("\nCREACION DE UN ARRAY")
mi_array = np.array([1, 2, 3, 4])
print("Mi Array: ", mi_array)

print("=================================================================")
print("ARITMETICA BASICA ")
Array1 = np.array([1, 2, 3, 4])
Array2 = np.array([5, 6, 7, 8])

#SUMA 
print("SUMA: ", Array1 + Array2)

#RESTA
print("RESTA: ", Array2 - Array1)

#MULTIPLICACION
print("MULTIPLICACION: ", Array1 * Array2)

#DIVISION
print("DIVISION: ", Array1 / Array2)

# RAIZ CUADRADA 
print("RAIZ CUADRADA: ", np.sqrt(Array2))

print("=================================================================")

print("TRIGONOMETRIA")
# Funciones trigonometricas 
#SENO 
print("Seno: ", np.sin(Array1))

#COSENO 
print("Coseno: ", np.cos(Array1))

#TANGENTE
print("Tangente: ", np.tan(Array1))

# HIPOTENUSA 
cateto1 = 3
cateto2 = 4
hipotenusa = np.hypot(cateto1, cateto2)
print("Hipotenusa: ", hipotenusa)

# ARCO TANGENTE DE DOS PARAMETROS 
x = 3
y = 4

angulo = np.arctan2(y,x)
print("Ángulo en radianes: ", angulo)

# RADIANES 
grados = 45 
radianes = np.deg2rad(grados)
print("Radiantes: ", radianes)

print("=================================================================")

print("EXPONENCIAL Y LOGARITMICA")
# EXPONENCIAL 
exp_movierating = np.exp(movie_ratingsnp)
print("Exponencial: ", exp_movierating)

# LOGARITMO NATURAL 
log_x = np.log(movie_ratingsnp)
print("Logaritmo natural: ", log_x)

# LOGARITMO EN BASE 10 
log10_x = np.log10(movie_ratingsnp)
print("Logaritmo en base 10: ", log10_x)

print("=================================================================")

print("POTENCIA Y RAICES")
# POTENCIA 
potencia = np.power(movie_ratingsnp, 2)
print("Potencia: ", potencia)
# RAIZ CUADRADA 
raiz2 = np.sqrt(movie_ratingsnp)
print("Raiz cuadrada: ", raiz2)
# RAIZ CUBICA 
raiz3 = np.cbrt(movie_ratingsnp)
print("Raiz cubica: ", raiz3)

print("=================================================================")

print("ESTADISTICAS")

# MEDIA 
print("Media: ", np.mean(movie_ratingsnp))

# MEDIANA 
print("Mediana: ", np.median(movie_ratingsnp))

# DESVIACION ESTANDAR 
print("Desviación estándar: ", np.std(movie_ratingsnp))

# MINIMO 
print("Mínimo: ", np.min(movie_ratingsnp))

# MAXIMO 
print("Máximo: ", np.max(movie_ratingsnp))
print("=================================================================")

print("ACUMULACIÓN Y AGREGACIÓN")

# ACUMULACION 
print("ACUMULACIÓN")
# SUMA
print("Suma acumulada: ", np.cumsum(movie_ratingsnp))

# PRODUCTO 
print("Producto acumulado: ", np.cumprod(movie_ratingsnp))

# FUNCIONES DE AGREGACION 
print("AGREGACIÓN")

#SUMA 
print("Suma: ", np.sum(movie_ratingsnp))

# PRODUCTO
print("Producto: ", np.prod(movie_ratingsnp))

print("=================================================================")

print("VERIFICAR TIPO")

rating = np.array([88, 73, 92, 90, 62, 23], dtype=np.int64)
# type devuelve <class 'numpy.ndarray'> sea int64 o 32
print(type(rating))
# Podemos usar type sobre su primer elemento
print(type(rating[0]))
# O podemos usar la propiedad dtype
print("Tipo de dato de los elementos:", rating.dtype)

print("=================================================================")

print("MANIPULACIONES")

# CAMBIO DE FORMA (RESHAPE)
reshaped = rating.reshape(2,3)
print("Reshaped array: \n", reshaped)

# 3 ARRAYS CON 2 ELEMENTOS
reshaped = rating.reshape(3, 2)
print("Reshaped array: \n", reshaped)

# VOLVEMOS AL INICIAL APLANANDO EL ARRAY CON flatten
flattened = reshaped.flatten()
print("Flattened array: \n", flattened)

# REANSPOSICIÓN 
reshaped = rating.reshape(3,2)
print("Reshaped array: \n", reshaped)
transposed =reshaped.transpose()
print("Transposed array:\n", transposed)

# CONCATENACIÓN
mitad1 = rating[:3]
mitad2 = rating[3:]

print("Primera parte: ", mitad1)
print("Segunda parte:", mitad2)

concatenated = np.concatenate((mitad1, mitad2))
print("Concatenated array: ", concatenated)

# DIVISION (SPLIT)
splitarrays = np.split(rating, 3)
print("Split arrays: ", splitarrays)

# STACKING -- usamos los arrays de mitades
stacked = np.vstack((mitad1, mitad2))
print("Stacked array:\n", stacked)

# EJERCICIO 2 STACKING
peliculas = np.array(['Avatar', 'Harry Potter'])
espectadores = np.array([12342342, 1252463432])

stackedpeliculas = np.column_stack((peliculas, espectadores))
print("Stacked array peliculas:\n", stackedpeliculas)

print("=================================================================")

print("ACCESO A DATOS EN ARRAYS")
print("ACCESO POR INDICES")
# Acceso por indice 
print(rating[2])

# Acceso a array multidimensional 
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[1, 2])

# Acceso con arrays de indices 
indices = np.array([1,5])
print(rating[indices])

print("ACCESO POR RANGO")
# Acceso por rango 
# Entre el indice 3 y 5
slicerating = rating[3:5]
print(slicerating) # Muestra apartir del 3 hasta el 5 incluido 

# Desde el principio ":n"
slicerating = rating[:3]
print(slicerating)

# Hasta el final 
slicerating = rating[3:]
print(slicerating)

# Slicing multidimensional
slice2d = arr2d[0:2, 1:3]
print(slice2d)

# Slicing con pasos 
slicingrating = rating[1:6:2]
print(slicingrating)


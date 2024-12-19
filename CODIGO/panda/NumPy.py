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
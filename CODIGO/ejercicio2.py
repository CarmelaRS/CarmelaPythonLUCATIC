#!/usr/bin/python
#!/usr/bin/env python

import copy

# Creamos una lista de alimentos que diga el precio y el tipo de alimento que es
alimentos = [
    ["Filete pollo", ["Mercadona", "Carrefour"]], 
    ["Merluza", ["Mercadona", "Aldi"]],
    ["Napolitana", ["Ahorramas"]]
]

# Hacemos una copia superficial y una copia profunda
copiaSuperficial = copy.copy(alimentos)

copiaProdunda = copy.deepcopy(alimentos)

# Imprimimos las listas 
print(copiaSuperficial)
print(copiaProdunda)

# Modificamos la copia superficial 
copiaSuperficial[0][0] = "Alitas de pollo" # Cambiamos el nombre de Filete pollo por Alitas de pollo 
copiaSuperficial[1][1][0] = "Ahorramas" #Cambiamos el nombre de Mercadona por Ahorramas (en merluza)
copiaSuperficial[0][1] = "Ahorramas2" #Cambiamos el nombre de Mercadona por Ahorramas (en en 1 elemneto)
copiaSuperficial[2][1].append("Lidl") # Añadimos Lidl a los supermercados de Napolitana

# Modificamos la copia profunda
copiaProdunda[0][0] = "Carne Picada" # Cambiamos el nombre de Filete pollo por Carne Picada 
copiaProdunda[0][1][1] = "Aldi" # Cambiamos el nombre de Mercadona por Aldi (en merluza)
copiaProdunda[1][1][0] = "Lidl2" # Cambiamos el nombre de Mercadona por Lidl2 (en merluza)
copiaProdunda[2][1].append("BM") # Añadimos BM a los supermercados de Napolitana

#Imprimimos las listas modificadas
print("Copia original:")
print(alimentos)

print("Copia superficial modificada:")
print(copiaSuperficial)

print("Copia profunda modificada:")
print(copiaProdunda)




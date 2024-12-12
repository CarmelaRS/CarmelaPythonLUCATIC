#!/usr/bin/python
#!/usr/bin/env python
import os

# Limpiamos la terminal antes de imprimir
os.system('cls' if os.name == 'nt' else 'clear')

# CASOS DE USO LISTAS
print("CASOS DE USO DE LISTAS")
# Creacion de una lista que se puede modificar -- Tema ideas de eventos solidarios
eventos = ["Concierto", "Exposicion", "Torneo"]

# Agregar un elemento a la lista
eventos.append("Recogidas de material")
eventos.append("Torneo de padel")
print("Agregar elemento: ", eventos)

# Eliminar un elemento de la lista con la opcion POP
eventos.pop(1) # Eliminamos primero la que esta mas lejos de la lista para que no cambien las posiciones
eventos.pop(0)
print("Eliminar elemento Concierto porque no cumple con los requisitos: ", eventos)

# Ordenamos la lista de eventos 
eventos.sort()
print("Ordenar eventos: ", eventos)

print("===================================================================")

print("CASOS DE USO DE TUPLAS")
# Creamos un conjunto de valores que no pueden ser modificados 
direccion = (["Madrid", "28001", "España"], ["Paris", "75001", "Francia"], ["London", "EC1A 1BB", "Reino Unido"])

# damos variable a cada valor
ciudad = direccion[0][0]
cp = direccion[0][1]
pais = direccion[0][2]

# Otra forma de acceder a los valores
ciudad2, cp2, pais2 = direccion[1]

# Imprimimos               
print("Imprimir valores de la direccion española:")
print("Ciudad: ", ciudad)
print("CP: ", cp)
print("Pais: ", pais)

print("Imprimir valores de la direccion francesa:")
print("Ciudad: ", ciudad2)
print("CP: ", cp2)
print("Pais: ", pais2)

# Cambiamos el cp de madrid, para ello: lo pasamos a una lista 
listaciudades = list(direccion)

# Modificamos la lista 
listaciudades[0][1] = "28050"

# Volvemos a pasarlo a tupla 
direcciones = tuple(listaciudades)

#Imprime la tupla modificada 
print("Tupla modificada: ", direcciones)
print("===================================================================")

print("CASOS DE USO CONJUNTOS")

# Creamos dos conjuntos distintos de prendas de ropa de mujer y de hombre 
mujer = {"falda", "pantalones", "tacones", "camiseta"}
hombre = {"camiseta", "corbata", "pantalones"}

# Comprobamos que los conjuntos tiene prendas especificas 
print("El armario de la MUJER tiene tacones? ", "tacones" in mujer)
print("El armario de la HOMBRE tiene tacones? ", "tacones" in hombre)

# Añadimos reloj al armario del hombre 
hombre.add("Reloj")
print("Armario del hombre: ", hombre)

# Unimos los armarios
armarios = mujer | hombre
print("Union de armarios: ", armarios)

# Añadimos las prendas que esten los dos
armarios2 = mujer & hombre
print("Prendas en ambos armarios: ", armarios2)

# DIFERENCIA DE CONJUNTOS
diffmujer = mujer - hombre
print("Las prendas que no están en hombre son: ", diffmujer)

diffhombre = hombre - mujer
print("Las prendas que no están en mujer son: ", diffhombre)

# DIFERENCIA SIMÉTRICA DE CONJUNTOS
diffarmariosimetrica = mujer ^ hombre
print("Las prendas que están en algún armario pero no en ambos son: ", diffarmariosimetrica)

print("===================================================================")
print("CASOS DE USO DICCIONARIOS")

# Creamos un diccionario con las profesiones de un grupo de personas
trabajadores = {
    "Juan": "Programador",
    "Maria": "Diseñadora",
    "Pedro": "Encargado de seguridad",
    "Ana": "Productor audiovisual"
}

# Mostramos el diccionario
print("Trabajadores: ", trabajadores)

# Accedemos al trabajo de 'Pedro'
print("Trabajo de Pedro: ", trabajadores["Pedro"])

# Añadimos un nuevo trabajador
trabajadores["Luis"] = "Gerente"
print("Trabajadores despues de añadir Luis: ", trabajadores)

# Eliminamos un trabajador
del trabajadores["Pedro"]
print("Trabajadores despues de eliminar Pedro: ", trabajadores)

# Modificamos el trabajo de 'Ana'
trabajadores["Luis"] = "Encargado de mantenimiento"
print("Trabajadores despues de modificar Luis: ", trabajadores)

# Numerar los trabajadores
print("Trabajadores numerados: ")
for indice, nombre in enumerate(trabajadores):
    print(indice, nombre)
print("===================================================================")

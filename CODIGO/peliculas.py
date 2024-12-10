#!/usr/bin/python
#!/usr/bin/env python

# Creamos las funciones necesarias para el programa 

# Funcion para mostrar el menu principal del programa

def menu_principal():
    print("\n---- Menú de películas ----")
    print("1. Listar películas")
    print("2. Buscar película")
    print("3. Añadir película")
    print("4. Eliminar película")
    print("5. Salir")
    print("\nElija una opción:")
    return input()
print("\n---------------------------")

# Funcion para listar las peliculas
def listar_peliculas(peliculas):
    #Si no hay peliculas, muestra un mensaje
    if not peliculas:
        print("\nNo hay películas agregadas.")
    else:
        print("\nListado de películas:")
        for i, pelicula in enumerate(peliculas, start=1):
            print(f"{i}. {pelicula}")

# Funcion para buscar una pelicula

# Funcion para añadir una pelicula
def agregar_pelicula(peliculas): # Peliculas es una lista de peliculas que se crea en el main
    print("\nAñadir película")
    pelicula = input("Nombre de la película: ")
    peliculas.append(pelicula)
    print("\nPelícula ' {pelicula} ' añadida correctamente.")


# Funcion para eliminar una pelicula

def eliminar_pelicula(peliculas):
    # Si no hay peliculas, muestra un mensaje
    if not peliculas:
        print("\nNo hay películas agregadas.")
        return  # Salimos de la función si no hay peliculas
    
    listar_peliculas(peliculas) # mostramos las peliculas
    try:
        opcion = int(input("\nElija la película a eliminar (número): "))
        if 1 <= opcion <= len(peliculas): # Verificamos que la opcion sea valida
            pelicula_eliminar = peliculas.pop[opcion - 1] # Eliminamos la pelicula
            print(f"\nPelícula '{pelicula_eliminar}' eliminada correctamente.")
        else: 
            print("\nOpción no válida.")
    except ValueError:
        print("\nDebe ingresar un número valido.")

# Programa principal


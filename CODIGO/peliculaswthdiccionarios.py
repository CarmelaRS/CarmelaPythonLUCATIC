#!/usr/bin/python
#!/usr/bin/env python
import os

# Limpiamos la terminal antes de imprimir
os.system('cls' if os.name == 'nt' else 'clear')

print("PELICULAS CON DICCIONARIOS")

# CREAMOS EL MENU PRINCIPAL: 
def menu_principal():
    print("\n---- Menú de películas ----")
    print("1. Añadir películas")
    print("2. Eliminar película")
    print("3. Mostrar película")
    print("4. Modificar película")
    print("5. Buscar película")
    print("6. Añadir IVA")
    print("7. Salir")
    print("\nElija una opción:")
    return input()
print("\n---------------------------")
# FUNCION LISTAR PELICULAS

def listar_peliculas(peliculas):
    # Si no hay peliculas, muestra un mensaje
    if not peliculas:
        print("\nNo hay películas agregadas.")
    else:
        print("\nListado de películas:")
        for i, pelicula in enumerate(peliculas, start=1):
            print(f"{i}. {pelicula}")

# FUNCION AÑADIR PELICULA
def añadir_pelicula(peliculas):
    # Solicitamos el nombre de la pelicula y comprobamos que no esta en el diccionario 
    titulo = input("Introduce el título de la película: ").strip().lower() # Lo pasamos a minusculas para que no de ningun tipo de errror. 
    if titulo in peliculas:
        print(f"\nLa película '{titulo}' ya está agregada.")
        return
    # Solicitamos el resto de elementos 
    director = input("Introduce el director de la película: ")
    anio = int(input("Introduce el año de la película: "))
    presupuesto = float(input("Introduce el presupuesto (en millones) de la película: "))

    # Añadimos la pelicula al diccionario
    peliculas[titulo] = {
        "director": director,
        "año": anio,
        "presupuesto": presupuesto
    }
    print(f"\nLa película '{titulo}' se ha añadido correctamente.")

# FUNCION ELIMINAR PELICULA 
def eliminar_pelicula(peliculas):
    # Si no hay peliculas, muestra un mensaje
    if not peliculas:
        print("\nNo hay películas agregadas.")
        return  # Salimos de la función si no hay peliculas
    
    # Mostramos las peliculas y solicitamos la que quiere eliminar
    listar_peliculas(peliculas)
    titulo = input("\nIntroduce el título de la película que deseas eliminar: ").strip().lower()
    
    # Si la pelicula existe, la eliminamos
    if titulo in peliculas:
        del peliculas[titulo]
        print(f"\nLa película '{titulo}' se ha eliminado correctamente.")
    else:
        print(f"\nNo se encontró la película '{titulo}'.")

# FUNCION MOSTRAR PELICULAS CON TODOS LOS DATOS DE LA PELICULA 
def mostrar_pelicula(peliculas):
    # Si no hay peliculas, muestra un mensaje
    if not peliculas:
        print("\nNo hay películas agregadas.")
        return  # Salimos de la función si no hay peliculas
    
    # Mostramos las peliculas y solicitamos la que quiere mostrar
    print("\nListado de todas las películas:")
    for titulo, pelicula in peliculas.items():
        print(f"\nPelicula: {titulo}")
        print(f"Director: {pelicula.get('director')}")
        print(f"Año: {pelicula.get('año')}")
        print(f"Presupuesto: {pelicula.get('presupuesto')} millones")
        print("---------------------------")

# FUNCION MODIFICAR PELICULAS
def modificar_pelicula(peliculas):
    # Comprobamos que haya peliculas
    if not peliculas:
        print("\nNo hay películas agregadas.")
        return  # Salimos de la función si no hay peliculas
    
    # Listamos las peliculas y solicitamos la que quiere modificar
    listar_peliculas(peliculas)
    titulo = input("\nIntroduce el título de la película que deseas modificar: ").strip().lower()

    # Si la pelicula existe, solicitamos los nuevos datos
    if titulo in peliculas:
        pelicula = peliculas[titulo]
        nuevopresupuesto = float(input("Introduce el NUEVO presupuesto de la película: "))
        pelicula["presupuesto"] = nuevopresupuesto
        # Mostramos los nuevos datos de la pelicula 
        print(f"\nPelicula: {titulo}")
        print(f"Director: {pelicula.get('director')}")
        print(f"Año: {pelicula.get('año')}")
        print(f"Nuevo presupuesto: {pelicula.get('presupuesto')} millones")
        print("---------------------------")
        
        # Mostramos el mensaje de confirmacion
        print(f"\nLa película '{titulo}' se ha modificado correctamente.")
    else:
        print(f"\nNo se encontró la película '{titulo}'.")

# FUNCION BUSCAR PELICULAS
def buscar_pelicula(peliculas):
    # Comprobamos que haya peliculas
    if not peliculas:
        print("\nNo hay películas agregadas.")
        return  # Salimos de la función si no hay peliculas
    
    # Mostramos las peliculas y solicitamos la que quiere buscar
    listar_peliculas(peliculas)
    titulo = input("\nIntroduce el título de la película que deseas buscar: ").strip().lower()
    
    # Si la pelicula existe, mostramos sus datos
    if titulo in peliculas:
        pelicula = peliculas[titulo]
        print(f"\nPelicula: {titulo}")
        print(f"Director: {pelicula.get('director')}")
        print(f"Año: {pelicula.get('año')}")
        print(f"Presupuesto: {pelicula.get('presupuesto')} millones")
        print("---------------------------")
    else:
        print(f"\nNo se encontró la película '{titulo}'.")

# FUNCION AÑADIR IVA
def añadir_iva(peliculas):
   # Si no hay peliculas, muestra un mensaje
    if not peliculas:
        print("\nNo hay películas agregadas.")
        return  # Salimos de la función si no hay películas
    
    # Recorrer todas las películas y aumentar el presupuesto en un 10%
    for titulo, pelicula in peliculas.items():
        nuevo_presupuesto = pelicula['presupuesto'] * 1.10  # Incrementamos el presupuesto en un 10%
        pelicula['presupuesto'] = nuevo_presupuesto  # Actualizamos el presupuesto
        print(f"\nEl presupuesto de la película '{titulo.title()}' ha sido incrementado a {nuevo_presupuesto} millones.")
        
# FUNCION MAIN
def main():
    # Creamos un diccionario vacío para almacenar las peliculas
    peliculas = {}

    # Bucle para manejar las opciones del menu
    while True:
        opcion = menu_principal()
        
        if opcion == "1":
            añadir_pelicula(peliculas)
        elif opcion == "2":
            eliminar_pelicula(peliculas)
        elif opcion == "3":
            mostrar_pelicula(peliculas)
        elif opcion == "4":
            modificar_pelicula(peliculas)
        elif opcion == "5":
            buscar_pelicula(peliculas)
        elif opcion == "6":
            añadir_iva(peliculas)
        elif opcion == "7":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida, por favor intentalo de nuevo.")

# Ejecutamos el programa
if __name__ == "__main__":
    main()
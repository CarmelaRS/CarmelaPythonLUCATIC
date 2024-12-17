from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo para simular una base de datos
peliculas = [
    {"id": 1, "titulo": "The Shawshank Redempt", "director": "Francis Ford Coppola", "anio": 1994, "presupuesto": 2.8},
     {"id": 2, "titulo": "Pulp Fiction", "director": "Quentin Tarantino", "anio": 1994, "presupuesto": 1.5},
     {"id": 3, "titulo": "The Godfather", "director": "Francis Ford Coppola", "anio": 1972, "presupuesto": 1.7}
]

# Obtenemos todas las peliculas 
@app.route('/peliculas', methods=['GET'])
def listar_peliculas():
    return jsonify(peliculas),200 # el 200 es el código de estado HTTP para éxito

# Obtenemos una pelicula por su id
@app.route('/peliculas/<int:id>', methods=['GET'])
def buscar_pelicula(id):
    pelicula = next((pelicula for pelicula in peliculas if pelicula['id'] == id), None)
    if pelicula:
        return jsonify(pelicula), 200
    return jsonify({"error": "Pelicula no encontrada"}), 404

# Añadimos una pelicula
@app.route('/peliculas', methods=['POST'])
def agregar_pelicula():
    nueva_pelicula = request.get_json()
    if not nueva_pelicula.get("titulo") or not nueva_pelicula.get("director") or not nueva_pelicula.get("anio") or not nueva_pelicula.get("presupuesto"):
        return jsonify({"error": "Faltan datos para la pelicula"}), 400
    
    nueva_pelicula["id"] = len(peliculas) + 1 # Generamos un ID 
    peliculas.append(nueva_pelicula)
    return jsonify(nueva_pelicula), 201

# Modificamos una pelicula
@app.route('/peliculas/<int:id>', methods=['PUT'])
def modificar_pelicula(pelicula_id):
    pelicula = next((pelicula for pelicula in peliculas if pelicula['id'] == pelicula_id), None)
    if not pelicula:
        return jsonify({"error": "Pelicula no encontrada"}), 404
    
    datos_actualizados = request.json
    
    pelicula.update({
        "titulo": datos_actualizados.get("titulo", pelicula["titulo"]),
        "director": datos_actualizados.get("director", pelicula["director"]),
        "anio": datos_actualizados.get("anio", pelicula["anio"]),
        "presupuesto": datos_actualizados.get("presupuesto", pelicula["presupuesto"])
    })
    return jsonify(pelicula), 200

# Eliminamos una pelicula
@app.route('/peliculas/<int:id>', methods=['DELETE'])
def eliminar_pelicula(pelicula_id):
    global peliculas
    peliculas = [pelicula for pelicula in peliculas if pelicula['id']!= pelicula_id]
    return jsonify({"message": "Pelicula eliminada"}), 204

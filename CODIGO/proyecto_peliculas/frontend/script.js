const urlBase = "http://127.0.0.1:5000/peliculas";

// Función para mostrar/ocultar secciones
function mostrarSeccion(id) {
    document.querySelectorAll(".seccion").forEach(div => div.classList.add("oculto"));
    document.getElementById(id).classList.remove("oculto");
}

// Cargar todas las películas
document.getElementById("btnListar").addEventListener("click", () => {
    fetch(urlBase)
        .then(response => response.json())
        .then(data => mostrarPeliculas(data))
        .catch(error => console.error("Error al listar:", error));
});

// Mostrar películas en lista
function mostrarPeliculas(peliculas) {
    const lista = document.getElementById("listaPeliculas");
    lista.innerHTML = "";
    peliculas.forEach(p => {
        const li = document.createElement("li");
        li.textContent = `${p.id}. ${p.titulo} - ${p.director} (${p.anio})`;
        lista.appendChild(li);
    });
}

// Agregar una película
document.getElementById("btnAgregarMostrar").addEventListener("click", () => mostrarSeccion("seccionAgregar"));
document.getElementById("btnAgregar").addEventListener("click", () => {
    const titulo = document.getElementById("tituloAgregar").value;
    const director = document.getElementById("directorAgregar").value;
    const anio = document.getElementById("anioAgregar").value;

    fetch(urlBase, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titulo, director, anio })
    })
    .then(() => alert("Película agregada"))
    .catch(error => console.error("Error al agregar:", error));
});

// Buscar una película
document.getElementById("btnBuscarMostrar").addEventListener("click", () => mostrarSeccion("seccionBuscar"));
document.getElementById("btnBuscar").addEventListener("click", () => {
    const titulo = document.getElementById("buscarTitulo").value;
    fetch(`${urlBase}/buscar?titulo=${titulo}`)
        .then(response => response.json())
        .then(data => mostrarPeliculas(data))
        .catch(error => console.error("Error al buscar:", error));
});

// Modificar una película
document.getElementById("btnModificarMostrar").addEventListener("click", () => mostrarSeccion("seccionModificar"));
document.getElementById("btnModificar").addEventListener("click", () => {
    const id = document.getElementById("idModificar").value;
    const titulo = document.getElementById("tituloModificar").value;
    const director = document.getElementById("directorModificar").value;
    const anio = document.getElementById("anioModificar").value;

    fetch(`${urlBase}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titulo, director, anio })
    })
    .then(() => alert("Película modificada"))
    .catch(error => console.error("Error al modificar:", error));
});

// Eliminar una película
document.getElementById("btnEliminarMostrar").addEventListener("click", () => mostrarSeccion("seccionEliminar"));
document.getElementById("btnEliminar").addEventListener("click", () => {
    const id = document.getElementById("idEliminar").value;
    fetch(`${urlBase}/${id}`, { method: "DELETE" })
        .then(() => alert("Película eliminada"))
        .catch(error => console.error("Error al eliminar:", error));
});

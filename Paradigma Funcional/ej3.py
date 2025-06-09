from utils import *

peliculas = [
    {"titulo": "Inception", "anio": 2010, "puntaje": 8.8},
    {"titulo": "The Matrix", "anio": 1999, "puntaje": 8.7},
    {"titulo": "Interstellar", "anio": 2014, "puntaje": 8.6},
    {"titulo": "Avatar", "anio": 2009, "puntaje": 7.8},
    {"titulo": "The Batman", "anio": 2022, "puntaje": 7.9}
]

procesar = procesar_lista
lista_ordenada_puntaje = procesar(peliculas, ordenar_lista, "puntaje","descendente")
for e in lista_ordenada_puntaje:
    print(f"Titulo: {e['titulo']} - Año: ${e['anio']} - Puntaje: {e['puntaje']}")
print("\n")

lista_ordenada_estreno = procesar(peliculas, ordenar_lista, "anio", "ascendente")
for e in lista_ordenada_estreno:
    print(f"Titulo: {e['titulo']} - Año: ${e['anio']} - Puntaje: {e['puntaje']}")

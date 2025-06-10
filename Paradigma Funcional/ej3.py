from utils import *
from listas import peliculas

procesar = procesar_lista

lista_ordenada_puntaje = procesar(peliculas, ordenar_lista, "puntaje","descendente")
mostrar_lista_diccionarios(lista_ordenada_puntaje)

print("\n")

lista_ordenada_estreno = procesar(peliculas, ordenar_lista, "anio", "ascendente")
mostrar_lista_diccionarios(lista_ordenada_estreno)

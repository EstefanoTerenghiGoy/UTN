from utils import *
from listas import estudiantes

procesar = procesar_lista
lista_filtrada = (procesar(estudiantes, filtrar_lista, "calificacion", 6.0, "mayor"))

mostrar_lista_diccionarios(estudiantes)

print("\nEl promedio de calificaciones es: ", procesar(estudiantes, calcular_promedio, "calificacion"))
from utils import *
from listas import productos

procesar = procesar_lista

lista_filtrada_tecnologia = procesar(productos, filtrar_lista, "categoria", "tecnología", "igual")

mostrar_lista_diccionarios(lista_filtrada_tecnologia)

print("\nEl promedio de todos los precios es: ", procesar(productos, calcular_promedio, "precio"))
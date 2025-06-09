productos = [
    {"nombre": "Laptop", "precio": 1200, "categoria": "tecnología"},
    {"nombre": "Silla", "precio": 150, "categoria": "hogar"},
    {"nombre": "Smartphone", "precio": 800, "categoria": "tecnología"},
    {"nombre": "Mesa", "precio": 300, "categoria": "hogar"},
    {"nombre": "Auriculares", "precio": 200, "categoria": "tecnología"}
]

def filtrar_lista(lista: list, key: str, value: any):
    lista_retorno = []
    for elem in lista:
        if elem[key] == value:
            lista_retorno.append(elem)
    return lista_retorno

def calcular_promedio(lista: list, key: str):
    total = 0
    for elem in lista:
        total += elem[key]
    return total / len(lista)

def procesar_productos(lista: list, funcion: callable, *args):
    return funcion(lista, *args)

procesar = procesar_productos

lista_filtrada = procesar(productos, filtrar_lista, "categoria", "tecnología")
for e in lista_filtrada:
    print(f"Nombre: {e['nombre']} - Precio: ${e['precio']} - Categoría: {e['categoria']}")

print("\nEl promedio de todos los precios es: ", procesar_productos(productos, calcular_promedio, "precio"))
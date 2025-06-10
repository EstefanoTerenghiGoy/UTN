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

def generar_filtro(key: str, value: any):
    def filtro(lista: list):
        return filtrar_lista(lista, key, value)
    return filtro

def generar_calculo_promedio(key: str):
    def promedio(lista: list):
        return calcular_promedio(lista, key)
    return promedio

def procesar_productos(lista: list, funcion: callable):
    return funcion(lista)


procesar = procesar_productos

promedio_precio = generar_calculo_promedio("precio")
filtro_tecnologia = generar_filtro("categoria", "tecnología")

lista_filtrada = procesar(productos, filtro_tecnologia)
for e in lista_filtrada:
    print(f"Nombre: {e['nombre']} - Precio: ${e['precio']} - Categoría: {e['categoria']}")


print("\nEl promedio de todos los precios es: ", procesar_productos(productos, promedio_precio))


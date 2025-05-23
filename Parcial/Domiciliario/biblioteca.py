def obtener_numero(mensaje: str) -> int:
    """
    Valida el input del usuario en caso de que la opcion deba ser numérica positiva y
    devuelve la opcion transformada en número
    """
    cadena = input(mensaje)
    while not cadena.isdigit():
        cadena = input("Ingrese un valor válido: ")
    return int(cadena)



def listar_ventas_trimestrales(ventas: list) -> list:
    """
    Dada la matriz de ventas, devuelve una lista con el total de la venta de los 3 trimestres
    """
    ventas_trimestrales = [["A", 0], ["B", 0], ["C", 0]] #Para usar en mas de una función, le asigno cada valor a su producto
    for i in range(len(ventas)):
        for j in range(len(ventas[i])):
            ventas_trimestrales[i][1] += ventas[i][j]
    return ventas_trimestrales




def mostrar_productos_y_ventas(productos: list, ventas:list):
    """
    Dada la matriz de productos, sus ventas y el total de sus ventas, muestra sus datos
    de una forma legible y ordenada
    """
    ventas_trimestrales = listar_ventas_trimestrales(ventas)
    print("-"*32)
    print("Producto | T1 | T2 | T3 | Total")
    print("-"*32)
    for i in range(3):
        print(" "*6, productos[i], end=" | ")
        for j in range(3):
            print(ventas[i][j], sep=" | ", end=" | ") 
        print(ventas_trimestrales[i][1], end=" ") #Solo muestro los valores de ventas trimestrales, no su producto
        print("")

def ordenar_productos_segun_venta_anual(ventas) -> list:
    """
    Dada la matriz de las ventas, llama a la funcion que calcula las ventas trimestrales
    y devuelve una lista ordenada de las mismas
    """
    ventas_trimestrales = listar_ventas_trimestrales(ventas)
    print(ventas_trimestrales)
    
    for i in range(len(ventas_trimestrales) - 1):
        for j in range(i+1, len(ventas_trimestrales)):
            if ventas_trimestrales[i][1] < ventas_trimestrales[j][1]:
                aux = ventas_trimestrales[i]
                ventas_trimestrales[i] = ventas_trimestrales[j]
                ventas_trimestrales[j] = aux
    return ventas_trimestrales


def mostrar_productos_ordenados(ventas_ordenadas: list):
    """
    Dada la lista de ventas ordendas, imprime los productos ordenados de forma formateada
    """
    print("-"*18)
    print("Producto | Total")
    print("-"*18)
    for i in range(len(ventas_ordenadas)):
        for j in range(len(ventas_ordenadas[i])):
            print(" "*4, ventas_ordenadas[i][j], end=" ")
        print("")


def comprobar_existencia_de_producto(productos, producto) -> bool:
    """
    Dada la lista de productos y un producto indicado por el usuario,
    comprueba que exista dentro de la lista
    """
    existe = False
    for i in range(len(productos)):
        if productos[i] == producto:
            existe = True
    return existe

def buscar_producto_por_nombre(productos: list, ventas: list, producto: str) -> list:
    """
    Dada la lista de productos y ventas, encuentra el producto dado por el usuario
    y devuelve una lista de información sobre el producto
    """
    info_producto = []
    info_producto.append(producto)

    for i in range(len(productos)):
            if productos[i] == producto:
                for j in range(len(ventas)):
                    info_producto.append(ventas[i][j])
    return info_producto

def mostrar_producto_por_nombre(info_producto: list):
    """
    Dada la información del producto, imprime sus ventas en un formato formateado
    """
    print("-" * 40)
    print(f"{'Producto':<15} {'T1':>7} {'T2':>7} {'T3':>7}")
    print("-" * 40)
    print(f"{info_producto[0]:<15} {info_producto[1]:>7} {info_producto[2]:>7} {info_producto[3]:>7}")


def comprobar_existencia_de_venta(ventas, venta) -> bool:
    """
    Dada la matriz de ventas y la venta indicada por el usuario,
    verifica que la venta exista, y devuelve un valor True en caso de que asi sea,
    o False si no se cumple
    """
    existe = False
    for i in range(len(ventas)):
        for j in range(len(ventas[i])):
            if ventas[i][j] == venta:
                existe = True
    return existe

def buscar_producto_y_trimestre_por_venta(productos: list, ventas: list, venta:int) -> list:
    """
    Dada la lista de productos, ventas y la venta que el usuario quiera filtrar,
    busca y devuelve los 3 datos en una matriz, en caso de que haya mas de uno,
    guarda los datos de todos ellos
    """
    venta_producto_trimestre = []
    for i in range(len(ventas)):
        for j in range(len(ventas[i])):
            if ventas[i][j] == venta:
                venta_producto_trimestre.append([venta, productos[i], f"T{j+1}"])
    return venta_producto_trimestre

def mostrar_producto_y_trimestre(venta_producto_trimestre: list):
    """
    Dada la lista del producto, su venta y su trimestre, los imprime en un formato formateado
    """
    
    print("-" * 35)
    print(f"{'Ventas':<10} {'Producto':<10} {'Trimestre':<10}")
    print("-" * 35)
    for i in range(len(venta_producto_trimestre)):
        venta = venta_producto_trimestre[i][0]
        producto = venta_producto_trimestre[i][1]
        trimestre = venta_producto_trimestre[i][2]
        print(f"{venta:<10} {producto:<10} {trimestre:<10}")
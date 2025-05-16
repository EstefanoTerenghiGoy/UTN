def comprobar_existencia_de_producto(matriz:list, producto:str) -> bool: 
    encontrado = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            for k in range(len(matriz[i][j])):
                if matriz[i][j][0].lower() == producto.lower():
                    encontrado = True
                    break
    return encontrado

def alta_producto(matriz:list, producto:str, cantidad:int)->bool: 
    ubicacion = pedir_ubicacion(matriz)
    fila = ubicacion[0]
    columna = ubicacion[1]
        
    if matriz[fila][columna] != "Vacío":
        return False
    else:
        
        nueva_lista = ["", 0]
        nueva_lista[0] = producto
        nueva_lista[1] = cantidad
        matriz[fila-1][columna-1] = nueva_lista            
    return True

def baja_producto(matriz:list) -> bool:
    ubicacion = pedir_ubicacion(matriz)
    fila = ubicacion[0]
    columna = ubicacion[1]
    if matriz[fila - 1][columna - 1] == "Vacío":
        return False
    else:
        matriz[fila - 1][columna - 1] = "Vacío"
    return True

def pedir_ubicacion(matriz: list) -> list:
    cantidad_filas = len(matriz)
    cantidad_columnas = len(matriz[0])

    
    fila = int(input("Ingrese la fila: "))
    while fila < 1 or fila > cantidad_filas:
        fila = int(input(f"Ingrese un valor entre 1 y {cantidad_filas}: "))
    
    columna = int(input("Ingrese la columna: "))
    while columna < 1 or columna > cantidad_columnas:
        columna = int(input(f"Ingrese un valor entre 1 y {cantidad_columnas}: "))
    
    return [fila, columna]

def modificar_producto(matriz: list, cantidad: int = -1, cambiar_ubicacion=False) -> str:
    print("Ingrese la ubicación actual del producto")
    ubicacion = pedir_ubicacion(matriz)
    fila = ubicacion[0] - 1
    columna = ubicacion[1] - 1

    
    if matriz[fila][columna] == "Vacío":
        return "No hay producto en esta posición."

    if cantidad != -1:
        matriz[fila][columna][1] = cantidad

    if cambiar_ubicacion:
        print("Ingrese la nueva ubicación del producto")
        nueva_ubicacion = pedir_ubicacion(matriz)
        nueva_fila = nueva_ubicacion[0] - 1
        nueva_columna = nueva_ubicacion[1] - 1
        
        if matriz[nueva_fila][nueva_columna] != "Vacío":
            return "Ya hay un producto en la nueva posición seleccionada."
        else:
            matriz[nueva_fila][nueva_columna] = matriz[fila][columna]
            matriz[fila][columna] = "Vacío"

        

    return "Producto modificado correctamente."


def listar_producto(matriz: list) -> list:
    productos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if type(matriz[i][j]) == list:
                for k in range(len(matriz[i][j])):
                    if k == 0:
                        nombre = matriz[i][j][k]
                    else:
                        cantidad = matriz[i][j][k]
                        productos.append(f"{nombre}({cantidad})")
    return productos

def listar_productos_por_nombre(matriz: list) -> list:
    productos = listar_producto(matriz)
    
    for i in range(len(productos) - 1):
        for j in range(i+1, len(productos)):
            if productos[j] < productos[i]:
                auxProducto = productos[i]
                productos[i] = productos[j]
                productos[j] = auxProducto
    return productos
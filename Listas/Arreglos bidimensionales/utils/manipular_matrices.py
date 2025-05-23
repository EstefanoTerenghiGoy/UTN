#Matrices simples

def mostrar_matriz(matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(" | ", matriz[i][j], end=" | ")
        print("") 

def mostrar_elementos(matriz:list): 
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j])

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        
        matriz += [fila]
        
    return matriz

def carga_matriz_aleatoria(matriz:list, cantidad_filas:int, cantidad_columnas:int, dato = None):
    
    opcion = "s"
    while opcion == "s":
        
        fila = int(input("Ingrese la fila: "))
        while fila < 1 or fila > cantidad_filas:
            fila = int(input(f"Ingrese un valor entre 1 y {cantidad_filas}: "))
        
        columna = int(input("Ingrese la columna: "))
        while columna < 1 or columna > cantidad_columnas:
            columna = int(input(f"Ingrese un valor entre 1 y {cantidad_columnas}: "))
        
        if dato == None:
            dato = input("Ingrese el dato: ") #Validar cuando pueda usar try
        else:
            matriz[fila-1][columna-1] = dato
        opcion = input("Desea poner otro dato? S/N: ").lower()

def inicializar_y_cargar_matriz():
    cantidad_filas = int(input("Ingrese la cantidad de filas: "))
    cantidad_columnas = int(input("Ingrese la cantidad de columnas: "))
    tipo_matriz = input("Ingrese de qué tipo de dato quiere que sea su matriz:\n1. Números\n2. Palabras\n").lower()
    
    match tipo_matriz:
        case "1" | "numeros" | "números":
            valor_inicial = 0
        case "2" | "palabras":
            valor_inicial = "Vacío"
        case _:
            print("Elija una opción válida")
            
    matriz = inicializar_matriz(cantidad_filas, cantidad_columnas, valor_inicial)
    
    carga_matriz_aleatoria(matriz, cantidad_filas, cantidad_columnas)
    
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("")

#Matrices complejas

def mostrar_matriz_triple(matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if type(matriz[i][j]) == list:
                for k in range(len(matriz[i][j])):
                    if k == 0:
                        nombre = matriz[i][j][k]
                    else:
                        cantidad = matriz[i][j][k]
                        print(f" | {nombre}({cantidad}) ", end=" | ") #print("{:<30} {:<20}".format("Apellidos", "Notas"))
            else:
                print(" | ", matriz[i][j], end=" | ")
        print("") 
        
def carga_matriz_aleatoria_triple(matriz:list, cantidad_filas:int, cantidad_columnas:int, dato = None): #GENERALIZAR
    
    opcion = "s"
    while opcion == "s":
        
        fila = int(input("Ingrese la fila: "))
        while fila < 1 or fila > cantidad_filas:
            fila = int(input(f"Ingrese un valor entre 1 y {cantidad_filas}: "))
        
        columna = int(input("Ingrese la columna: "))
        while columna < 1 or columna > cantidad_columnas:
            columna = int(input(f"Ingrese un valor entre 1 y {cantidad_columnas}: "))
        
        if dato == None:
            dato = input("Ingrese el dato: ") #Validar cuando pueda usar try
        
        cantidad = int(input("Ingrese la cantidad del producto: "))
        
        nueva_lista = [None, None]
        nueva_lista[0] = dato
        nueva_lista[1] = cantidad
        matriz[fila-1][columna-1] = nueva_lista
        
        opcion = input("Desea poner otro dato? S/N: ").lower()
def validar_coordenadas(tablero: list, x:int, y:int)->bool:
    hundido = False
    if tablero[x][y] == 1:
        hundido = True
    return hundido
tablero = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1]
    ]
opcion = "s"
hundidos = 0
while opcion == "s":    
    fila = int(input("Ingrese la fila entre 0 y 4: "))
    while fila < 0 or fila > 4:
        fila = int(input("Ingrese una posicion entre 0 y 4: "))
    columna = int(input("Ingrese la columna entre 0 y 4: "))
    while columna < 0 or columna > 4:
        columna = int(input("Ingrese una posicion entre 0 y 4: "))
    if validar_coordenadas(tablero, fila, columna):
        print("Hundido")
        hundidos += 1
    else:
        print("Agua")
    opcion = input("¿Desea disparar otra vez? (S/N): ".lower())
print(f"Hundió {hundidos} barco(s)")

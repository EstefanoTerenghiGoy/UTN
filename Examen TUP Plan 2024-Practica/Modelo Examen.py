def verificar_tesoro(mapa: list, x: int, y: int) -> int:
    '''
    Devuelve 0 si se encuentra el valor 1 en "mapa", o
    la distancia hasta él en caso contrario
    '''
    
    #Si se encuentra, devuelve 0
    if mapa[x][y] == 1: 
        return 0
    #Sino, encuentro el tesoro y calculo la distancia hacia él
    else:
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if mapa[i][j] == 1:
                    tesoro_x = i
                    tesoro_y = j
        distancia_manhattan = (x - tesoro_x) + (y - tesoro_y)
        if distancia_manhattan < 0:
            distancia_manhattan *= -1
        return distancia_manhattan
mapa = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
opcion = "s"
while opcion == "s":
    coordenada_x = int(input("Ingrese la coordenada X (Entre 0 y 4 inclusive): ")) #No se pide verificar
    coordenada_y = int(input("Ingrese la coordenada Y (Entre 0 y 4 inclusive): ")) 
    verificar = verificar_tesoro(mapa, coordenada_x, coordenada_y)
    if verificar == 0:
        print("¡Encontraste el tesoro!")
        opcion = "n"
    else:    
        print(f"Fallaste. El tesoro esta a {verificar} casilleros de distancia")
        opcion = input("¿Desea continuar? S/N: ")
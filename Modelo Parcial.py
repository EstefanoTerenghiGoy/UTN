matriz = [
        [5, 2, 3, 4],
        [5, 2, 7, 8],
        [2, 2, 3, 1],
        [1, 6, 7, 4]]

def recorrer_columnas(matriz):
    numero_encontrado = None
    contador_columnas = 0
    columnas = []
    for i in range(len(matriz)):
        columna = []
        for j in range(len(matriz)):
            columna.append(matriz[j][contador_columnas])
        columnas.append(columna)
        contador_columnas+=1
    #Hasta aca
    
    
    for i in range(len(columnas)):
        for j in range(len(columnas[i]) - 2):
            if columnas[i][j] == columnas[i][j+1] and columnas[i][j] == columnas[i][j+2]:
                numero_encontrado = columnas[i][j]
    return numero_encontrado
                
    # print(columnas)

if recorrer_columnas(matriz) is not None:
    print("El número que se repite es: ", recorrer_columnas(matriz))
else:
    print("Ningun número se repite")
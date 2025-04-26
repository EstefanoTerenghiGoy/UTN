def pedir_posicion_y_numero(numero: int, posicion: int)->list:
    
    
    numeros = [0] * 10
    numeros[posicion] = numero
    return numeros

numero = int(input("Ingrese el número que quiere guardar: "))
posicion = int(input("Indique la posición en donde lo quiere guardar: "))

print(pedir_posicion_y_numero(numero, posicion - 1))
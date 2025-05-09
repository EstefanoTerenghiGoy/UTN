def pedir_numeros() -> list:
    numeros = []
    rango_minimo = 1
    rango_maximo = 10
    
    for i in range(10):
        numero = int(input("Ingrese un valor entre 1 y 10: "))
        while not (numero >= 1 and numero <= 10):
            numero = int(input("Ingrese un valor válido: "))
        numeros += [numero]
    return numeros


print(pedir_numeros())
numero = int(input("Ingrese un número: "))

if numero <= 1:
    print("El número debe ser mayor que 1 para ser considerado primo")
else:
    for i in range(2, numero):
        numTemporal = numero % i
        if numTemporal == 0:
            print("No es primo")
            break
    else: #Un else en un for solo se activa al no cortarse el for con un break. Tambien se puede usar una Flag
        print("Es primo")
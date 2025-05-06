# def buscar_numero(numeros: list, numero: int) -> bool:
#     return numero in numeros

# numeros = [1, 2, 3, 4, 5, 7, 8, 9, 10]
# numero = 1
# if buscar_numero(numeros, numero):
#     print("El número está en la lista")
# else:
#     print("El número no está en la lista")
    


def buscar_numero(numeros: list, numero: int) -> bool:
    encontrado = False
    for i in range(len(numeros)):
        if numeros[i] == numero:
            encontrado = True
            break
    return encontrado

numeros = [1, 2, 3, 4, 5, 7, 8, 9, 10]
numero = 2
if buscar_numero(numeros, numero):
    print("El número está en la lista")
else:
    print("El número no está en la lista")
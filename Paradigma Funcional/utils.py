def filtrar_lista(lista: list, key: str, value: any, opcion: str):
    lista_retorno = []
    
    
    for elem in lista:
        match opcion:
            case "igual":
                if elem[key] == value:
                    lista_retorno.append(elem)
            case "mayor":
                if elem[key] > value:
                    lista_retorno.append(elem)
            case "menor":
                if elem[key] < value:
                    lista_retorno.append(elem)
            case _:
                print("Opción inválida")
                break
    return lista_retorno


def calcular_promedio(lista: list, key: str):
    total = 0
    for elem in lista:
        total += elem[key]
    return total / len(lista)

def ordenar_lista(lista:list, key: str, opcion: str):
    lista_ordenada = lista[:]
    for i in range(len(lista_ordenada) - 1):
        for j in range(i+1, len(lista_ordenada)):
            match opcion:
                case "ascendente":
                    if lista_ordenada[i][key] > lista_ordenada[j][key]:
                        swap_multiple(lista_ordenada, i, j)
                case "descendente":
                    if lista_ordenada[i][key] < lista_ordenada[j][key]:
                        swap_multiple(lista_ordenada, i, j)
    return lista_ordenada

def procesar_lista(lista: list, funcion: callable, *args):
    return funcion(lista, *args)

def swap_multiple(datos_a_intercambiar: list, i:int, j:int):
    aux = datos_a_intercambiar[i]
    datos_a_intercambiar[i] = datos_a_intercambiar[j]
    datos_a_intercambiar[j] = aux 
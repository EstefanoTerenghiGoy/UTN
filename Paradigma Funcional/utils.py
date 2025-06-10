def filtrar_lista(lista: list, key: str, value: any, opcion: str):
    """
    Crea una lista nueva que se llena solo con datos indicados, y como compararlos,
    retorna la nueva lista
    """
    
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
    """
    Calcula el promedio de una cantidad indefinida de valores dada su key
    """
    total = 0
    for elem in lista:
        total += elem[key]
    return total / len(lista)

def ordenar_lista(lista:list, key: str, opcion: str):
    """
    Crea una copia de la lista original y la ordena de forma ascendente o descendente,
    segun lo indicado por parametro, mediante su key
    """
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
    """
    Dada la función, se pueden o no pasar los parametros que hagan falta para
    esa función (mediante *args)
    """
    return funcion(lista, *args)

def swap_multiple(datos_a_intercambiar: list, i:int, j:int):
    """
    Ordena los datos de una lista mediante "swap"
    """
    aux = datos_a_intercambiar[i]
    datos_a_intercambiar[i] = datos_a_intercambiar[j]
    datos_a_intercambiar[j] = aux 


def mostrar_lista_diccionarios(lista: list):
    for elem in lista:
        print("-----")
        for clave, valor in elem.items():
            print(f"{clave.capitalize()}: {valor}")


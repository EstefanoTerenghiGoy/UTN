import json

def mostrar_menu():
    print("""
    Elija una opción: 
    1 - Leer Archivo JSON
    2 - Generar CSV
    3 - Convertir lista de JSON en CSV
    4 - Ordenar heroes por clave
    """)

def mostrar_lista_diccionarios(lista: list):
    """
    Muestra una lista de diccionarios de manera formateada
    """
    for elem in lista:
        print("-----")
        for clave, valor in elem.items():
            print(f"{clave.capitalize()}: {valor}")


def leer_json(lista: str, ruta: str):
    """
    Dado el nombre de un archivo y su ruta, lee sus datos y los retorna en caso de existir,
    en caso contrario, devuelve un mensaje de error
    """
    salida = ""
    try:
        with open(ruta, "r") as archivo:
            salida = json.load(archivo)
            salida = salida[lista]
    except FileNotFoundError:
        salida = "Archivo no encontrado"
    except KeyError:
        salida = "Lista no encontrada"
    return salida
        

def guardar_archivo(nombre_archivo: str, data: str):
    """
    Dado un nombre de archivo y su contenido, crea un archivo CSV,
    si ya existe, lo sobreescribe
    """
    retorno = ""
    try:
        with open(nombre_archivo, "w+") as archivo:
            archivo.write(data)
            retorno = "Archivo creado/modificado"
    except Exception as e:
        retorno = str(e)
    return retorno

def guardar_archivo_csv(nombre_archivo: str, data: list):
    """
    Dado una lista con datos JSON, crea o sobreescribe un archivo CSV
    """
    with open(nombre_archivo, "w+") as archivo:
        titulos = list(data[0].keys())
        archivo.write(",".join(titulos) + "\n")
        
        for elem in data:
            datos = []
            for titulo in titulos:
                datos.append(str(elem[titulo]))
            archivo.write(",".join(datos))
            archivo.write("\n")
            
def ordenar_lista(lista:list, key: str, opcion: str):
    """
    Crea una copia de la lista original y la ordena de forma ascendente o descendente,
    segun lo indicado por parametro, mediante su key
    """
    if key not in lista:
        lista_ordenada = []
        print("Clave no encontrada")
    else:
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
    

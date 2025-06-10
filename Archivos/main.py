from biblioteca import *

mostrar_menu()
opcion = int(input("Ingrese una opción: "))

data_heroes = (leer_json("heroes", "D:\Trabajos\Programación\Archivos\data_stark.json"))
data_villanos = (leer_json("villanos", "D:\Trabajos\Programación\Archivos\data_stark.json"))


match opcion:
    case 1:
        mostrar_lista_diccionarios(leer_json("heroes", "D:\Trabajos\Programación\Archivos\data_stark.json"))
    case 2:
        guardar_archivo("prueba.txt", "Esto es una prueba")
    case 3:
        guardar_archivo_csv("heroes.csv", data_heroes)
        guardar_archivo_csv("villanos.csv", data_villanos)
    case 4:
        clave = input("Ingrese la clave por la que quiere ordenar la lista (Peso - altura - fuerza): ")
        lista_filtrada = procesar_lista(data_heroes, ordenar_lista, clave, "ascendente")
        mostrar_lista_diccionarios(lista_filtrada)
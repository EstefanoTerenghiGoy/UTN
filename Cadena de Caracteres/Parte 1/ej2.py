def cadena_entre_indices(cadena, indice_inicio, indice_fin):
    return cadena[indice_inicio:indice_fin]

cadena = input("Ingrese una palabra: ")
indice_inicio = int(input("Ingrese desde dónde desea cortar (Desde 0 hasta el largo de la palabra): "))
while indice_inicio < 0 or indice_inicio > len(cadena):
    indice_inicio = int(input("Ingrese un valor dentro del rango: "))

indice_fin = int(input("Ingrese hasta dónde desea cortar (Desde 0 hasta el largo de la palabra): "))
while indice_fin < 0 or indice_fin > len(cadena):
    indice_fin = int(input("Ingrese un valor dentro del rango: "))

print(cadena_entre_indices(cadena, indice_inicio, indice_fin))
    
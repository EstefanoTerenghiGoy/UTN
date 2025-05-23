def primer_caracter(cadena, caracter):
    indice_caracter = -1
    for i in range(len(cadena)):
        if cadena[i].lower() == caracter.lower():
            indice_caracter = i
    return indice_caracter

primera_ocurrencia = primer_caracter("Hola", "s") 
if  primera_ocurrencia == -1:
    print("No se encontró ese caracter")
else:
    print(f"El caracter esta en la posicion: {primera_ocurrencia}")
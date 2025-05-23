def suprimir_repetidos(cadena):
    nueva_cadena = ""
    for letra in cadena:
        if letra not in nueva_cadena:
            nueva_cadena += letra
        
    return nueva_cadena

print(suprimir_repetidos("hoooola"))
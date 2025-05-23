def suprimir_vocales(cadena):
    nueva_cadena = ""
    for letra in cadena:
        if letra in ["a", "e", "i", "o", "u"]: # == letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u": EQUIVALENTES
            continue
        else:
            nueva_cadena+=letra
    return nueva_cadena

print(suprimir_vocales("hola"))
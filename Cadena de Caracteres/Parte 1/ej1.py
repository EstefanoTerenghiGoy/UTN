def encontrar_cantidad_de_letras(palabra, letra):
    contador = 0
    for caracter in palabra:
        if caracter == letra:
            contador+=1
    return contador

palabra = "elefante"
letra = "e"
print(f"La cantidad de {letra} en {palabra} es: {encontrar_cantidad_de_letras(palabra, letra)}")


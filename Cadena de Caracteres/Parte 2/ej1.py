def contar_vocales(cadena):
    vocales = [["a", 0], ["e", 0], ["i", 0], ["o", 0], ["u", 0]]
    
    for caracter in cadena:
        for i in range(len(vocales)):
            if caracter.lower() == vocales[i][0]:
                vocales[i][1]+=1
    
    return vocales

print(contar_vocales("murcielaguito"))

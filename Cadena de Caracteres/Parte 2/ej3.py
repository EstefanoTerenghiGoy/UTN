def es_palindromo(cadena):
    return cadena == cadena[::-1]

if es_palindromo("anilina"):
    print("Es palindromo")
else:
    print("No es palindromo")
#12. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def devolver_string() -> str:
    cadena = str(input("Ingrese una cadena de texto: "))
    return cadena


print(devolver_string())
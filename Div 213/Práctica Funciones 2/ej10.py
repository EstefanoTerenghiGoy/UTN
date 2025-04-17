#10. Crear una función que le solicite al usuario el ingreso de un número entero y lo
#retorne.

def devolver_entero() -> int:
    numeroEntero = int(input("Ingrese un número entero: "))
    return numeroEntero


print(devolver_entero())
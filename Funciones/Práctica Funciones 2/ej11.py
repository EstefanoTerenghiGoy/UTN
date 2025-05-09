#11. Crear una función que le solicite al usuario el ingreso de un número flotante y lo
#

def devolver_flotante() -> float:
    numeroFloat = float(input("Ingrese un número con coma: "))
    return numeroFloat


print(devolver_flotante())
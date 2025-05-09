# 6. Diseña una función que calcule la potencia de un número. La función debe recibir la
# base y el exponente como argumentos y devolver el resultado.

def potenciarNumero(base:int,exponente:int)->int:
    resultado = base ** exponente
    return resultado

base = int(input("Ingrese el numero de base: "))
exponente = int(input("Ingrese el exponente: "))

print(potenciarNumero(base, exponente))
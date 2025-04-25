def sumar_digitos(numero: int) -> int:
    if numero == 0:
        return 0
    else:
        return numero % 10  + sumar_digitos(numero // 10)

numero = int(input("Ingrese el número para sumar sus digitos:  "))
print(sumar_digitos(numero))

def sumar_naturales(numero: int) -> int:
    if numero <= 0:
        return 0
    else:
        return numero + sumar_naturales(numero - 1)

numero = int(input("Ingrese el número para sumar desde 1 hasta él: "))
print(sumar_naturales(numero))

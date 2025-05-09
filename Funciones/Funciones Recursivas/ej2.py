def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    else:
        return base * (calcular_potencia(base, exponente - 1))
        
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

print(calcular_potencia(base, exponente))

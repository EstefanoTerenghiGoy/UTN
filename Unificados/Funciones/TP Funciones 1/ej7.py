def sumar_o_restar(num1: int, num2: int, op: str) -> int:
    if op == 's':
        return num1 + num2
    else:
        return num1 - num2

numero1 = int(input("Ingrese un número mayor a 10 y menor a 100: "))
while numero1 <= 10 or numero1 >= 100:
    print("Ingrese un valor válido.")
    numero1 = int(input("Ingrese un número mayor a 10 y menor a 100: "))

numero2 = int(input("Ingrese otro número mayor a 10 y menor a 100: "))
while numero2 <= 10 or numero2 >= 100:
    print("Ingrese un valor válido.")
    numero2 = int(input("Ingrese otro número mayor a 10 y menor a 100: "))

operacion = input("\nIngrese 's' para sumar o 'r' para restar ambos números: ").lower()
while operacion != 's' and operacion != 'r':
    print("\nIntente de nuevo.")
    operacion = input("Ingrese 's' para sumar o 'r' para restar ambos números: ").lower()

resultado = sumar_o_restar(numero1, numero2, operacion)
print(f"\nEl resultado es: {resultado}")

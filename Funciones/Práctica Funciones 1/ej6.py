def realizarDescuento(num1: int):
    if num1 > 10 and num1 < 100:
        num1 = num1 * 0.95
    print(num1)

numero1 = int(input("Ingrese un número: "))
realizarDescuento(numero1)


# Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor solicitado al usuario, valide el
# mismo entre 10 y 100, realice un descuento del 5% a dicho valor a través de una función llamada realizarDescuento().
# Mostrar el resultado por pantalla. Atención: pueden reutilizarse funciones ya creadas.
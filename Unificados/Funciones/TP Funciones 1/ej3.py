def numero_par(numero:int)->bool:
    return numero % 2 == 0
    

numero = int(input("Ingrese un número: "))

if numero_par(numero):
    print("El número ingresado es par.")
else:
    print("El número ingresado es impar")
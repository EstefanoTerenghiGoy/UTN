def es_par(num1: int): 
    if num1 % 2 == 0:
        print(f"El número {num1} es par")
    else:
        print(f"El número {num1} es impar")
        
numero = int(input("Ingrese un número: "))
es_par(numero)
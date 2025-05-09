# 5. Define una función que encuentre el máximo de tres números. La función debe
# aceptar tres argumentos y devolver el número más grande.

def numero_mas_grande(num1:int,num2:int,num3:int)->int:
    maximo = num1
    if num2 > maximo:
        maximo = num2
    if num3 > maximo:
        maximo = num3
    return maximo

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

print(f"El número mas grande es: {numero_mas_grande(num1, num2, num3)}") 

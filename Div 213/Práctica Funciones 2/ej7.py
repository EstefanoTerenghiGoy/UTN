# 7. Crear una función que reciba un número y retorne True si el número es primo, False
# en caso contrario.

def determinar_primo(num:int)->bool:
    flag = True
    for i in range(2, num):
        if (num % i) == 0:
            flag = False
    return flag

numero = int(input("Ingrese un número: "))

if determinar_primo(numero):
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")
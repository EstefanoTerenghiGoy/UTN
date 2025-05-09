
def calcular_fibonacci(num: int)->int:
    if num == 0 or num == 1:
        return num
    else:
        return calcular_fibonacci(num - 1) + calcular_fibonacci(num - 2)

print(calcular_fibonacci(9))
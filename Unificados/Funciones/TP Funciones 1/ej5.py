def restar1(num1:int,num2:int)->int:
    resta = num1 - num2
    return resta
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))
print(restar1(num1, num2))


def restar2()->int:
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese un número: "))
    resta = num1 - num2
    return resta
print(restar2())


def restar3(num1:int, num2:int):
    resta = num1 - num2
    print(resta)
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))
restar3(num1, num2)


def restar4():
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese un número: "))
    resta = num1 - num2
    print(resta)
restar4()
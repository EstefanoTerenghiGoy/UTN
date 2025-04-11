num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
num4 = int(input("Ingrese el cuarto numero: "))
num5 = int(input("Ingrese el quinto numero: "))

pares = 0
impares = 0
numMenor = num1
numMayorPar = 0

if (num1 % 2) == 0:
    pares+=1
    if num1 > numMayorPar:
        numMayorPar = num1
else:
    impares+=1
if (num2 % 2) == 0:
    pares+=1
    if num2 > numMayorPar:
        numMayorPar = num2
else:
    impares+=1
if (num3 % 2) == 0:
    pares+=1
    if num3 > numMayorPar:
        numMayorPar = num3
else:
    impares+=1
if (num4 % 2) == 0:
    pares+=1
    if num4 > numMayorPar:
        numMayorPar = num4
else:
    impares+=1
if (num5 % 2) == 0:
    pares+=1
    if num5 > numMayorPar:
        numMayorPar = num5
else:
    impares+=1   




if num2 < num1:
    numMenor = num2
    
if num3 < num2:
    numMenor = num3
    
if num4 < num3:
    numMenor = num4
    
if num5 < num4:
    numMenor = num5
    
print(f"El numero menor es: {numMenor}")

sumaPositivos = 0
productoNegativos = 1

if num1 > 0:
    sumaPositivos+=num1
else:
    productoNegativos *= num1
if num2 > 0:
    sumaPositivos+=num2
else:
    productoNegativos *= num2
if num3 > 0:
    sumaPositivos+=num3
else:
    productoNegativos *= num3
if num4 > 0:
    sumaPositivos+=num4
else:
    productoNegativos *= num4
if num5 > 0:
    sumaPositivos+=num5
else:
    productoNegativos *= num5


print(f"La cantidad de pares es: {pares}")
print(f"La cantidad de impares es: {impares}")
print(f"El numero mayor entre los pares es: {numMayorPar}")
print(f"La suma de los positivos es: {sumaPositivos}") 
print(f"El producto de los negativos: {productoNegativos}")


vueltas = 1

numero = int(input("Ingrese un número: "))

maximo = numero
minimo = numero

while vueltas <= 10:
    
    numero = int(input("Ingrese un número: "))
    
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero
    vueltas += 1
    

print(maximo)
print(minimo)
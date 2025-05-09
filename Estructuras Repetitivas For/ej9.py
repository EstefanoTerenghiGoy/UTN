numero = int(input("Ingrese un número: "))

for i in range(numero):
    if numero % (i+1) == 0:
        print(i+1)
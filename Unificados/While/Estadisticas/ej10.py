print("Ingrese por lo menos 5 números, hasta 10 como máximo\n")
opcion = "s"
vueltas = 0
promedio = 0
total = 0

while opcion == "s":
    
    numero = int(input("Ingrese un número: "))
    total += numero
    if vueltas >= 4 and vueltas != 9:
        opcion = input("Desea agregar mas números? s/n: ")
    if vueltas == 9:
        opcion = "n"
    vueltas += 1
    
print(total)
print(total / vueltas)
print("Ingrese por lo menos 5 números\n")
opcion = "s"
vueltas = 0
promedio = 0
total = 0

while opcion == "s":
    
    numero = int(input("Ingrese un número: "))
    total += numero
    if vueltas >= 4:
        opcion = input("Desea agregar mas números? s/n: ")
    
    vueltas += 1
    
print(total)
print(total / vueltas)
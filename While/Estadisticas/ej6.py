opcion = "s"
total = 0
vueltas = 0

while opcion == "s":
    numero = int(input("Ingrese un número: "))
    total += numero
    
    opcion = input("¿Quiere seguir ingresando números? s/n: ")
    vueltas += 1

print(total)
print(total / vueltas)

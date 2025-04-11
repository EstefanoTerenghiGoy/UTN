opcion = "s"
sumaPositivos = 0
productoNegativos = 1

while opcion == "s":
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        sumaPositivos += numero
    else:
        productoNegativos *= numero
    opcion = input("¿Quiere seguir ingresando números? s/n: ")
    
print(sumaPositivos)
print(productoNegativos)
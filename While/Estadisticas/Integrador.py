opcion = "s"
vueltas = 0
sumaPositivos = 0
sumaNegativos = 0
cantNegativos = 0
promedioPositivos = 0
numMaximoPositivos = 0
porcNegativos = 0

while opcion == "s":
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        sumaPositivos += numero
        if numero > numMaximoPositivos:
            numMaximoPositivos = numero
    else:
        sumaNegativos += numero
        cantNegativos += 1
        
    
    
    vueltas += 1
    opcion = input("¿Quiere continuar ingresando números? s/n: ")

promedioPositivos = sumaPositivos / vueltas
porcNegativos = (cantNegativos * 100) / vueltas

print(f"\nLa suma de los positivos es: {sumaPositivos}")
print(f"La suma de los negativos es: {sumaNegativos}")
print(f"La cantidad de negativos es: {cantNegativos}")
print(f"El promedio de los números positivos es: {promedioPositivos}")
print(f"El número positivo mas grande es: {numMaximoPositivos}")
print(f"El porcentaje de números negativos es: {porcNegativos}%\n")



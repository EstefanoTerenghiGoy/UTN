total = 0
vueltas = 0

for i in range(10):
    numero = int(input("Ingrese un numero"))
    if numero != 0:
        total += numero
        vueltas = i+1
    else:
        break


promedio = total / vueltas

print(f"Total: {total}")
print(f"Promedio: {promedio}")
nota = int(input("Ingrese una nota del 1 al 10: "))
while nota < 1 or nota > 10:
    print("Ingrese una nota válida")
    nota = int(input("Ingrese una nota del 1 al 10: "))
    

print(f"La nota es {nota}")
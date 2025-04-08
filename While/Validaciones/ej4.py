color = input("Ingrese un color entre Rojo, Verde o Azul: ").lower()

while color != "rojo" and color != "verde" and color != "azul":
    print("Ingrese un color válido")
    color = input("Ingrese un color entre Rojo, Verde o Azul").lower()
    

print(f"El color elegido es {color}")
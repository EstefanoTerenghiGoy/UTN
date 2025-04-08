clave = input("Ingrese su clave: ")
seLogueo = True
intentos = 1

while clave != "clave123":
    if intentos != 3 :
        clave = input("Clave incorrecta, pruebe de nuevo: ")
    else:
        seLogueo = False
        break
    
    intentos += 1
    
if seLogueo:
    print("Bienvenido!")
else:
    print("Muchos intentos incorrectos")

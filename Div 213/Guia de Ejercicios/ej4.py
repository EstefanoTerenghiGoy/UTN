edad = int(input("Ingrese una edad: "))
estadoCivil = input("Ingrese su estado civil: ")

if edad < 18 and estadoCivil != "soltero":
    print("Es muy pequeño para NO ser soltero")
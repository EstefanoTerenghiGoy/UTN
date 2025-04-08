vueltas = 1

cant_masculino_iot_ia_25_50 = 0

cant_no_fem_no_ia_33_40 = 0
porc_no_fem_no_ia_33_40 = 0

nombre_masculino_mayor = ""
tecnologia_masculino_mayor = ""
edad_masculino_mayor = 0

while vueltas <= 10:
    
    nombre = input("Ingrese su nombre: ")
    
    edad = int(input("Ingrese su edad (Mayor a 18): "))
    while edad < 18:
        print("Ingrese una edad válida: ")
        edad = int(input("Ingrese su edad (Mayor a 18): "))
    
    genero = input("Ingrese su género (Masculino, femenino, otro): ").lower()
    while not(genero == "masculino" or genero == "femenino" or genero == "otro"):    
        print("Ingrese un género válido: ")
        genero = input("Ingrese su género (Masculino, femenino, otro): ").lower()
        
    tecnologia = input("Ingrese la tecnología con la que trabaja (IA, RV/RA, IOT)").lower()
    while not(tecnologia == "ia" or tecnologia == "rv/ra" or tecnologia == "iot"):
        print("Ingrese una tecnología válida")
        tecnologia = input("Ingrese la tecnología con la que trabaja (IA, RV/RA, IOT)").lower()
    
    if (genero == "masculino" and tecnologia == "iot" or tecnologia == "ia") and (edad >= 25 and edad <= 50):
        cant_masculino_iot_ia_25_50 += 1
    
    if tecnologia != "ia" and (genero != "femenino" or (edad >= 33 and edad <= 40)):
        cant_no_fem_no_ia_33_40 += 1
    
    if genero == "masculino":
        if edad > edad_masculino_mayor:
            edad_masculino_mayor = edad
            nombre_masculino_mayor = nombre
            tecnologia_masculino_mayor = tecnologia
    
    vueltas += 1
    
if cant_masculino_iot_ia_25_50 > 0:
    print(f"La cantidad de empleados masculinos con tecnología IOT - IA entre 25 y 50 es: {cant_masculino_iot_ia_25_50}") #bien
else:
    print("No hay empleados masculinos con tecnología IOT - IA entre 25 y 50")

if cant_no_fem_no_ia_33_40 > 0:
    porc_no_fem_no_ia_33_40 = (cant_no_fem_no_ia_33_40 * 100) / 10
    print(f"El porcentaje de empleados no femeninos que no usan tecnología IA entre 33 y 40 es: {porc_no_fem_no_ia_33_40}")
else:
    print("No hay empleados no femeninos que no usan tecnología IA entre 33 y 40")
    
if edad_masculino_mayor > 0:
    print(f"El empleado masculino con mayor edad es: {nombre_masculino_mayor} y su tecnología es: {tecnologia_masculino_mayor}")
else:
    print("No hay empleados masculinos")

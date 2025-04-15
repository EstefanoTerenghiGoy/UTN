opcion = "s"
cant_jugadores = 0

#Punto 1
cantidad_jugadores_plano_19_25 = 0

#Punto 2
nombre_menor_50pts = ""
categoria_menor_50pts = ""
edad_menor_50pts = 61
menor_50pts = False

#Punto 3
cant_experto = 0
porc_experto = 0

#Punto 4
cant_avanzado = 0
total_edades_avanzado = 0

#Punto 5
cant_plano = 0
cant_liftado = 0
cant_cortado = 0
mayor_saque = 0


while opcion == "s":
    nombre = input("Ingrese el nombre del jugador: ")
    
    edad = int(input("Ingrese la edad del jugador (13-60): "))
    while not(edad >= 13 and edad <= 60):
        print("Ingrese una edad válida: ")
        edad = int(input("Ingrese la edad del jugador (13-60): "))   
    
    puntos = int(input("Ingrese la cantidad de puntos (0-60): "))
    while not(puntos >= 0 and puntos <= 60):
        print("Ingrese una cantidad de puntos válida: ")
        puntos = int(input("Ingrese una cantidad de puntos (0-60): "))
    
    partidos_ganados = int(input("Ingrese los partidos ganados (0-35): "))
    while not(partidos_ganados >= 0 and partidos_ganados <= 35):
        print("Ingrese una cantidad de partidos ganados válida")
        partidos_ganados = int(input("Ingrese los partidos ganados (0-35): "))
    
    tipo_saque = input("Ingrese el tipo de saque (Plano - Liftado - Cortado): ").lower()
    while not(tipo_saque == "plano" or tipo_saque == "liftado" or tipo_saque == "cortado"):
        print("Ingrese un tipo de saque válido: ")
        tipo_saque = input("Ingrese el tipo de saque (Plano - Liftado - Cortado): ").lower()
        
    categoria = input("Ingrese la categoría (Elite - Experto - Avanzado): ").lower()
    while not(categoria == "elite" or categoria == "experto" or categoria == "avanzado"):
        print("Ingrese una categoría válida: ")
        categoria = input("Ingrese la categoría (Elite - Experto - Avanzado): ").lower()
    
    if categoria == "elite" and tipo_saque == "plano" and (edad >= 19 and edad <= 25): #Parentesis para edad no necesario, pero mas legible (personalmente)
        cantidad_jugadores_plano_19_25 += 1
        
    if edad < edad_menor_50pts and puntos > 50:
        nombre_menor_50pts = nombre
        categoria_menor_50pts = categoria
        edad_menor_50pts = edad
        menor_50pts = True
        
    if categoria == "experto":
        cant_experto += 1
    elif categoria == "avanzado":
        cant_avanzado += 1
        total_edades_avanzado += edad
    elif categoria == "elite":
        match tipo_saque:
            case "cortado":
                cant_cortado += 1
            case "liftado":
                cant_liftado += 1
            case "plano":
                cant_plano += 1    
    
    
    cant_jugadores += 1
    opcion = input("¿Desea ingresar otro jugador? (s/n): ")

if cantidad_jugadores_plano_19_25 > 0:
    print(f"La cantidad de jugadores élite con saque plano entre 19 y 25 es: {cantidad_jugadores_plano_19_25}")
else:
    print("No hay jugadores élite con saque plano entre 19 y 25")

if menor_50pts:
    print("El jugador con menor edad y mas de 50 puntos es: {nombre_menor_50pts} con {edad_menor_50pts} años")
else:
    print("Nadie hizo mas de 50 puntos")

if cant_experto > 0:
    porc_experto = (cant_experto * 100) / cant_jugadores
    print(f"El porcentaje de jugadores expertos es: {porc_experto}%")
else:
    print("No hay expertos")

if cant_avanzado > 0:
    promedio_avanzado = total_edades_avanzado / cant_avanzado
    print(f"El promedio de edad de jugadores avanzados es: {promedio_avanzado}")
else:
    print("Error")


mayor_saque = cant_cortado #5
saque_mas_usado = "Cortado"

if cant_plano > cant_cortado: #3 > 5
    mayor_saque = cant_plano
    saque_mas_usado = "Plano"

if cant_liftado > mayor_saque: #9 > 5
    mayor_saque = cant_liftado
    saque_mas_usado = "Liftado"

print(f"El saque mas usado es {saque_mas_usado}")
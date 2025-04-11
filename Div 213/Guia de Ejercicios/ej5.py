PRECIOBASE = 15000

localidad = input("Ingrese una localidad (Bariloche/Cataratas/Mar del Plata/Córdoba): ").lower()
aumento = 0
descuento = 0
match localidad:
        case "bariloche" | "cataratas" | "cordoba" | "mar del plata":
            estacion = input("Ingrese una estación (Invierno/Verano/Otoño/Primavera): ").lower()
            match estacion:
                case "invierno":
                    if localidad == "bariloche":
                        aumento = 1.20
                    elif localidad == "cataratas" or localidad == "cordoba":
                        descuento = 0.90
                    elif localidad == "mar del plata":
                        descuento = 0.80
                case "verano":
                    if localidad == "bariloche":
                        descuento = 0.80
                    elif localidad == "cataratas" or localidad == "cordoba":
                        aumento = 1.10
                    elif localidad == "mar del plata":
                        aumento = 1.20
                case "otoño" | "primavera":
                    if localidad == "bariloche" or localidad == "cataratas" or localidad == "mar del plata":
                        aumento = 1.10
                    elif localidad == "cordoba":
                        descuento = 1
                case _:
                    print("Ingrese una estación válida")
        case _:
            print("Ingrese una localidad válida")                
total = (PRECIOBASE * aumento) + (PRECIOBASE * descuento)
print(f"El precio total es: {total}")

# Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 
# por cada estadía como base, se pide el ingreso de una estación del 
# año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del 
# Plata/Córdoba) para vacacionar para poder calcular el precio final: 
    
# Invierno: 
#       Bariloche tiene un aumento del 20%
#       Cataratas y Córdoba tiene un descuento del 10% 
#       Mar del Plata tiene un descuento del 20% 
# Verano: 
#     Bariloche tiene un descuento del 20% 
#     Cataratas y Córdoba tiene un aumento del 10% 
#     Mar del Plata tiene un aumento del 20% 
# -Otoño y Primavera: 
#     Bariloche tiene un aumento del 10% 
#     Cataratas tiene un aumento del 10% 
#     Mar del Plata tiene un aumento del 10% y Córdoba tiene el precio sin descuento.
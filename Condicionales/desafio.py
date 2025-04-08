import math

CARGOFIJO = 7000
COSTOM3 = 200
IVA = 1.21
bonificacion = 0
recargo = 0

tipoCliente = input("Ingrese el tipo de cliente: ").lower()
consumo = int(input("Ingrese el consumo en m³: "))

subtotalBase = (consumo * COSTOM3)  
# print(subtotalBase)

match tipoCliente:
    case "residencial":
        if consumo < 30:
            bonificacion = 0.90
        elif consumo > 80:
            recargo = 1.15
            
        if subtotalBase < 35000: #Descuento adicional, al subtotalbase o subtotal final?
            subtotalBase * 0.95
    
    case "comercial":
        if consumo < 50:
            recargo = 1.05
        elif 150 < consumo <= 300:
            bonificacion = 0.92
        elif consumo > 300:
            bonificacion = 0.88
        
    case "industrial":
        if consumo < 200:
            recargo = 1.10
        elif 500 < consumo <= 1000:
            bonificacion = 0.80
        elif consumo > 1000:
            bonificacion = 0.70
    case _:
        print("Ingrese un tipo de cliente válido")  


if bonificacion!=0 or recargo!=0:
    subtotal = (subtotalBase * bonificacion) + (subtotalBase * recargo)
else:
    subtotal = subtotalBase





print(f"Pre modificaciones: {subtotalBase}")
if bonificacion != 0:
    print(f"Bonificaciones: {int(100 - (bonificacion * 100))}%")
else:
    print("Bonificaciones: 0%")

if recargo != 0:
    print(f"Recargos: {math.ceil((recargo * 100) - 100)}%")
else:
    print("Recargos: 0%")    
print(f"Post modificaciones: {subtotal}")
print(f"Cargo fijo: {CARGOFIJO}")
print(f"IVA: {int((IVA * 100) - 100)}%")


total = (subtotal + 7000) * IVA

print(f"Total: {total}")


# print(subtotal)

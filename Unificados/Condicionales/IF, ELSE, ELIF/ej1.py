altura = int(input("Ingrese su altura en cm: "))

if altura < 160:
    print("Base")
elif altura < 180:
    print("Escolta")
elif altura < 200:
    print("Alero")
else:
    print("Pivot")
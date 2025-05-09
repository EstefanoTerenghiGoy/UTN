def area_circulo(radio:int)->int:
    area = 3.14 * radio ** 2
    return area

radio = int(input("Ingrese el radio del circulo: "))
print(area_circulo(radio))
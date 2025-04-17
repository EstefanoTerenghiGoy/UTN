def area_rectanculo(base:int,altura:int)->int:
    area = base * altura
    return area

base = int(input("Ingrese el area del rectángulo: "))
altura = int(input("Ingrese la altura del rectángulo: "))
print(f"El area es: {area_rectanculo(base, altura)}")
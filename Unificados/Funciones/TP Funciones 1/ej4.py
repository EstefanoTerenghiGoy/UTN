def rango_num(min:int, max:int):
    numero = int(input("Ingrese un número: "))
    if numero >= max or numero <= min:
        print(f"El número {numero} no se encuentra dentro del rango.")
    else:
        print(f"El número {numero} se encuentra dentro del rango.")

min_range = int(input("Determine el mínimo del rango: "))
max_range = int(input("Determine el máximo del rango: "))
rango_num(min_range, max_range)
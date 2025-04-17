def es_par_bool(num1:int)->bool:
    return numero % 2 == 0

numero = int(input("Ingrese un número: "))

if es_par_bool(numero):
    print("Es par")
else:
    print("Es impar")
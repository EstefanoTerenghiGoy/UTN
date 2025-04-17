# 8. Crear una función que (utilizando la función del punto 11 de la guía de For),
# muestre todos los números primos comprendidos entre entre la unidad y un número
# ingresado como parámetro. La función retorna la cantidad de números primos
# encontrados.'''

def numeros_primos(num)->int:
    flag = True
    contador = 0
    for i in range(2,num):
        for n in range(2, i):
            if i % n == 0:
                flag = False
                break
        else:
            flag = True
            contador +=1
        if flag:
            print(i)
    return contador

numero_limite = int(input("Ingrese hasta qué numero quiere saber los primos del 1 hasta sí mismo: "))

print(f"Se encontraron {numeros_primos(numero_limite)} números primos")
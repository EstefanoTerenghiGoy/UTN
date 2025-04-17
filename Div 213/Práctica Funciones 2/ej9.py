#9. Crear una función que imprima la tabla de multiplicar de un número recibido como
#parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir
#el rango de multiplicación. Por defecto es del 1 al 10.

def calcularTabla(numero: int, inicio: int = 1, final: int = 10):
    contador = inicio
    while contador <= final:
        print(f"{numero} x {contador} = {numero * contador}")
        contador+=1


numero = int(input("Ingrese el número a multiplicar: "))

calcularTabla(numero, 2, 5)
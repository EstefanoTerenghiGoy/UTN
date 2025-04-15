'''# 1. Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna
# el área.

def area_rectanculo(base:int,altura:int)->int:
    area = base * altura
    return area

# 2. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro
# y devolver el área.

def area_circulo(radio:int)->int:
    area = 3.14 * radio ** 2
    return area

# 3. Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje
# indicando si el número es par o impar.

def es_par():
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

# 4. Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es
# par, False en caso contrario.

def es_par2()->bool:
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        return True
    else:
        return False
    
# 5. Define una función que encuentre el máximo de tres números. La función debe
# aceptar tres argumentos y devolver el número más grande.

def numero_mas_grande(num1:int,num2:int,num3:int)->int:
    maximo = num1
    if num2 > maximo:
        maximo = num2
    if num3 > maximo:
        maximo = num3
    return maximo

# 6. Diseña una función que calcule la potencia de un número. La función debe recibir la
# base y el exponente como argumentos y devolver el resultado.

def potencia_de_un_numero(base:int,exponente:int)->int:
    resultado = base ** exponente
    return resultado

print(potencia_de_un_numero(10,2))

# 7. Crear una función que reciba un número y retorne True si el número es primo, False
# en caso contrario.

def es_primo(num:int)->bool:
    flag = True
    for i in range(2, num):
        if (num % i) == 0:
            flag = False
    return flag

num = 8
if es_primo(num):
    print("El número es primo.")
else:
    print("El número no es primo")

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

numeros_primos(30)

print(f"Se encontraron {contador} números primos.")
# 9. Crear una función que imprima la tabla de multiplicar de un número recibido como
# parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir
# el rango de multiplicación. Por defecto es del 1 al 10.
# 10. Crear una función que le solicite al usuario el ingreso de un número entero y lo
# retorne.
# 11. Crear una función que le solicite al usuario el ingreso de un número flotante y lo
# retorne.
# 12. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.
# 13. Especializar las funciones del punto 10, 11, 12 para hacerlas reutilizables. Agregar
# validaciones.
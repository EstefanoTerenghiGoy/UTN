#13. Especializar las funciones del punto 10, 11, 12 para hacerlas reutilizables. Agregar
#validaciones.

#Estaría mucho mas completo y mejor hecho con try, sin eso se escapan muchos casos inválidos

def devolver_entero(numeroEntero: int) -> int:
    while int(numeroEntero) != numeroEntero:
        print("Ingrese un número válido")
        numeroEntero = float(input("Ingrese un número entero: "))
    return int(numeroEntero)
numeroEntero = float(input("Ingrese un número entero: "))
print(devolver_entero(numeroEntero))


def devolver_flotante(numeroFloat: float) -> float:
    while int(numeroFloat) == numeroFloat:
        print("Ingrese un número con parte decimal (coma)")
        numeroFloat = float(input("Ingrese un número con coma: "))
    
    return numeroFloat
numeroFloat = float(input("Ingrese un número con coma: "))
print(devolver_flotante(numeroFloat))


def devolver_string(cadena: str) -> str:
    
    while cadena.strip() == "":
        print("No puede estar vacío.")
        cadena = input("Ingrese una cadena de texto: ")
    
    return cadena

cadena = input("Ingrese una cadena de texto: ")
print(devolver_string(cadena))
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    
    numero = int(input(mensaje))
    
    while not(minimo <= numero <= maximo) and reintentos > 0:
        numero = int(input(f"{mensaje_error}: "))
        reintentos -= 1
    if reintentos == 0:
        mensaje_error = "Sin intentos restantes"
        print(mensaje_error)
        numero = None
    return numero
        

minimo = 1
maximo = 5
reintentos = 3
mensaje = f"Ingrese un número entre {minimo} y {maximo}"
mensaje_error = "ERROR: Ingrese un número dentro del rango"

print(get_int(mensaje, mensaje_error, minimo, maximo, reintentos))




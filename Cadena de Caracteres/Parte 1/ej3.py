def char_at(cadena, numero):
    return cadena[numero]

cadena = input("Ingrese una palabra: ")
numero = int(input("Ingrese el indice que quiere saber (Desde 1 hasta el largo de la palabra): "))-1
while numero < 0 or numero >= len(cadena):
    numero = int(input("Ingrese un valor dentro del rango: "))-1

print(char_at(cadena, numero))
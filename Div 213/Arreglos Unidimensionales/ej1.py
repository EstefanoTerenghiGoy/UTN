'''Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los
guarde en una lista y la retorne. El programa principal debe invocar a la función y
mostrar por pantalla el retorno.'''

def pedir_y_mostrar_nombres()->list:
    nombres = []
    for i in range(10):
        nombres.append(input("Ingrese un nombre: "))
    return nombres

nombres = pedir_y_mostrar_nombres()
for nombre in nombres:
    print(pedir_y_mostrar_nombres())
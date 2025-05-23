from biblioteca import *

productos = ["A", "B", "C"]
ventas = [
    #T1 #T2 #T3
    [50, 60, 70], #A
    [80, 55, 90], #B
    [40, 65, 90]  #C
]
seguir = "s"
while seguir == "s": #Bucle que el usuario puede cortar cuando quiera
    print("""
    Elija una opción: 
    1 - Mostrar la lista de productos y las ventas
    2 - Ordenar los productos de mayor a menor según sus ventas totales anuales
    3 - Buscar un producto por nombre y mostrar sus ventas
    4 - Buscar un valor de venta dentro de la matriz y mostrar a qué producto y trimestre pertenece
    5 - Salir
    """)
    opcion = 0
    while opcion == 0: #Bucle de opciones
        opcion = obtener_numero("Ingrese una opción (1-5): ")
        
        match int(opcion): #Transforma el string de opcion en número
            case 1:
                mostrar_productos_y_ventas(productos, ventas)
            case 2:
                mostrar_productos_ordenados(ordenar_productos_segun_venta_anual(ventas))
            case 3:
                producto = input("Ingrese el producto que desea buscar: ").upper()
                if comprobar_existencia_de_producto(productos, producto):
                    mostrar_producto_por_nombre(buscar_producto_por_nombre(productos, ventas, producto))
                else:
                    print("El producto no existe")                
                    opcion = 0
            case 4:
                venta = obtener_numero("Ingrese la venta por la que desea filtrar: ")
                if comprobar_existencia_de_venta(ventas, venta):
                    mostrar_producto_y_trimestre(buscar_producto_y_trimestre_por_venta(productos, ventas, venta))
                else:
                    print("No hay ningun producto con esa cantidad de ventas")
                    opcion = 0
            case 5:
                seguir = "n"
                break
            case _:
                print("Opción inválida")

    if opcion != 5:
        seguir = input("\n¿Desea realizar otra operación? (s/n): ").lower()
        while seguir != "s" and seguir != "n":
            seguir = input("Ingrese una opción válida: ")
print("Saliendo del programa...")

# mostrar_matriz_formateada(productos, ventas)
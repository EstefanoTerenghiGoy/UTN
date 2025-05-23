from utils.manipular_matrices import *
from biblioteca import *

productos = [
    ["Vacío",["botellas",3], "Vacío",["frascos", 8], "Vacío"], 
    ["Vacío","Vacío",["fideos", 4], "Vacío","Vacío"], 
    ["Vacío","Vacío","Vacío",["leche", 6],"Vacío"]  
]

opcion = 0
alta_producto_flag = False

while opcion == 0:
    print("\nEliga una opción: \n1-Alta de productos\n2-Baja de productos\n3-Modificar productos\n4-Listar productos\n5-Lista de productos ordenado por nombre\n6-Salir\n")
    opcion = int(input("Elija una opción: "))
    
    match opcion:
        
        case 1:
            producto_nuevo = input("Ingrese el producto que desea agregar: ")
            if comprobar_existencia_de_producto(productos, producto_nuevo):
                print("El producto ya existe")
            else:
                cantidad = int(input("Ingrese la cantidad del producto: "))
                if alta_producto(productos, producto_nuevo, cantidad):
                    print("Producto agregado")
                    mostrar_matriz_triple(productos)
                else:
                    print("Ya hay un producto en esta posicion")
                alta_producto_flag = True
                opcion = 0
        case 2 | 3:
            if not alta_producto_flag:
                print("Debe dar de alta un producto primero")
                opcion = 0
            else:
                match opcion:
                    case 2:
                        if baja_producto(productos):
                            print("Producto dado de baja correctamente")
                            mostrar_matriz_triple(productos)
                        else:
                            print("No hay ningun producto en esta posición")
                    case 3:
                        opcion_modificacion = input("\n¿Qué deséa modificar?\n1-Cantidad\n2-Ubicación\n3-Ambas\n").lower()
                        match opcion_modificacion:
                            case "1" | "cantidad":
                                cantidad = int(input("Ingrese la nueva cantidad: "))
                                while cantidad < 1:
                                    cantidad = int(input("Ingrese una cantidad válida: "))
                                mensaje = modificar_producto(productos, cantidad)
                            case "2" | "ubicacion" | "ubicación":
                                mensaje = modificar_producto(productos, cambiar_ubicacion=True)
                            case "3" | "ambas":
                                cantidad = int(input("Ingrese la nueva cantidad: "))
                                while cantidad < 1:
                                    cantidad = int(input("Ingrese una cantidad válida: "))
                                mensaje = modificar_producto(productos, cantidad, True)
                            case _:
                                print("Opción no válida.")
                                mensaje = None

                        if mensaje is not None:
                            print("\n" + mensaje)
                            if mensaje == "Producto modificado correctamente.":
                                mostrar_matriz_triple(productos)

        case 4:
            productos_listados = listar_producto(productos) 
            for producto in productos_listados:
                print(producto)
        case 5:
            productos_listados_por_nombre = listar_productos_por_nombre(productos)
            for producto in productos_listados_por_nombre:
                print(producto)
        case 6:
            print("Saliendo del programa")
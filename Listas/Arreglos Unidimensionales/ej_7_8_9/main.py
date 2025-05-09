from biblioteca import *
from listas_personas import *

def menu():
    opcion = 0
    print("\nEliga una opción: \n1-Importar listas\n2-Listar usuarios de México\n3-Listar usuarios de Brasil\n4-Listar usuario/s más joven/es\n5-Promedio de edad\n6-Usuario más grande de Brasil\n7-Usuarios de México y Brasil con CP > 8000\n8-Italianos mayores de 40 años\n")
    listas_importadas = False
    
    while opcion == 0:
        opcion = int(input("Elija una opción: "))
        match opcion:
            case 1:
                print("Listas importadas correctamente")
                listas_importadas = True
                opcion = 0
            case 2 | 3 | 4 | 5 | 6 | 7 | 8:
                if not listas_importadas:
                    print("Debe importar las listas primero")
                    opcion = 0
                else:
                    match opcion:
                        case 2:
                            for usuario in listar_usuarios_mexico():
                                print(usuario)
                        case 3:
                            for usuario in listar_usuarios_brasil():
                                print(usuario)
                        case 4:
                            for usuario in buscar_menores_de_edad():
                                print(usuario)
                        case 5:
                            print(f"El promedio de edades es: {promediar_edades()}")
                        case 6:
                            print(f"El usuario de Brasil con mayor edad es: {listar_usuarios_brasil_mayores()}")
                        case 7:
                            for usuario in usuarios_mexico_brasil_cp_8000():
                                print(usuario)
                        case 8:
                            for usuario in listar_datos_italianos_40():
                                print(usuario)
            case _:
                print("Elija una opción válida")
                opcion = 0

menu()
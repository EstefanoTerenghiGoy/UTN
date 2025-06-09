from biblioteca import *
from estudiantes import *


mostrar_menu()
opcion = int(input("Ingrese una opción: "))
match opcion:
    case 1:
        mostrar_estudiantes(ordenar_por_apellido(estudiantes), ["legajo", "nombre", "apellido", "edad"])
    case 2:
        mostrar_estudiantes(listar_promedio_estudiantes(estudiantes))
    case 3:
        mostrar_estudiantes(listar_estudiantes_informatica(estudiantes))
    case 4:
        print("El promedio de edades de los estudiantes es:", calcular_promedio_edades(estudiantes))
    case 5:
        mostrar_estudiantes(calcular_mayor_promedio_nota(estudiantes))
    case 6:
        mostrar_estudiantes(listar_estudiantes_club_informatica(estudiantes))
    case 7:
        mostrar_estudiantes(listar_alumnos_mas_jovenes(estudiantes))
    case 8:
        print("Saliendo del programa...")
    case _:
        print("Opción no válida. Por favor, intente de nuevo.")
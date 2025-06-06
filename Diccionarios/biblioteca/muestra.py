def mostrar_menu():
    print("""
    Elija una opción: 
    1 - Ordenar los estudiantes por apellido y nombre
    2 - Calcular el promedio de notas de cada estudiante
    3 - Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de “Ingenieria en Informatica”
    4 - Obtener un promedio de edad de los estudiantes.
    5 - Informar el alumno con mayor pomedio de notas. Mostrar nombre y apellido
    6 - Listar nombre y apellido de los alumnos que forman el grupo “Club de Informática” con sus respectivos promedios
    7 - Listar legajo, nombre,
    8 - Salir
    """)
def mostrar_estudiantes(estudiantes: list, campos = None):
    """
    Muestra los estudiantes en un formato legible.
    Si se le da el argumento campos, solo mostrará esos campos específicos, util cuando en vez de
    darse una lista especifica, se pasa la lista completa de estudiantes.
    """
    for estudiante in estudiantes:
        if campos is None:
            for key in estudiante:
                print(f"{key}: {estudiante[key]}")
        else:
            for campo in campos:
                print(f"{campo}: {estudiante[campo]}")
        print()



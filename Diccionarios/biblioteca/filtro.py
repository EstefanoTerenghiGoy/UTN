from .logica import calcular_menor_edad

def listar_promedio_estudiantes(estudiantes: list):
    """
    Calcula el promedio de notas de cada estudiante y devuelve una lista con los datos del mismo
    """
    datos_promedio = []
    for i in range(len(estudiantes)):
        promedio = 0
        suma_notas = 0
        for nota in estudiantes[i]["notas"]:
            suma_notas += nota
            promedio = suma_notas / len(estudiantes[i]["notas"])
        datos_promedio.append({
            "legajo": estudiantes[i]["legajo"],
            "nombre": estudiantes[i]["nombre"],
            "apellido": estudiantes[i]["apellido"],
            "promedio": round(promedio, 2),
        })
    
    return datos_promedio

def listar_estudiantes_informatica(estudiantes: list):
    """
    Filtra los estudiantes que cursan el programa de "Ingenieria en Informatica" y devuelve una lista con sus datos.
    """
    estudiantes_informatica = []
    for estudiante in estudiantes:
        if estudiante["programa"]["nombre"] == "Ingenieria en Informatica":
            estudiantes_informatica.append({
                    "legajo" : estudiante["legajo"],
                    "nombre" : estudiante["nombre"],
                    "apellido" : estudiante["apellido"],
                    "edad" : estudiante["edad"]
                })
    return estudiantes_informatica





def listar_estudiantes_club_informatica(estudiantes: list):
    """
    Lista los estudiantes que forman parte del "Club de Informática" junto con sus promedios de notas.
    """
    promedios = listar_promedio_estudiantes(estudiantes)
    estudiantes_club_informatica = []
    for i in range(len(estudiantes)):
        if "grupos" in estudiantes[i]:
            for grupo in estudiantes[i]["grupos"]:
                if grupo["nombre"] == "Club de Informatica":
                    estudiantes_club_informatica.append({
                        "nombre": estudiantes[i]["nombre"],
                        "apellido": estudiantes[i]["apellido"],
                        "promedio": promedios[i]["promedio"]
                    })
    return estudiantes_club_informatica



def listar_alumnos_mas_jovenes(estudiantes: list):
    """
    Lista los estudiantes más jóvenes y devuelve una lista con sus datos.
    Si hay más de un estudiante con la misma edad, los devuelve a todos.
    """
    menor_edad = calcular_menor_edad(estudiantes)
    alumnos_mas_jovenes = []
    for estudiante in estudiantes:
        if estudiante["edad"] == menor_edad:
            alumnos_mas_jovenes.append({
                "legajo": estudiante["legajo"],
                "nombre": estudiante["nombre"],
                "apellido": estudiante["apellido"],
                "edad": estudiante["edad"],
                "programa" : estudiante["programa"]["nombre"]
            })
    return alumnos_mas_jovenes
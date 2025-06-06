def calcular_promedio_edades(estudiantes: list):
    """
    Calcula el promedio de edades de los estudiantes y lo devuelve.
    """
    promedio_ededades = 0
    for estudiante in estudiantes:
        promedio_ededades += estudiante["edad"]
    return promedio_ededades / len(estudiantes)


def calcular_mayor_promedio_nota(estudiantes: list):
    """
    Calcula el estudiante con el mayor promedio de notas y devuelve una lista con sus datos.
    Si hay más de un estudiante con el mismo promedio, los devuelve a todos.
    """
    mayor_promedio = 0
    datos_mayor_promedio = []
    for estudiante in estudiantes:
        promedio = 0
        for nota in estudiante["notas"]:
            promedio += nota
        promedio /= len(estudiante["notas"])
        if promedio > mayor_promedio:
            mayor_promedio = promedio
            datos_mayor_promedio.clear()
            datos_mayor_promedio.append({
                "nombre": estudiante["nombre"],
                "apellido": estudiante["apellido"],
                "promedio": round(promedio, 2)
            })
        elif promedio == mayor_promedio:
            datos_mayor_promedio.append({
                "nombre": estudiante["nombre"],
                "apellido": estudiante["apellido"],
                "promedio": round(promedio, 2)
            })
    return datos_mayor_promedio



def calcular_menor_edad(estudiantes: list):
    """
    Calcula la edad mínima entre los estudiantes y devuelve el valor.
    """
    menor_edad = estudiantes[0]["edad"]
    for estudiante in estudiantes:
        if estudiante["edad"] < menor_edad:
            menor_edad = estudiante["edad"]
    return menor_edad


def ordenar_por_apellido(estudiantes: list):
    """
    Crea una copia de la lista de estudiantes, la ordena por apellido y nombre y la devuelve.
    """
    copia_estudiantes = estudiantes.copy()
    for i in range(len(copia_estudiantes) - 1):
        for j in range(i+1, len(copia_estudiantes)):
            if copia_estudiantes[i]["apellido"] > copia_estudiantes[j]["apellido"]:
                aux = copia_estudiantes[i]
                copia_estudiantes[i] = copia_estudiantes[j]
                copia_estudiantes[j] = aux
            elif copia_estudiantes[i]["apellido"] == copia_estudiantes[j]["apellido"] and copia_estudiantes[i]["nombre"] > copia_estudiantes[j]["nombre"]:
                aux = copia_estudiantes[i]
                copia_estudiantes[i] = copia_estudiantes[j]
                copia_estudiantes[j] = aux
    return copia_estudiantes
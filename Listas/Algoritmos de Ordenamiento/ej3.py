def swap(estudiantes: list, apellidos: list, nota: list, i: int, j: int):
    auxApellidos = apellidos[i]
    apellidos[i] = apellidos[j]
    apellidos[j] = auxApellidos
    
    auxEstudiantes = estudiantes[i]
    estudiantes[i] = estudiantes[j]
    estudiantes[j] = auxEstudiantes
    
    auxNota = nota[i]
    nota[i] = nota[j]
    nota[j] = auxNota

def ordenar_por_nombre(estudiantes: list, apellidos: list, nota: list):
    for i in range(len(estudiantes) - 1):
        for j in range(i + 1, len(estudiantes)):
            if apellidos[j] < apellidos[i]:
                swap(estudiantes, apellidos, nota, i, j)
            elif apellidos[j] == apellidos[i]:
                if estudiantes[j] < estudiantes[i]:
                    swap(estudiantes, apellidos, nota, i, j)
                elif estudiantes[j] == estudiantes[i]:
                    if nota[j] > nota[i]:
                        swap(estudiantes, apellidos, nota, i, j)


Estudiantes =["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

ordenar_por_nombre(Estudiantes, Apellidos, Nota)

for i in range(len(Estudiantes)):
    print(f"{Estudiantes[i]} {Apellidos[i]}: {Nota[i]}")
    
    
    
    
    
    
    
    
    
    
    
    

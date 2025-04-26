def buscar_menores_de_edad(nombres: list, edades: list) -> list:
    menor_edad = 200
    edades_y_nombre = []
    for i in range(len(edades)):
        if edades[i] < menor_edad:
            menor_edad = edades[i]
    for i in range(len(nombres)):
        if edades[i] == menor_edad:
            edades_y_nombre += [nombres[i]]
    edades_y_nombre += [menor_edad]
    return edades_y_nombre

nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 

for persona in buscar_menores_de_edad(nombres, edades):
    print(persona)

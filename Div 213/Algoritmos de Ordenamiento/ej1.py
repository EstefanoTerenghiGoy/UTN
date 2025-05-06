# def ordenar_por_edad(nombres: list, edades: list) -> list:
#     auxEdad = 0
#     auxNombre = ""
#     for i in range(len(edades) - 1):
#         for j in range(i+1, len(edades)):
#             if edades[j] < edades[i]:
#                 auxEdad = edades[i]
#                 edades[i] = edades[j]
#                 edades[j] = auxEdad
                
#                 auxNombre = nombres[i]
#                 nombres[i] = nombres[j]
#                 nombres[j] = auxNombre


# Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
# Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

# ordenar_por_edad(Nombres, Edades)

# for i in range(len(Nombres)):
#     print(f"{Nombres[i]}: {Edades[i]}")

def ordenar_por_nombre(nombres: list, edades: list):
    auxEdad = 0
    auxNombre = ""
    for i in range(len(edades) - 1):
        for j in range(i+1, len(edades)):
            if nombres[j] < nombres[i]:
                auxNombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = auxNombre
                
                auxEdad = edades[i]
                edades[i] = edades[j]
                edades[j] = auxEdad

Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

ordenar_por_nombre(Nombres, Edades)

for i in range(len(Nombres)):
    print(f"{Nombres[i]}: {Edades[i]}")
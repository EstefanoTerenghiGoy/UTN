# def ordenar_nombres(nombres: list, puntos: list):
#     auxPuntos = 0
#     auxNombre = 0
#     for i in range(len(puntos) - 1):
#         for j in range(i+1, len(puntos)):
#             if puntos[j] < puntos[i]:
#                 auxPuntos = puntos[i]
#                 puntos[i] = puntos[j]
#                 puntos[j] = auxPuntos
                
#                 auxNombre = nombres[i]
#                 nombres[i] = nombres[j]
#                 nombres[j] = auxNombre

# Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza", "Fisica"]
# Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

# # print(Nombres, Puntos)
# ordenar_nombres(Nombres, Puntos)
# for i in range(len(Puntos)):
#     print(f"{Nombres[i]}: {Puntos[i]}")





def ordenar_por_nombre(nombres: list, puntos: list):
    auxPuntos = 0
    auxNombre = ""
    for i in range(len(puntos) - 1):
        for j in range(i+1, len(puntos)):
            if nombres[j] < nombres[i]:
                auxNombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = auxNombre
                
                auxPuntos = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = auxPuntos
            elif nombres[j] == nombres[i] and puntos[j] > puntos[i]:
                    auxPuntos = puntos[i]
                    puntos[i] = puntos[j]
                    puntos[j] = auxPuntos
                    #Bastante repetitivo, mejor incluir una funcion auxiliar para el swap como en el ej3
    
    
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza", "Fisica"]
Puntos = [100,98,64,25,87,38,56,42,28,91,66,35,49,57,98]

ordenar_por_nombre(Nombres, Puntos)

for i in range(len(Nombres)):
    print(f"{Nombres[i]}: {Puntos[i]}")
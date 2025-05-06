from listas_personas import *

def listar_usuarios_mexico() -> list:
    datos_usuarios_mexico = []
    for i in range(len(country)):
        if country[i] == "Mexico":
            datos_usuarios_mexico += [[nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], edades[i]]]
    return datos_usuarios_mexico

def listar_usuarios_brasil() -> list:
    datos_usuarios_brasil = []
    for i in range(len(country)):
        if country[i] == "Brazil":
            datos_usuarios_brasil += [[nombres[i], telefonos[i], mails[i]]]
    return datos_usuarios_brasil

def buscar_menores_de_edad() -> list:
    
    menor_edad = 200
    datos_menor = []
    for i in range(len(edades)):
        if edades[i] < menor_edad:
            menor_edad = edades[i]
    for i in range(len(nombres)):
        if edades[i] == menor_edad:
            datos_menor += [[nombres[i], telefonos[i], mails[i], address[i], postalZip[i], country[i], region[i], menor_edad]]
    return datos_menor

def promediar_edades() -> int:
    total_edades = 0
    for i in range(len(edades)):
        total_edades += edades[i]
    return total_edades / len(edades)

def listar_usuarios_brasil_mayores() -> list:
    datos_usuario_brasil_mayor = []
    mayor_edad = 0
    for i in range(len(country)):
        if country[i] == "Brazil":
            if edades[i] > mayor_edad:
                mayor_edad = edades[i]
                datos_usuario_brasil_mayor += [edades[i],nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], edades[i]]
    return datos_usuario_brasil_mayor

def usuarios_mexico_brasil_cp_8000() -> list:
    datos_usuario_mexico_brasil = []
    for i in range(len(country)):
        if country[i] == "Brazil" or country[i] == "Mexico":
            if postalZip[i] > 8000:
                datos_usuario_mexico_brasil += [[nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i],edades[i]]]
    return datos_usuario_mexico_brasil

def listar_datos_italianos_40() -> list:
    
    usuarios_italianos_mayores_40 = []
    for i in range(len(country)):
        if country[i] == "Italy":
            if edades[i] > 40:
                usuarios_italianos_mayores_40 += [[nombres[i], mails[i], telefonos[i]]]
    return usuarios_italianos_mayores_40

def listar_usuarios_mexico_por_nombre() -> list:
    datos_usuarios_mexico = listar_usuarios_mexico()
    
    for i in range(len(datos_usuarios_mexico) - 1):
        for j in range(i+1, len(datos_usuarios_mexico)):
            nombre_i = datos_usuarios_mexico[i][0]
            nombre_j = datos_usuarios_mexico[j][0]
            if nombre_j < nombre_i:
                swap_multiple(datos_usuarios_mexico, i, j)
    return datos_usuarios_mexico

def usuario_de_menor_edad_ordenados() -> list:
    usuarios_menor_edad = buscar_menores_de_edad()
    
    for i in range(len(usuarios_menor_edad) - 1):
        for j in range(i+1, len(usuarios_menor_edad)):
            nombre_i = usuarios_menor_edad[i][0]
            nombre_j = usuarios_menor_edad[j][0]
            if nombre_j < nombre_i:
                swap_multiple(usuarios_menor_edad, i, j)
    return usuarios_menor_edad

def usuarios_mexico_brasil_cp_8000_ordenados():
    datos_usuarios_mexico_brasil = usuarios_mexico_brasil_cp_8000()
    for i in range(len(datos_usuarios_mexico_brasil)-1):
        for j in range(i+1, len(datos_usuarios_mexico_brasil)):
            nombre_i = datos_usuarios_mexico_brasil[i][0]
            nombre_j = datos_usuarios_mexico_brasil[j][0]
            edad_i = datos_usuarios_mexico_brasil[i][7]  
            edad_j = datos_usuarios_mexico_brasil[j][7]
            
            if nombre_j < nombre_i or (nombre_j == nombre_i and edad_j > edad_i):
                swap_multiple(datos_usuarios_mexico_brasil, i, j)
    return datos_usuarios_mexico_brasil

def swap_multiple(datos_a_intercambiar: list, i:int, j:int):
        aux = datos_a_intercambiar[i]
        datos_a_intercambiar[i] = datos_a_intercambiar[j]
        datos_a_intercambiar[j] = aux 
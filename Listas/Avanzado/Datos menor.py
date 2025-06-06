jugadores = [
    {"nombre": "Ana", "edad": 43, "puntos":[10,12,14]},  
    {"nombre": "Juan", "edad": 32, "puntos":[12,10,11]},  
    {"nombre": "Pedro", "edad": 28, "puntos":[9,15,11]},
    {"nombre": "Sol", "edad": 31, "puntos":[11,8,15]}
]

menor_edad = jugadores[0]["edad"]
datos_menor = []

for e_jugador in jugadores:
    if e_jugador["edad"] < menor_edad:
        menor_edad = e_jugador["edad"]
        datos_menor = [e_jugador["nombre"], menor_edad]

print(f"La persona de menor edad es {datos_menor[0]} con {datos_menor[1]} años")
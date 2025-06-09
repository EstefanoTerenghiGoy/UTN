from utils import *

estudiantes = [
    {"nombre": "Sofía", "curso": "Matemáticas", "calificacion": 7.5},
    {"nombre": "Tomás", "curso": "Historia", "calificacion": 5.5},
    {"nombre": "Valentina", "curso": "Ciencias", "calificacion": 9.0},
    {"nombre": "Lucas", "curso": "Literatura", "calificacion": 4.0},
    {"nombre": "Martina", "curso": "Física", "calificacion": 6.8}
]

procesar = procesar_lista
lista_filtrada = (procesar(estudiantes, filtrar_lista, "calificacion", 6.0, "mayor"))
for e in lista_filtrada:
    print(f"Nombre: {e['nombre']} - Curso: ${e['curso']} - Calificación: {e['calificacion']}")

print("\nEl promedio de calificaciones es: ", procesar(estudiantes, calcular_promedio, "calificacion"))
"""
Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.

Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla.


"""


apellido = input("Ingrese su apellido: ")
while apellido == "":
    apellido = input("Apellido inválido. Ingrese su apellido: ")

# Ingreso y validación de la edad (18 a 90 inclusive)
edad = int(input("Ingrese su edad (entre 18 y 90): "))
while not  18 <= edad <= 90:
    edad = int(input("Edad inválida. Ingrese una edad válida (entre 18 y 90): "))


# Ingreso y validación del estado civil
estado_civil = input("Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a): ").lower()
while not(estado_civil == "Soltero/a" or estado_civil == "casado/a" or estado_civil == "divorciado/a" or estado_civil == "viudo/a"):
    estado_civil = input("Ingrese un estado civil válido (Soltero/a, Casado/a, Divorciado/a, Viudo/a): ").lower()

# Ingreso y validación del número de legajo (4 cifras, sin ceros a la izquierda)
legajo = input("Ingrese su número de legajo (4 cifras, sin ceros a la izquierda): ")
while not (legajo.isdigit() and len(legajo) == 4 and not legajo.startswith("0")):
    legajo = input("Legajo inválido. Ingrese un número de legajo válido (4 cifras, sin ceros a la izquierda): ")
legajo = int(legajo)

# Mostrar datos ingresados
print("\nDatos ingresados:")
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado civil: {estado_civil}")
print(f"Número de legajo: {legajo}")

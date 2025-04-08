import random

notaAleatoria = random.randint(1, 10)

if notaAleatoria < 4:
    print(f"Desaprobado, la nota es {notaAleatoria}")
elif notaAleatoria < 6:
    print(f"Aprobado, la nota es {notaAleatoria}")
else:
    print(f"Promoción directa, la nota es {notaAleatoria}")

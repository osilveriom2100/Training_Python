# Comprension de listas
# Es una forma de crear listas a partir de otras listas o iterables, utilizando una sintaxis más concisa y legible.
# Sintaxis básica:
# [expresion for item in iterable if condicion]
# Ejemplo 1: Crear una lista de cuadrados de números del 0 al 9
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# sin comprension de listas
cuadrados2 = []
for x in range(10):
    cuadrados2.append(x**2)
print(cuadrados2)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Ejemplo 2: Crear una lista de números pares del 0 al 9
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Output: [0, 2, 4, 6, 8]
# sin comprension de listas
pares2 = []
for x in range(10):
    if x % 2 == 0:
        pares2.append(x)
print(pares2)  # Output: [0, 2, 4, 6, 8]


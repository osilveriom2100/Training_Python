# Asignacion multiple
# es una forma de asignar valores a varias variables en una sola linea de codigo
# se puede hacer de varias formas, como por ejemplo:
# Asignacion multiple con valores diferentes
a, b, c = 1, 2, 3
print(f"El valor de a es: {a}, el valor de b es: {b}, el valor de c es: {c}")
# Asignacion multiple con el mismo valor, o asignacion multiple encadenada
x = y = z = 0
print(f"El valor de x es: {x}, el valor de y es: {y}, el valor de z es: {z}")
# Asignacion multiple con expresiones
p, q, r = 2 + 3, 4 * 5, 6 ** 2
print(f"El valor de p es: {p}, el valor de q es: {q}, el valor de r es: {r}")
# Asignacion multiple con listas
lista = [10, 20, 30]
m, n, o = lista
print(f"El valor de m es: {m}, el valor de n es: {n}, el valor de o es: {o}")
# Asignacion multiple con tuplas
tupla = (100, 200, 300)
u, v, w = tupla
print(f"El valor de u es: {u}, el valor de v es: {v}, el valor de w es: {w}")
# Asignacion multiple con diccionarios
diccionario = {'a': 1, 'b': 2, 'c': 3}
a, b, c = diccionario.values()
print(f"El valor de a es: {a}, el valor de b es: {b}, el valor de c es: {c}")
# Asignacion multiple con variables ya definidas
x = 5
y = 10
z = 15
x, y, z = y, z, x
print(f"El valor de x es: {x}, el valor de y es: {y}, el valor de z es: {z}")
# Intercambio de valores con asignacion multiple, sin necesidad de una variable temporal
a, b = 1, 2
print(f"Antes del intercambio: a = {a}, b = {b}")
a, b = b, a
print(f"Despues del intercambio: a = {a}, b = {b}")

# Recibir valores de entrada del usuario con asignacion multiple
nombre, edad = input("Ingrese su nombre y edad separados por un espacio: ").split()
print(f"El nombre ingresado es: {nombre}, y la edad ingresada es: {edad}")
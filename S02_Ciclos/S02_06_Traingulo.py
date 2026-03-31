print("Triangulo simetrico: ")
filas = int(input("Cuantas filas tendra: "))

x = 1
for i in range(filas):
    print(" " * (filas - i), "*" * x)
    x +=2

for i in range(1, filas + 1):
    print(" " * (filas - i), "*" * (2 * i - 1))

# Ejemplo break
for numero in range(1, 10):
    if numero % 2 == 0:
        print(f"Par {numero}")
        break # rompe el ciclo que este iterando

# Ejemplo continue
for numero in range(1, 10):
    if numero % 2 == 1:
        continue # pasa a la otra iteracion
    print(f"Par {numero}")
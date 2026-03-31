# Operadores aritméticos
# son los operadores que se utilizan para realizar operaciones matemáticas básicas, como suma, resta, multiplicación, división, etc.
# necesitan al menos un operando para funcionar, y pueden ser unarios (con un solo operando) o binarios (con dos operandos).
# +, -, *, /, //, %, **
## suma
a = 10
b = 3
c = a + b
print(f"La suma de {a} y {b} es: {c}")
## resta
c = a - b
print(f"La resta de {a} y {b} es: {c}")
## multiplicación
c = a * b
print(f"La multiplicación de {a} y {b} es: {c}")
## división
c = a / b
print(f"La división de {a} y {b} es: {c:.2f}")  # .2f para mostrar solo 2 decimales
## división entera
c = a // b
print(f"La división entera de {a} y {b} es: {c}")
## módulo
c = a % b
print(f"El módulo de {a} y {b} es: {c}")
## potencia
c = a ** b
print(f"La potencia de {a} elevado a {b} es: {c}")
# Funcion range en python
# funcion incorporada que genera una secuencia de numeros

# es comunmente utilizada para iterar sabre ciclos tipo for

# Sintaxis function range
# inicio - valor inicial (Optonial)
# fin - valor final, sin incluirlo
# incremento - diferencia entre cada numero (optonial)
# range(inicio, fin, incremento)

# usar range para imprimir 0 al 4
for i in range(5):
    print(i, end=' ')
print("")
# usar range para imprimir del 0 al 9
# con incremento de 2
for i in range (0, 10, 2):
    print(i, end=" ") # imprimet 0, 2, 4, 6, 8

print("")
cadena = input("cual es tu mensaje: ")
numero_rep = int(input("Cuantas veces: "))
# el _ es para usarse cuando la variable no se usara, por lo que se pone un _
for _ in range(numero_rep):
    print(cadena)
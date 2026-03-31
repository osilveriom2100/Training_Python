import random
print("Numero secreto")
secreto = random.randint(0, 50)
intento = 0
numero = 0

while numero != secreto and intento < 10:
    numero = int(input("Aidvina el numero secreto entre 0 a 50: "))
    if secreto > numero:
        print(f"numero {numero} menor a numero secreto ")
    elif secreto < numero:
        print(f"numero {numero} mayor a numero secreto ")
    intento += 1
    print(f"Numero de intento {intento}")
else:
    print(f"Adivinaste el juego" if intento < 10 else f"Perdiste")
    print("Saliste del juego")
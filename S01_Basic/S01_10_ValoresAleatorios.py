# valores aleatorios en python
import random # módulo para generar valores aleatorios
#from random import randint, random # también podemos importar funciones específicas del módulo, lo que nos permite usarlas directamente sin el prefijo del módulo

# randint(a, b) -> devuelve un número entero aleatorio entre a y b (inclusive)
random_number = random.randint(1, 100)
print(random_number)

# también podemos usar la función randint() directamente sin el prefijo del módulo si la importamos específicamente
#random_number = randint(1, 100)
#print(random_number)

# random() -> devuelve un número flotante aleatorio entre 0.0 y 1.0
random_float = random.random()
print(random_float)

# también podemos generar un número aleatorio dentro de un rango específico usando random() y escalando el resultado
min_value = 1
max_value = 10
random_scaled = random.random() * (max_value - min_value) + min_value
print(random_scaled)

# Generar un ID aleatorio
nombre = input("Ingrese su nombre: ").strip()
apellido = input("Ingrese su apellido: ").strip()
ano_nacimiento = input("Ingrese su año de nacimiento: ").strip()
valor_aleatorio = random.randint(1000, 9999)
id_usuario = f"{nombre[0:2]}{apellido[0:2]}{ano_nacimiento[-2:]}{str(valor_aleatorio)}".upper()
print(f"Su ID de usuario es: {id_usuario}")
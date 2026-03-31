# Atuoenticacion de usuario
USUARIO = "victor"
CONTRASENA = "1234"
usuario_ingresado = input("Ingrese su usuario: ")
contrasena_ingresada = input("Ingrese su contraseña: ")

if USUARIO == usuario_ingresado.lower().strip() and CONTRASENA == contrasena_ingresada.lower().strip():
    print("¡Bienvenido, Victor!")
else:
    print("Usuario o contraseña incorrectos. Intente nuevamente.")

# Valor dentro de un rango
VALOR_MINIMO = 0
VALOR_MAXIMO = 5
valor_ingresado = int(input(f"Ingrese un valor entre {VALOR_MINIMO} y {VALOR_MAXIMO}: "))
if VALOR_MINIMO <= valor_ingresado <= VALOR_MAXIMO:
    print(f"El valor {valor_ingresado} esta dentro del rango permitido.")
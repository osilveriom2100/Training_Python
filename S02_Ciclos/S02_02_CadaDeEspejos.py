## caja de spejos

# edad = int(input("Cual es tu edad? "))
# is_miedo = input("Tines medio a la oscuridad si/no? ").strip().lower() == 'si'

# if edad > 10 and not is_miedo:
#     print("Puedes entrar")
# else:
#     print("No puedes entrar")

## Operador ternario
# Una forma compacta de agregar una condicion, y el condicion y el objetivo es asignar un valor 
# a un variable dependiendo del valor de la condicion
# Sintaxis operador ternario
# resultado = valor_ternario if condicion else valor_si_falso

# Ejemplo operador ternario
edad = 18
es_adulto = "Si" if edad >= 18 else "No"
print(f" es adulto? {es_adulto}")

## Reserva Hotel
# nombre = input('Cual es tu nombre? ')
# dias_estandia = int(input("Cuantos dias reservaras? "))
# vista_mar = input("Cuarto con vista al mar si/no? ").strip().lower()

# precio = 190.5 if vista_mar == 'si' else 150.5
# print(f"""Reserva de {nombre}
# Dias de reservacion {dias_estandia}
# Costo de la estandia: ${precio * dias_estandia}
# Su cuarto {vista_mar} es con vista al mar""")


# num = int(input("Numero1 "))
# min = int(input("Numero2 "))
# print(f"El numero mayor es {num}" if num > min else f"El numero menor es {min}")

mes = 9
if mes in [1, 2, 12]:
    print("Invierno")
elif mes in [3, 4, 5]:
    print("Primavera")
elif mes in [6, 7, 8]:
    print("Verano")
elif mes in [8, 9, 10]:
    print("Otoño")
else:
    print("Estaion desconocida")
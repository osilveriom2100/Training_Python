# Sentencia de decision nos permiten controlar el flujo de ejecucion
# La estructura que se pueden usar son: if, else y elif
# La sentenia if permite ejecutar un bloque de codigo si la condicion a evaluar es verdadera,

# Ejemplo sentencia if
edad = 15
if edad > 18:
    print(f"eres mayor de edad. Tienes {edad}")
elif 15 <= edad <= 18:
    print(f"Eres adolesente. Tienes {edad}")
else:
    print(f"Eres menor de edad. Tienes {edad}")

# Numero positivo
numero = 5
if numero > 0:
    print(f"Numero positivo")
elif numero < 0:
    print(f"Numero negativo")
else:
    print(f"es cero")

mienbro_tienda = input("Eres miembro de la tienda (si/no): ").strip().lower() == "si"
compra = float(input("Monto de la compra: "))

if True == mienbro_tienda and compra >= 1000:
    print(f"Descuento 10%, compra {compra - compra*0.1}") 
elif True == mienbro_tienda:
    print(f"Descuento 5%, compra {compra - compra*0.05}")
else:
    print(f"Descuento 0%, compra {compra - compra*0}")

salir_sistem_txt = input('Deseas salir del sistema (si/no)? ')
salir_sistema = salir_sistem_txt.strip().lower() == 'si'

if not salir_sistema:
    print('continuamos')
else:
    print('salimos')
# inventarrio = []

# numero_inventario = int(input("Cuantos valores dgitaras? "))

# for _ in range(numero_inventario):
#     nombre = input("ingresa el nombre")
    
inventario = [{'id': 1, 'nombre': 'victor', 'precio': 25.5, 'cantidad': 50},
            {'id': 2, 'nombre': 'diego', 'precio': 35.5, 'cantidad': 10},
            {'id': 3, 'nombre': 'oman', 'precio': 55.5, 'cantidad': 30}]

nombre = 'victor'

for elemento in inventario:
    if elemento['nombre'] == nombre:
        print('ya existe')

if any(elemento['nombre'] == nombre for elemento in inventario):
    print('ya existe')
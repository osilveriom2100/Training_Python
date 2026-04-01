print('Combinar listas y diccionarios')

variables = []

variables = [{'nombre': 'Juan', 'appellido': 'Perez', 'edad': 30}, 
            {'nombre': 'Maria', 'apellido': 'Gomez', 'edad': 25}]

print(f'Lista de diccionarios: {variables}')
for diccionario in variables:
    for key, value in diccionario.items():
        print(f'{key}: {value}')

# acceder a un valor especifico de un diccionario dentro de la lista
print(f'El nombre del primer diccionario es: {variables[0]["nombre"]}')
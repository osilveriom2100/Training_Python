print('Diccionarios en Python')

# Un diccionario es una estructura de datos que almacena pares de clave-valor.
# Las claves (key) deben ser únicas y pueden ser de cualquier tipo inmutable (como cadenas, números o tuplas).
# Los valores pueden ser de cualquier tipo, incluyendo otros diccionarios.

# Crear un diccionario vacío
diccionario = {}
print(f'Diccionario vacío: {diccionario}')

# Crear un diccionario con algunos pares clave-valor
persona = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
print(f'Persona: {persona}')

# Acceder a los valores utilizando las claves
print(f'Nombre: {persona["nombre"]}')
print(f'Edad: {persona.get("edad")}')

# modificar un valor
persona['edad'] = 31
print(f'Persona actualizada: {persona}')

# Agregar un nuevo par clave-valor, si la clave ya existe se actualiza el valor
persona['profesion'] = 'Ingeniero'
print(f'Persona con profesión: {persona}')

# Eliminar un par clave-valor
del persona['ciudad']
print(f'Persona sin ciudad: {persona}')

persona.pop('profesion') # Elimina la clave 'profesion' y devuelve su valor
print(f'Persona sin profesión: {persona}')

# Iterar sobre un diccionario, obteniendo tanto las claves como los valores
print('Iterando sobre el diccionario:')
for clave, valor in persona.items():        # items() devuelve una vista de los pares clave-valor del diccionario
    print(f'{clave}: {valor}')

# obtener solo las claves o los valores
print(f'Claves: {persona.keys()}')          # keys() devuelve una vista de las claves del diccionario
print(f'Valores: {persona.values()}')      # values() devuelve una vista de los valores del diccionario


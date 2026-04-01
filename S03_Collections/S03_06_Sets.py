print(' Manejo de sets en Python ')
# Un set es una colección de elementos únicos, sin orden específico y mutable.
# Se pueden crear utilizando la función set() o con llaves {}.
# Crear un set con la función set()
mi_set = set([1, 2, 3, 4, 5])
print('Set creado con la función set():', mi_set)
# Crear un set con llaves {}
otro_set = {6, 7, 8, 9, 10}
print('Set creado con llaves {}:', otro_set)

# verificar que no se agregan elementos duplicados
mi_set.add(3)  # Intentar agregar un elemento duplicado
print('Set después de intentar agregar un elemento duplicado:', mi_set)

# Agregar un nuevo elemento al set
mi_set.add(6)
print('Set después de agregar un nuevo elemento:', mi_set)

# Eliminar un elemento del set
mi_set.remove(2)
print(f'Set después de eliminar un elemento: {mi_set}')

# Verificar si un elemento está en el set
print(f'¿El número 3 está en el set? {3 in mi_set}')

# iterar sobre los elementos del set
print('Elementos en el set:')
for elemento in mi_set:
    print(elemento)

# longitud del set
print(f'Número de elementos en el set: {len(mi_set)}')

# operaciones de conjuntos
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# Unión de sets
union_set = set_a.union(set_b)
print(f'Unión de sets: {union_set}')

# unión de sets con el operador |
union_set_op = set_a | set_b
print(f'Unión de sets con operador |: {union_set_op}')

# Intersección de sets
interseccion_set = set_a.intersection(set_b)
print(f'Intersección de sets: {interseccion_set}')

# Intersección de sets con el operador &
interseccion_set_op = set_a & set_b
print(f'Intersección de sets con operador &: {interseccion_set_op}')

# Diferencia de sets
diferencia_set = set_a.difference(set_b)
print(f'Diferencia de sets (set_a - set_b): {diferencia_set}')

# Diferencia de sets con el operador -
diferencia_set_op = set_a - set_b
print(f'Diferencia de sets con operador -: {diferencia_set_op}')
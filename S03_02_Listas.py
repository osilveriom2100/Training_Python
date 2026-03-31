print('*** Manejo de listas ***')

mi_lista = [1, 2, 3, 4 , 5]
print(f'lista -> {mi_lista}')

# Largo de una lista
print(f'largo de la lista: {len(mi_lista)}')

# Acceder a los elmentos de la lista por indice
print(f'El valor del indice 4 es: {mi_lista[4]}')
print(f'El valor del indice 4 es: {mi_lista[-1]}')

# Modificar el elemento de una lista
mi_lista[1] = 10
print(f"Modificamos el valor del indice 1 es: {mi_lista[1]}")

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(f'El valor del indice 5 es: {mi_lista[-1]}')

# Añadir un nuevo elementos en un indice especifico
mi_lista.insert(2, 5)
print(f'lista -> {mi_lista}, se añadio el valor de 10 en el indice 2')

# Eliminar elementos de una lista
## usando el metodo remove
mi_lista.remove(5)
print(f'{mi_lista} se remove el primer elemento 5 de la lista')
## usando el metodo pop
mi_lista.pop(5)
print(f'{mi_lista} se removio el indice 5 de la lista')
## Elinar usando la palabra del
del mi_lista[3]
print(f'{mi_lista} se elimino el indice 2 de la lista')

# obtener sublista de una lista
sublista = mi_lista[1:3]
print(f'de lista {mi_lista} se creo sublista {sublista}')
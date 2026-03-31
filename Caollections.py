## Collection

#una colección es un tipo de dato que puede almacenar varios valores, 
# como una lista, un conjunto o un diccionario. 
# Las colecciones son útiles para organizar y manipular datos de manera eficiente.

# Listas
# Una lista es una colección ordenada y mutable de elementos.
# se pueden agregar, eliminar o modificar elementos en una lista.
# Las listas se definen utilizando corchetes [] y los elementos se separan por comas.
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)

# los elementos de una lista pueden ser de diferentes tipos de datos
mi_lista_mixta = [1, 'Hola', 3.14, True]
print(mi_lista_mixta)

# Las listas también pueden contener otras listas, lo que se conoce como listas anidadas.
mi_lista_anidada = [1, [2, 3], 4]
print(mi_lista_anidada)

# para acceder a los elementos de una lista, se utiliza el índice, que comienza en 0.
print(mi_lista[0])  # Imprime el primer elemento de la lista
# para modificar un elemento de la lista, se asigna un nuevo valor al índice correspondiente.
mi_lista[0] = 10
print(mi_lista)  # Imprime la lista modificada
# para agregar un elemento al final de la lista, se utiliza el método append().
mi_lista.append(6)
print(mi_lista)  # Imprime la lista con el nuevo elemento
# para eliminar un elemento de la lista, se utiliza el método remove() o del.
mi_lista.remove(3)  # Elimina el elemento con valor 3
print(mi_lista)  # Imprime la lista después de eliminar el elemento
del mi_lista[0]  # Elimina el elemento en el índice 0
print(mi_lista)  # Imprime la lista después de eliminar el elemento
# para ordenar una lista, se utiliza el método sort().
mi_lista.sort()
print(mi_lista)  # Imprime la lista ordenada
# para obtener la longitud de una lista, se utiliza la función len().
print(len(mi_lista))  # Imprime la longitud de la lista
# para verificar si un elemento está en la lista, se utiliza el operador in.
print(4 in mi_lista)  # Imprime True si el elemento 4 está en la lista, de lo contrario imprime False
# para recorrer los elementos de una lista, se puede utilizar un bucle for.
for elemento in mi_lista:
    print(elemento)  # Imprime cada elemento de la lista en una nueva línea
# para crear una lista a partir de una cadena de texto, se puede utilizar el método split().
cadena = "Hola mundo"
mi_lista_desde_cadena = cadena.split()
print(mi_lista_desde_cadena)  # Imprime la lista ['Hola', 'mundo']  
# para convertir una lista en una cadena de texto, se puede utilizar el método join().
mi_lista_para_cadena = ['Hola', 'mundo']
cadena_desde_lista = ' '.join(mi_lista_para_cadena)
print(cadena_desde_lista)  # Imprime la cadena "Hola mundo"
# para copiar una lista, se puede utilizar el método copy() o la función list().
mi_lista_copia = mi_lista.copy()
print(mi_lista_copia)  # Imprime la copia de la lista
mi_lista_copia2 = list(mi_lista)
print(mi_lista_copia2)  # Imprime la copia de la lista
# para limpiar una lista, se puede utilizar el método clear().
mi_lista.clear()
print(mi_lista)  # Imprime una lista vacía
# para invertir una lista, se puede utilizar el método reverse().
mi_lista_invertida = [1, 2, 3, 4, 5]
mi_lista_invertida.reverse()
print(mi_lista_invertida)  # Imprime la lista invertida
# para contar el número de veces que un elemento aparece en una lista, se puede utilizar el método count().
mi_lista_con_repetidos = [1, 2, 3, 2, 4, 2, 5]
print(mi_lista_con_repetidos.count(2))  # Imprime el número de veces que el elemento 2 aparece en la lista
# para encontrar el índice de la primera aparición de un elemento en una lista, se puede utilizar el método index().
mi_lista_con_repetidos = [1, 2, 3, 2, 4, 2, 5]
print(mi_lista_con_repetidos.index(2))  # Imprime el índice de la primera aparición del elemento 2 en la lista
# para eliminar el último elemento de una lista, se puede utilizar el método pop().
mi_lista_pop = [1, 2, 3, 4, 5]
ultimo_elemento = mi_lista_pop.pop()
print(ultimo_elemento)  # Imprime el último elemento eliminado de la lista
print(mi_lista_pop)  # Imprime la lista después de eliminar el último elemento
# para eliminar un elemento en un índice específico, se puede utilizar el método pop() con el índice como argumento.
mi_lista_pop = [1, 2, 3, 4, 5]
elemento_eliminado = mi_lista_pop.pop(2)  # Elimina el elemento en el índice 2
print(elemento_eliminado)  # Imprime el elemento eliminado de la lista
print(mi_lista_pop)  # Imprime la lista después de eliminar el elemento en el índice 2
# para extender una lista con otra lista, se puede utilizar el método extend().
mi_lista1 = [1, 2, 3]
mi_lista2 = [4, 5, 6]
mi_lista1.extend(mi_lista2)
print(mi_lista1)  # Imprime la lista extendida con los elementos de mi_lista2
# para concatenar dos listas, se puede utilizar el operador +.
mi_lista_concatenada = mi_lista1 + mi_lista2
print(mi_lista_concatenada)  # Imprime la lista concatenada con los elementos de mi_lista1 y mi_lista2
# para repetir una lista, se puede utilizar el operador *.
mi_lista_repetida = mi_lista1 * 2
print(mi_lista_repetida)  # Imprime la lista repetida con los elementos de mi_lista1 dos veces

# Tuplas
# Una tupla es una colección ordenada e inmutable de elementos.
# Las tuplas se definen utilizando paréntesis () y los elementos se separan por comas.
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
# los elementos de una tupla pueden ser de diferentes tipos de datos
mi_tupla_mixta = (1, 'Hola', 3.14, True)
print(mi_tupla_mixta)
# Las tuplas también pueden contener otras tuplas, lo que se conoce como tuplas anidadas.
mi_tupla_anidada = (1, (2, 3), 4)
print(mi_tupla_anidada)
# para acceder a los elementos de una tupla, se utiliza el índice, que comienza en 0.
print(mi_tupla[0])  # Imprime el primer elemento de la tupla
# para obtener la longitud de una tupla, se utiliza la función len().
print(len(mi_tupla))  # Imprime la longitud de la tupla
# para verificar si un elemento está en la tupla, se utiliza el operador in.
print(4 in mi_tupla)  # Imprime True si el elemento 4 está en la tupla, de lo contrario imprime False
# para recorrer los elementos de una tupla, se puede utilizar un bucle for.
for elemento in mi_tupla:
    print(elemento)  # Imprime cada elemento de la tupla en una nueva línea 
# para crear una tupla a partir de una cadena de texto, se puede utilizar el método split() y convertirlo en tupla.
cadena = "Hola mundo"
mi_tupla_desde_cadena = tuple(cadena.split())
print(mi_tupla_desde_cadena)  # Imprime la tupla ('Hola', 'mundo')
# para convertir una tupla en una cadena de texto, se puede utilizar el método join().
mi_tupla_para_cadena = ('Hola', 'mundo')
cadena_desde_tupla = ' '.join(mi_tupla_para_cadena)  # Imprime la cadena 'Hola mundo'
print(cadena_desde_tupla)
# para contar el número de veces que un elemento aparece en una tupla, se puede utilizar el método count().
mi_tupla_con_repetidos = (1, 2, 3, 2, 4, 2, 5)
print(mi_tupla_con_repetidos.count(2))  # Imprime el número de veces que el elemento 2 aparece en la tupla
# para encontrar el índice de la primera aparición de un elemento en una tupla, se puede utilizar el método index().
mi_tupla_con_repetidos = (1, 2, 3, 2, 4, 2, 5)
print(mi_tupla_con_repetidos.index(2))  # Imprime el índice de la primera aparición del elemento 2 en la tupla  

# Diccionarios
# Un diccionario es una colección no ordenada, mutable y indexada de pares clave-valor.
# Los diccionarios se definen utilizando llaves {} y los pares clave-valor se separan por comas, mientras que la clave y el valor se separan por dos puntos :.
mi_diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
print(mi_diccionario)
# los valores de un diccionario pueden ser de diferentes tipos de datos
mi_diccionario_mixto = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid', 'es_estudiante': True}
print(mi_diccionario_mixto)
# para acceder a los valores de un diccionario, se utiliza la clave entre corchetes [].
print(mi_diccionario['nombre'])  # Imprime el valor asociado a la clave 'nombre' en el diccionario
# para modificar un valor en un diccionario, se asigna un nuevo valor a la clave
mi_diccionario['edad'] = 31
print(mi_diccionario)  # Imprime el diccionario modificado
# para agregar un nuevo par clave-valor a un diccionario, se asigna un valor a una nueva clave.
mi_diccionario['profesion'] = 'Ingeniero'
print(mi_diccionario)  # Imprime el diccionario con el nuevo par clave-valor
# para eliminar un par clave-valor de un diccionario, se utiliza el método pop() o del.
mi_diccionario.pop('ciudad')  # Elimina el par clave-valor con la clave 'ciudad'
print(mi_diccionario)  # Imprime el diccionario después de eliminar el par clave-valor
del mi_diccionario['profesion']  # Elimina el par clave-valor con la clave 'profesion'
print(mi_diccionario)  # Imprime el diccionario después de eliminar el par clave-valor
# para obtener las claves de un diccionario, se utiliza el método keys().
print(mi_diccionario.keys())  # Imprime las claves del diccionario
# para obtener los valores de un diccionario, se utiliza el método values().
print(mi_diccionario.values())  # Imprime los valores del diccionario   
# para obtener los pares clave-valor de un diccionario, se utiliza el método items().
print(mi_diccionario.items())  # Imprime los pares clave-valor del diccionario
# para verificar si una clave está en el diccionario, se utiliza el operador in.
print('nombre' in mi_diccionario)  # Imprime True si la clave 'nombre' está en el diccionario, de lo contrario imprime False
# para recorrer los pares clave-valor de un diccionario, se puede utilizar un bucle for con el método items().
for clave, valor in mi_diccionario.items():
    print(f'{clave}: {valor}')  # Imprime cada par clave-valor del diccionario en una nueva línea
# para crear un diccionario a partir de dos listas, se puede utilizar la funcion zip() y dict().
claves = ['nombre', 'edad', 'ciudad']
valores = ['juan', 30, 'Madrid']
mi_diccionario_desde_listas = dict(zip(claves, valores))
print(mi_diccionario_desde_listas)  # Imprime el diccionario creado a partir de las listas de claves y valores
# para crear un diccionario a partir de una lista de tuplas, se puede utilizar la función dict().
lista_de_tuplas = [('nombre', 'Juan'), ('edad', 30), ('ciudad', 'Madrid')]
mi_diccionario_desde_tuplas = dict(lista_de_tuplas)
print(mi_diccionario_desde_tuplas)  # Imprime el diccionario creado a partir de la lista de tuplas
# para crear un diccionario a partir de una cadena de texto, se puede utilizar el método split() y dict().
cadena = "nombre:Juan,edad:30,ciudad:Madrid"
pares_clave_valor = [par.split(':') for par in cadena.split(',')]
mi_diccionario_desde_cadena = dict(pares_clave_valor)
print(mi_diccionario_desde_cadena)  # Imprime el diccionario creado a partir de la cadena de texto
# para convertir un diccionario en una cadena de texto, se puede utilizar el método join() y una comprensión de listas.
mi_diccionario_para_cadena = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
cadena_desde_diccionario = ', '.join([f'{clave}:{valor}' for clave, valor in mi_diccionario_para_cadena.items()])
print(cadena_desde_diccionario)  # Imprime la cadena "nombre:Juan, edad:30, ciudad:Madrid"
# para copiar un diccionario, se puede utilizar el método copy() o la función dict().
mi_diccionario_copia = mi_diccionario.copy()
print(mi_diccionario_copia)  # Imprime la copia del diccionario
mi_diccionario_copia2 = dict(mi_diccionario)
print(mi_diccionario_copia2)  # Imprime la copia del diccionario
# para limpiar un diccionario, se puede utilizar el método clear().
mi_diccionario.clear()
print(mi_diccionario)  # Imprime un diccionario vacío

# Conjuntos
# Un conjunto es una colección no ordenada, mutable y sin elementos duplicados.
# Los conjuntos se definen utilizando llaves {} o la función set() y los elementos se separan por comas.
mi_conjunto = {1, 2, 3, 4, 5}
print(mi_conjunto)
# los elementos de un conjunto pueden ser de diferentes tipos de datos, pero deben ser inmutables.
mi_conjunto_mixto = {1, 'Hola', 3.14, True}
print(mi_conjunto_mixto)
# para agregar un elemento a un conjunto, se utiliza el método add().
mi_conjunto.add(6)  
print(mi_conjunto)  # Imprime el conjunto con el nuevo elemento
# para eliminar un elemento de un conjunto, se utiliza el método remove() o discard().
mi_conjunto.remove(3)  # Elimina el elemento 3 del conjunto
print(mi_conjunto)  # Imprime el conjunto después de eliminar el elemento
mi_conjunto.discard(4)  # Elimina el elemento 4 del conjunto, pero no genera un error si el elemento no existe
print(mi_conjunto)  # Imprime el conjunto después de eliminar el elemento
# para verificar si un elemento está en el conjunto, se utiliza el operador in.
print(2 in mi_conjunto)  # Imprime True si el elemento 2 está en el conjunto, de lo contrario imprime False
# para obtener la longitud de un conjunto, se utiliza la función len().
print(len(mi_conjunto))  # Imprime la longitud del conjunto
# para recorrer los elementos de un conjunto, se puede utilizar un bucle for.
for elemento in mi_conjunto:
    print(elemento)  # Imprime cada elemento del conjunto en una nueva línea
# para realizar operaciones de conjuntos, se pueden utilizar los métodos union(), intersection(), difference() y symmetric_difference().
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}
print(conjunto_a.union(conjunto_b))  # Imprime la unión de los conjuntos A y B
print(conjunto_a.intersection(conjunto_b))  # Imprime la intersección de los conjuntos A y B
print(conjunto_a.difference(conjunto_b))  # Imprime la diferencia de los conjuntos A y B
print(conjunto_a.symmetric_difference(conjunto_b))  # Imprime la diferencia simétrica de los conjuntos A y B
# para copiar un conjunto, se puede utilizar el método copy() o la función set().
mi_conjunto_copia = mi_conjunto.copy()
print(mi_conjunto_copia)  # Imprime la copia del conjunto
mi_conjunto_copia2 = set(mi_conjunto)
print(mi_conjunto_copia2)  # Imprime la copia del conjunto
# para limpiar un conjunto, se puede utilizar el método clear().
mi_conjunto.clear()
print(mi_conjunto)  # Imprime un conjunto vacío

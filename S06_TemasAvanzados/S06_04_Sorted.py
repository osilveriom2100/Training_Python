#Funcion Sorted es una función incorporada en Python que se utiliza para ordenar elementos de una secuencia (como listas, tuplas, etc.) y devuelve una nueva lista ordenada. La sintaxis básica de la función sorted es la siguiente:
# sorted(iterable, key=None, reverse=False)
# Donde:
# iterable: Es la secuencia que se desea ordenar.   
# key: Es una función que se utiliza para extraer un valor de cada elemento de la secuencia, el cual se utilizará para realizar la comparación durante la ordenación. Si no se especifica, se ordenará por los valores de los elementos directamente.
# reverse: Es un valor booleano que indica si se desea ordenar en orden descendente (True) o en orden ascendente (False). Por defecto, es False.
# Ejemplo:
numeros = [5, 2, 9, 1, 5, 6]
numeros_ordenados = sorted(numeros) 
print(numeros_ordenados)  # Output: [1, 2, 5, 5, 6, 9]
# En este ejemplo, la función sorted toma la lista numeros y devuelve una nueva lista ordenada llamada numeros_ordenados. La lista original numeros no se modifica, ya que sorted devuelve una nueva lista ordenada. El resultado es [1, 2, 5, 5, 6, 9], que es la versión ordenada de la lista original.
# Ejemplo con key:
palabras = ['banana', 'apple', 'cherry', 'date']    
palabras_ordenadas = sorted(palabras, key=len)
print(palabras_ordenadas)  # Output: ['date', 'apple', 'banana', 'cherry']
# En este ejemplo, la función sorted toma la lista palabras y utiliza el argumento key para ordenar las palabras según su longitud. La función len se utiliza como clave para extraer la longitud de cada palabra, y la lista se ordena en función de esa longitud. El resultado es ['date', 'apple', 'banana', 'cherry'], que es la lista de palabras ordenada por su longitud, desde la más corta hasta la más larga.
# Ejemplo con reverse:   
numeros_descendente = sorted(numeros, reverse=True)
print(numeros_descendente)  # Output: [9, 6, 5, 5, 2, 1]
# En este ejemplo, la función sorted toma la lista numeros y utiliza el argumento reverse para ordenar los números en orden descendente. El resultado es [9, 6, 5, 5, 2, 1], que es la versión ordenada de la lista original en orden descendente.      
#Ordenar un diccionario por sus valores:
diccionario = {'a': 3, 'b': 1, 'c': 2}
diccionario_ordenado = sorted(diccionario.items(), key=lambda item: item[1])
print(diccionario_ordenado)  # Output: [('b', 1), ('c', 2), ('a', 3)]   
# En este ejemplo, la función sorted toma los elementos del diccionario utilizando el método items(), que devuelve una lista de tuplas (clave, valor). Luego, se utiliza una función lambda como clave para ordenar las tuplas según el segundo elemento (valor) de cada tupla. El resultado es [('b', 1), ('c', 2), ('a', 3)], que es la lista de tuplas ordenada por los valores del diccionario en orden ascendente.
# Ordenar un diccionario por sus claves:
diccionario_ordenado_claves = sorted(diccionario.items(), key=lambda item: item[0])
print(diccionario_ordenado_claves)  # Output: [('a', 3), ('b', 1), ('c', 2)]
# En este ejemplo, la función sorted toma los elementos del diccionario utilizando el método items(), que devuelve una lista de tuplas (clave, valor). Luego, se utiliza una función lambda como clave para ordenar las tuplas según el primer elemento (clave) de cada tupla. El resultado es [('a', 3), ('b', 1), ('c', 2)], que es la lista de tuplas ordenada por las claves del diccionario en orden ascendente.
# lista en de diccionarios ordenada por un valor específico:
lista_diccionarios = [{'nombre': 'Alice', 'edad': 30}, {'nombre': 'Bob', 'edad': 25}, {'nombre': 'Charlie', 'edad': 35}]
lista_ordenada = sorted(lista_diccionarios, key=lambda x: x['edad'])   
print(lista_ordenada)  # Output: [{'nombre': 'Bob', 'edad': 25}, {'nombre': 'Alice', 'edad': 30}, {'nombre': 'Charlie', 'edad': 35}]
# En este ejemplo, la función sorted toma una lista de diccionarios y utiliza una función lambda como clave para ordenar los diccionarios según el valor asociado a la clave 'edad'. El resultado es una nueva lista de diccionarios ordenada por la edad en orden ascendente, con Bob (25) primero, seguido de Alice (30) y Charlie (35).       
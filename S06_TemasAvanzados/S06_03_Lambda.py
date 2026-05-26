#Funcion lamnda es una función anónima, es decir, no tiene un nombre específico. Se utiliza para crear funciones pequeñas y de una sola línea de código. La sintaxis básica de una función lambda es la siguiente:
# lambda argumentos: expresión 
# Ejemplo:
suma = lambda x, y: x + y
print(suma(3, 5))  # Output: 8
# Las funciones lambda también se pueden usar con funciones de orden superior como map, filter y reduce
# Ejemplo con map:
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Output: [1, 4, 9, 16, 25]
#Funcion map aplica la función lambda a cada elemento de la lista numeros y devuelve una nueva lista con los resultados. En este caso, se calcula el cuadrado de cada número en la lista.   
# Ejemplo con filter:
numeros2 = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros2))
print(pares)  # Output: [2, 4]  
# La función filter utiliza la función lambda para filtrar los elementos de la lista numeros2, devolviendo solo aquellos que son pares (es decir, aquellos que cumplen la condición x % 2 == 0). En este caso, se obtiene una nueva lista con los números pares [2, 4]. 
# Ejemplo con reduce:
from functools import reduce
numeros3 = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x * y, numeros3)
print(producto)  # Output: 120
# La función reduce utiliza la función lambda para aplicar una operación de reducción a los elementos de la lista numeros3. En este caso, se calcula el producto de todos los números en la lista, lo que da como resultado 120 (1 * 2 * 3 * 4 * 5).    

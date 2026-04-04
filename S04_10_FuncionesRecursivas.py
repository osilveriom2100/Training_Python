# Funciones recursivas
# Una función recursiva es aquella que se llama a sí misma para resolver un problema.
# La recursividad es una técnica de programación que permite resolver problemas de manera elegante y eficiente, dividiendo el problema en subproblemas más pequeños y manejables.
# Para que una función recursiva funcione correctamente, debe tener una condición de parada que evite que la función se llame a sí misma indefinidamente, lo que causaría un error de desbordamiento de pila (stack overflow).
# Estructura básica de una función recursiva:
# def funcion_recursiva(parametros):
#     if condicion_de_parada:
#         return resultado_base
#     else:
#         return funcion_recursiva(parametros_modificados)

# Ejemplo de función recursiva para calcular el factorial de un número:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Para calcular el factorial de un número, se llama a la función factorial con el número deseado como argumento. Por ejemplo, para calcular el factorial de 5:
resultado = factorial(5)
print(f"El factorial de 5 es: {resultado}") 

print('Imprimir del 1 al 5 de forma recursiva')

def imprimir_numeros(num):
    if num > 0:
        print(f'{num}')
        imprimir_numeros(num - 1)
    else:
        print('¡Fin de la recursión!')

imprimir_numeros(5)

def factorial(n):
    # val = 0
    # while val <= n:
    #     if val in [0, 1]:
    #         sum = 1
    #     else:
    #         sum = val * sum
    #     val +=1
    if n in [0, 1]:
        return 1

    else:
        return n * factorial(n - 1)

print(f"factorial de 5 es: {factorial(5)}")


def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base  * (potencia(base, exponente - 1)) 
        # La función potencia se llama a sí misma con el exponente reducido en 1, lo que permite calcular la potencia de manera recursiva. 
        # La condición de parada es cuando el exponente es igual a 0, en cuyo caso se devuelve 1.
    # call stack de la función potencia:
    # potencia(4, 5) -> 4 * potencia(4, 4) -> 4 * (4 * potencia(4, 3)) -> 4 * (4 * (4 * potencia(4, 2))) -> 4 * (4 * (4 * (4 * potencia(4, 1)))) -> 4 * (4 * (4 * (4 * 4))) -> 1024
    # Call stack es la estructura de datos que se utiliza para almacenar información sobre las funciones que se están ejecutando en un programa. 
    # Cada vez que se llama a una función, se crea un nuevo marco de pila (stack frame) que contiene información sobre la función, como sus 
    # parámetros y variables locales. Cuando la función termina su ejecución, el marco de pila se elimina y el control vuelve a la función que la llamó.
    # En el caso de la función potencia, cada llamada recursiva crea un nuevo marco de pila, y cuando se alcanza la condición de parada, los marcos de pila
    #  se van eliminando a medida que las funciones terminan su ejecución, devolviendo el resultado final. 
    # LIFO (Last In, First Out) es el principio que rige el funcionamiento de la pila, donde el último elemento en entrar es el primero en salir.

def potencia_iterativa(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado
    
print(f'{potencia(4, 1)} igual a {4**1}')
print(f'{potencia_iterativa(4, 5)} igual a {4**5}')
# Funciones en python
- Las funciones son bloques de código reutilizables que realizan una tarea específica.
- Existen funciones predefinidas en Python, pero también podemos crear nuestras propias funciones.

## Sintaxis para definir una función:
```python
    def nombre_de_la_funcion(parametros_opcionales):
        """Docstring (opcional): descripción de la función."""
        #Código de la función
        return valor_de_retorno (opcional)
```

* Las funciones pueden tener parámetros, que son variables que se pasan a la función para que las utilice en su ejecución. También pueden devolver un valor utilizando la palabra clave `return`.   
* Llamar a una función se hace escribiendo su nombre seguido de paréntesis, y dentro de los paréntesis se pasan los argumentos necesarios.
    * Ejemplo de función sin parámetros ni valor de retorno:
    ```python
    def saludar():
        """Esta función saluda a todos."""
        print("¡Hola a todos!")

    # Llamar a la función
    saludar()
    ```
    * Ejemplo de función con parámetros y sin valor de retorno:
    ```python
    def saludar_persona(nombre):
        """Esta función saluda a la persona cuyo nombre se le pasa como argumento."""
        print(f"Hola, {nombre}!")
    # Llamar a la función con un argumento
    saludar_persona("Alice")
    ```
    * Ejemplo de función con parámetros y sin valor de retorno:
    ```python
    def sumar(a, b):
        """Esta función devuelve la suma de dos números."""
        return a + b
    # Llamar a la función y almacenar el resultado
    resultado = sumar(5, 3)
    print(f"La suma de 5 y 3 es: {resultado}")
    ```
* funcion con parametros opcionales, se le asigna un valor por defecto al parametro. 
    * si no se le asigna un valor al parametro, se utiliza el valor por defecto
    * se puede poner `None` como valor por defecto, pero es mejor asignar un mensaje por defecto para evitar errores
    ```python
    # funcion con parametro opcional
    def saludar(mensaje="Hola, No agrege un mensaje"):
        print(mensaje)
    saludar()
    saludar("Hola, Funcion con parametro opcional")
    ```
* Las funciones también pueden tener parámetros con valores predeterminados, lo que significa que si no se proporciona un argumento para ese parámetro, se utilizará el valor predeterminado.
    ```python
    def saludar_con_saludo(nombre, saludo="Hola"):
        """Esta función saluda a la persona con un saludo personalizado."""
        print(f"{saludo}, {nombre}!")
    # Llamar a la función sin proporcionar el saludo, se usará el valor predeterminado
    saludar_con_saludo("Bob")
    # Llamar a la función proporcionando un saludo personalizado
    saludar_con_saludo("Charlie", "¡Buenos días!")
    ```
### Nota
Si defines dos funciones con el mismo nombre, la segunda reemplaza a la primera, aunque una tenga parámetro y la otra no.

## *args & **kwargs
### Las funciones también pueden aceptar un número variable de argumentos utilizando *args para argumentos posicionales y **kwargs para argumentos con nombre.
### *args permite pasar un número variable de argumentos posicionales a la función, y dentro de la función, args se trata como una tupla que contiene todos los argumentos pasados. De manera similar, **kwargs permite pasar un número variable de argumentos con nombre, y dentro de la función, kwargs se trata como un diccionario que contiene los pares clave-valor de los argumentos pasados.
- Ejemplo de uso de *args

    ```python
        def imprimir_numeros(*args):
            """Esta función imprime una lista de números."""
            for numero in args:
                print(numero)
        # Llamar a la función con un número variable de argumentos
        imprimir_numeros(1, 2, 3, 4, 5)
    ```
- Ejemplo de uso *arg como primero argumento variable
    ```python
        def superheroe_superpoderes(*args, nombre):
            print(f'superpoderes: {args} - nombre: {nombre}')
            for superpoder in args:
                print(f'superpoder: {superpoder}')
        # se pueden pasar cualquier número de argumentos posicionales a la función, pero el argumento con nombre debe ir al final 
        # y se debe especificar el nombre del argumento con nombre al llamar a la función ya que es un argumento con nombre
        # en caso de usar *args como primer argumento variable, se deben pasar los argumentos posicionales antes del argumento con nombre
        superheroe_superpoderes('vuelo', 'super fuerza', 'visión de rayos x', nombre='clark kent')
    ```
-  Ejemplo de uso de **kwargs
    ```python
        def imprimir_informacion(**kwargs):
            """Esta función imprime información proporcionada como argumentos con nombre."""
            for clave, valor in kwargs.items():
                print(f"{clave}: {valor}")
        # Llamar a la función con argumentos con nombre
        imprimir_informacion(nombre="Alice", edad=30, ciudad="Madrid")
    ```
-  Ejemplo de uso de **kwargs y variable
    ```python
    def superheroe_superpoderes(nombre, **kwargs):
        print(f'superheroe: {nombre} - superpoderes: {kwargs}')
        for superpoder, descripcion in kwargs.items():
            print(f'superpoder: {superpoder} - descripcion: {descripcion}')

    # se pueden pasar cualquier número de argumentos con nombre a la función, pero el argumento con nombre debe ir al principio
    # y se debe especificar el nombre del argumento con nombre al llamar a la función ya que es un argumento con nombre
    superheroe_superpoderes(nombre='clark kent', vuelo='puede volar a gran velocidad', super_fuerza='tiene una fuerza sobrehumana', vision_rayos_x='puede ver a través de objetos sólidos')
    ```
## Modulos

* Los modulos en Python son archivos que contienen definiciones y declaraciones de funciones, clases y variables.
* Los modulos permiten organizar el codigo en partes mas pequeñas y reutilizables, lo que facilita el mantenimiento y la legibilidad del codigo.
* Para crear un modulo, simplemente se crea un archivo con extension .py y se definen las funciones, clases y variables que se quieran incluir en el modulo.
* Para usar un modulo en otro archivo, se puede importar el modulo usando la palabra clave import seguida del nombre del modulo.
* Por ejemplo, si se tiene un archivo llamado S04_M01_Modulo_Sumar.py que contiene la funcion sumar, se puede importar el modulo en otro archivo usando `import S04_M01_Modulo_Sumar`, y luego usar la funcion sumar del modulo usando `S04_M01_Modulo_Sumar.sumar()`.  
    * En este archivo se define la funcion sumar que se usara en cualquier otro archivo que importe este modulo
    ```python
        # S04_M01_Modulo_Sumar.py
        # funcion con retorno
        def sumar(a, b):
            return a + b
    ```
    ```python
        # Sccript de desarrollo
        import S04_M01_Modulo_Sumar
        suma = S04_M01_Modulo_Sumar.sumar(a, b)
    
    ```
* para probar la funcion sumar, se puede ejecutar este archivo directamente
```python
if __name__ == "__main__":
    resultado = sumar(5, 3)
    print("El resultado de la suma es:", resultado)
```
* __name__ es una variable especial en Python que se asigna automáticamente  a "__main__" cuando el archivo se ejecuta directamente, y a el nombre del modulo cuando se importa. Esto permite que el bloque de codigo dentro del if __name__ == "__main__": solo se ejecute cuando el archivo se ejecuta directamente, y no cuando se importa como un modulo. 
* Cuando se importa este modulo en otro archivo, el bloque de codigo de prueba no se ejecutara, lo que permite que la funcion sumar se use sin ejecutar el codigo de prueba cada vez que se importe el modulo. y la variable __name__ se asignara al nombre del modulo, lo que permite que el bloque de codigo de prueba no se ejecute.  
    * ejemplo: si se importa este modulo en el archivo S04_03_Modulos.py,la variable __name__ se asignara a "S04_M01_Modulo_Sumar", lo que hara que el bloque de codigo de prueba no se ejecute.   
    * De esta manera, se puede probar la funcion sumar ejecutando este archivo directamente, y al mismo tiempo, se puede importar esta funcion en otros archivos sin que se ejecute el bloque de codigo de prueba.

## Alcance de variables
- Las varaibles definidas dentro de una función solo existen dentro de esa función, es decir, no pueden ser accedidas desde fuera de la función. Esto se conoce como alcance de variables o scope.
- Por ejemplo, si se define una variable dentro de una función, esa variable solo existirá dentro de esa función y no podrá ser accedida desde fuera de la función. Si se intenta acceder a esa variable desde fuera de la función, se obtendrá un error de NameError indicando que la variable no está definida.
- Sin embargo, si se define una variable fuera de una función, esa variable puede ser accedida desde dentro de la función, siempre y cuando no se intente modificar esa variable dentro de la función. Si se intenta modificar esa variable dentro de la función, se creará una nueva variable local con el mismo nombre, lo que puede causar confusión y errores en el código. Por lo tanto, es importante tener cuidado al usar variables con el mismo nombre tanto dentro como fuera de las funciones para evitar problemas de alcance de variables. 
- Ejemplo de alcance de variables
    ```python
    print(' Alcance de variables ')
    # variable global
    contador_global = 0

    def incrementar_contador():
        # variable local
        contador_local = 0
        contador_local += 1
        print(f'Contador local: {contador_local}')
        # se puede acceder a la variable global dentro de la funcion, pero para modificarla, se debe usar la palabra clave global   
        global contador_global
        contador_global += 1
        print(f'Contador global: {contador_global}')

    while contador_global < 5:
        # llamar a la funcion varias veces
        incrementar_contador()

    print(f'Contador global despues de llamar a la funcion: {contador_global}')
    # intentar acceder a la variable local fuera de la funcion
    try:
        print(contador_local) # esto generara un error de NameError porque contador_local no esta definida fuera de la funcion incrementar_contador()   
    except NameError as e:
        print(f'Error: {e}')
    ```

## Funciones recursivas
- Una función recursiva es aquella que se llama a sí misma para resolver un problema.
- La recursividad es una técnica de programación que permite resolver problemas de manera elegante y eficiente, dividiendo el problema en subproblemas más pequeños y manejables.
- Para que una función recursiva funcione correctamente, debe tener una condición de parada que evite que la función se llame a sí misma indefinidamente, lo que causaría un error de desbordamiento de pila (stack overflow).
- Estructura básica de una función recursiva:
    ```python
    def funcion_recursiva(parametros):
        if condicion_de_parada:
            return resultado_base
        else:
            return funcion_recursiva(parametros_modificados)
    ```      

- Ejemplo de función recursiva para calcular el factorial de un número:
    ```python
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    # Para calcular el factorial de un número, se llama a la función factorial con el número deseado como argumento. Por ejemplo, para calcular el factorial de 5:
    resultado = factorial(5)
    print(f"El factorial de 5 es: {resultado}") 
    ```  
- Ejemplo 2:
    ```python
    def potencia(base, exponente):
        if exponente == 1:
            return base
        else:
            return base  * (potencia(base, exponente - 1)) 
    ```
- Nota:
    - La función potencia se llama a sí misma con el exponente reducido en 1, lo que permite calcular la potencia de manera recursiva. 
    - La condición de parada es cuando el exponente es igual a 0, en cuyo caso se devuelve 1.
    - call stack de la función potencia:\
     potencia(4, 5) -> 4 * potencia(4, 4) -> 4 * (4 * potencia(4, 3)) -> 4 * (4 * (4 * potencia(4, 2))) -> 4 * (4 * (4 * (4 * potencia(4, 1)))) -> 4 * (4 * (4 * (4 * 4))) -> 1024
    - Call stack es la estructura de datos que se utiliza para almacenar información sobre las funciones que se están ejecutando en un programa. 
    - Cada vez que se llama a una función, se crea un nuevo marco de pila (stack frame) que contiene información sobre la función, como sus 
    - parámetros y variables locales. Cuando la función termina su ejecución, el marco de pila se elimina y el control vuelve a la función que la llamó.
    - En el caso de la función potencia, cada llamada recursiva crea un nuevo marco de pila, y cuando se alcanza la condición de parada, los marcos de pila
    -  se van eliminando a medida que las funciones terminan su ejecución, devolviendo el resultado final. 
    - LIFO (Last In, First Out) es el principio que rige el funcionamiento de la pila, donde el último elemento en entrar es el primero en salir.



## Las funciones son fundamentales en la programación, ya que permiten organizar el código, evitar la repetición y mejorar la legibilidad.

### Ventajas de usar funciones:
1. Reutilización de código: Las funciones permiten escribir un bloque de código una vez y reutilizarlo en diferentes partes del programa.
2. Organización: Las funciones ayudan a organizar el código en bloques lógicos, lo que facilita su comprensión y mantenimiento.
3. Abstracción: Las funciones permiten ocultar los detalles de implementación y centrarse en la funcionalidad, lo que mejora la legibilidad del código.
4. Facilitan la depuración: Al dividir el código en funciones, es más fácil identificar y corregir errores, ya que cada función puede ser probada de manera independiente.    
5. Modularidad: Las funciones permiten dividir un programa en módulos más pequeños y manejables, lo que facilita el desarrollo y la colaboración entre programadores. 
6. Parametrización: Las funciones pueden aceptar parámetros, lo que las hace más flexibles y adaptables a diferentes situaciones. 


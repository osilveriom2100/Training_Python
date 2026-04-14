# Clases y Objetos en Python
En Python, la programación orientada a objetos (POO) es un paradigma de programación que se basa en el concepto de "objetos". Un objeto es una instancia de una clase, que es una plantilla para crear objetos. La POO permite organizar el código de manera más modular y reutilizable, facilitando la creación de programas complejos.
- una instacia es un objeto creado a partir de una clase. Cada instancia puede tener sus propios atributos y métodos, lo que permite que cada objeto tenga su propio estado y comportamiento.
- una clase es una plantilla o un molde que define las características y comportamientos comunes de los objetos que se crean a partir de ella. Una clase puede contener atributos (variables) y métodos (funciones) que definen el comportamiento de los objetos creados a partir de la clase.  

En resumen, una clase es una plantilla para crear objetos, mientras que una instancia es un objeto específico creado a partir de esa clase. La POO permite organizar el código de manera más modular y reutilizable, facilitando la creación de programas complejos.  

- Para crear una clase en Python, se utiliza la palabra clave "class" seguida del nombre de la clase. Dentro de la clase, se pueden definir atributos y métodos. Los atributos son variables que almacenan información sobre el objeto, mientras que los métodos son funciones que definen el comportamiento del objeto.    
- Para crear una instancia de una clase, se llama a la clase como si fuera una función, pasando los argumentos necesarios para inicializar los atributos del objeto. Por ejemplo, si tenemos una clase "Persona" con un atributo "nombre", podemos crear una instancia de la clase de la siguiente manera:  

- Partes de una clase en Python:
    1. Definición de la clase: Se utiliza la palabra clave "class" seguida del nombre de la clase para definir una nueva clase.
    2. Método __init__: Es un método especial que se llama automáticamente cuando se crea una instancia de la clase. Se utiliza para inicializar los atributos del objeto. 
    - El método __init__ recibe como primer argumento "self", que hace referencia a la instancia del objeto que se está creando. Además, puede recibir otros argumentos para inicializar los atributos del objeto.  
     3. Atributos: Son variables que almacenan información sobre el objeto. Se definen dentro del método __init__ y se acceden a través de la instancia del objeto.
    4. Métodos: Son funciones que definen el comportamiento del objeto. Se definen dentro de la clase y se acceden a través de la instancia del objeto.

    ```Python
    # Ejemplo de una clase en Python:
    class Persona:
        def declaracion(self, nombre, apellido):
            self.nombre = nombre   
            self.apellido = apellido  

        def presentarse(self):
            return f"Hola, mi nombre es {self.nombre} {self.apellido}."
    # Crear la instacia de la clase persona
    persona1 = Persona()
    persona1.declaracion("Juan", "Pérez")
    print(persona1.presentarse())
    ```

- self es una referencia a la instancia actual de la clase. Es un parámetro que se utiliza en los métodos de una clase para acceder a los atributos y métodos de esa instancia. Cuando se define un método dentro de una clase, el primer parámetro debe ser "self", aunque no es necesario nombrarlo así, es una convención ampliamente utilizada en Python. El uso de "self" permite que cada instancia de la clase tenga sus propios atributos y métodos, lo que hace posible crear objetos con diferentes estados y comportamientos. Por ejemplo, si tenemos una clase "Persona" con un atributo "nombre", podemos usar "self.nombre" para acceder al nombre específico de cada instancia de la clase. En resumen, "self" es esencial para trabajar con objetos en Python y permite que cada instancia tenga su propia identidad y comportamiento.  
- identidad de una clase se refiere a la capacidad de cada instancia de una clase para tener su propia identidad única. En Python, cada vez que se crea una instancia de una clase, se le asigna un identificador único que la distingue de otras instancias. Esto significa que cada objeto creado a partir de una clase tiene su propia identidad y puede tener atributos y comportamientos diferentes. La identidad de una clase es importante porque permite que cada instancia tenga su propio estado y comportamiento, lo que hace posible crear objetos con diferentes características y funcionalidades. En resumen, la identidad de una clase es fundamental para la programación orientada a objetos en Python, ya que permite que cada instancia tenga su propia identidad única y pueda interactuar con otras instancias de manera independiente.   
- reutilización de código se refiere a la capacidad de utilizar el mismo código en diferentes partes de un programa o en diferentes programas sin tener que escribirlo nuevamente. En Python, la reutilización de código se puede lograr a través de la programación orientada a objetos (POO) utilizando clases y objetos. Al definir una clase, se puede crear una plantilla para objetos que comparten características y comportamientos comunes. Luego, se pueden crear múltiples instancias de esa clase, cada una con su propia identidad y estado, pero todas compartiendo el mismo código definido en la clase. Esto permite que el código sea más modular y fácil de mantener, ya que cualquier cambio realizado en la clase se reflejará automáticamente en todas las instancias creadas a partir de esa clase. En resumen, la reutilización de código es una ventaja clave de la programación orientada a objetos en Python, ya que permite escribir código más eficiente y fácil de mantener.   
- modularidad se refiere a la capacidad de dividir un programa en partes más pequeñas y manejables, conocidas como módulos. En Python, la modularidad se puede lograr a través de la programación orientada a objetos (POO) utilizando clases y objetos. Al definir una clase, se puede encapsular un conjunto de atributos y métodos relacionados en un solo módulo, lo que facilita la organización y el mantenimiento del código. Cada clase puede ser considerada como un módulo independiente que puede ser reutilizado en diferentes partes del programa o incluso en diferentes programas. La modularidad también permite que los desarrolladores trabajen en diferentes partes del programa de manera independiente, lo que mejora la colaboración y la eficiencia en el desarrollo de software. En resumen, la modularidad es una ventaja clave de la programación orientada a objetos en Python, ya que permite organizar el código de manera más eficiente y facilita el mantenimiento y la colaboración en proyectos de software.   
- reutilización de código y modularidad son dos conceptos clave en la programación orientada a objetos (POO) en Python. La reutilización de código se refiere a la capacidad de utilizar el mismo código en diferentes partes de un programa o en diferentes programas sin tener que escribirlo nuevamente. Esto se logra a través de la creación de clases y objetos, lo que permite que el código sea más modular y fácil de mantener. Por otro lado, la modularidad se refiere a la capacidad de dividir un programa en partes más pequeñas y manejables, conocidas como módulos. En Python, cada clase puede ser considerada como un módulo independiente que puede ser reutilizado en diferentes partes del programa o incluso en diferentes programas. La modularidad también permite que los desarrolladores trabajen en diferentes partes del programa de manera independiente, lo que mejora la colaboración y la eficiencia en el desarrollo de software. En resumen, tanto la reutilización de código como la modularidad son ventajas clave de la programación orientada a objetos en Python, ya que permiten escribir código más eficiente, fácil de mantener y colaborativo.  
- En resumen, la programación orientada a objetos (POO) en Python es un paradigma de programación que se basa en el concepto de objetos. Una clase es una plantilla para crear objetos, mientras que una instancia es un objeto específico creado a partir de esa clase. La POO permite organizar el código de manera más modular y reutilizable, facilitando la creación de programas complejos. El método __init__ se utiliza como constructor para inicializar los atributos de un objeto, y el uso de self permite que cada instancia tenga su propia identidad única. La reutilización de código y la modularidad son ventajas clave de la POO en Python, ya que permiten escribir código más eficiente, fácil de mantener y colaborativo. 

- constructor es un método especial que se utiliza para inicializar los atributos de un objeto cuando se crea una instancia de una clase. En Python, el constructor se define utilizando el método especial "__init__". El constructor se llama automáticamente cuando se crea una instancia de la clase, y su función principal es asignar valores a los atributos del objeto. El constructor puede recibir argumentos que se utilizan para inicializar los atributos del objeto. Por ejemplo, si tenemos una clase "Persona" con un atributo "nombre", podemos definir un constructor que reciba el nombre como argumento y lo asigne al atributo "nombre" del objeto. De esta manera, cada vez que se cree una instancia de la clase "Persona", se podrá proporcionar un nombre específico para esa instancia. En resumen, el constructor es una parte fundamental de la programación orientada a objetos en Python  
    ```Python    
    # sintaxis del método __init__:
    class NombreDeLaClase:
        def __init__(self, arg1, arg2, ...):
            self.atributo1 = arg1
            self.atributo2 = arg2
    ```   
    -  En este ejemplo, "NombreDeLaClase" es el nombre de la clase, "__init__" es el método constructor, "arg1", "arg2", etc. son los argumentos que se pasan al constructor para inicializar los atributos del objeto, y "self.atributo1", "self.atributo2", etc. son los atributos del objeto que se inicializan con los valores de los argumentos. Al crear una instancia de la clase, se llamará automáticamente al método __init__ para inicializar los atributos del objeto con los valores proporcionados.
    - El método __init__ es un constructor que se utiliza para inicializar los atributos de un objeto cuando se crea una instancia de una clase. Es un método especial que se llama automáticamente cuando se crea un objeto a partir de una clase. El método __init__ recibe como primer argumento "self", que hace referencia a la instancia del objeto que se está creando, y puede recibir otros argumentos para inicializar los atributos del objeto. Por ejemplo, si tenemos una clase "Persona" con un atributo "nombre", podemos definir un método __init__ que reciba el nombre como argumento y lo asigne al atributo "nombre" del objeto. De esta manera, cada vez que se cree una instancia de la clase "Persona", se podrá proporcionar un nombre específico para esa instancia. En resumen, el método __init__ es esencial para la programación orientada a objetos en Python, ya que permite inicializar los atributos de un objeto de manera eficiente y flexible.  

- En caso de no usar el __init__, se puede crear una instancia de la clase sin inicializar los atributos, lo que puede llevar a errores al intentar acceder a esos atributos más adelante en el código. Por ejemplo, si intentamos acceder al atributo "nombre" de una instancia de la clase Persona sin haberlo inicializado previamente, obtendremos un error de atributo no encontrado. Por lo tanto, es importante utilizar el método __init__ para asegurarnos de que los atributos de la clase estén correctamente inicializados y evitar posibles errores en el código.
- Ejemplo de un constructor:
    ```Python  
    class Persona:

        def __init__(self, nombre, apellido): 
            self.nombre = nombre    # El uso de self permite que cada instancia tenga su propia identidad única, es una referencia a la instancia actual de la clase y se utiliza para acceder a los atributos y métodos de esa instancia   
            self.apellido = apellido # self.nombre y self.apellido son atributos de la clase Persona, que se inicializan con los valores pasados como argumentos al crear una instancia de la clase. Cada instancia de la clase Persona tendrá su propio nombre y apellido, lo que permite que cada objeto tenga su propia identidad única.
        def presentarse(self):
            return f"Hola, mi nombre es {self.nombre} {self.apellido}."
    ``` 
    - Crear una instancia de la clase Persona, lo que se conoce como crear un objeto a partir de la clase. Al crear una instancia, se llama al método __init__ para inicializar los atributos del objeto con los valores proporcionados. En este caso, se crea una instancia llamada persona1 con el nombre "Juan" y el apellido "Pérez". Cada vez que se crea una instancia de la clase Persona, se le asigna su propia identidad única, lo que permite que cada objeto tenga sus propios atributos y comportamientos. 
    - Al crear la instancia persona1, se le asigna un identificador único que la distingue de otras instancias de la clase Persona. Esto significa que persona1 tiene su propia identidad y puede tener atributos y comportamientos diferentes a otras instancias de la clase Persona. En resumen, al crear una instancia de una clase en Python, se le asigna una identidad única que permite que cada objeto tenga su propio estado y comportamiento. 
    ```Python  
        persona1 = Persona("Juan", "Pérez")
        print(persona1.presentarse())
    ```
    - Output: Hola, mi nombre es Juan Pérez., lo que demuestra que la instancia persona1 tiene su propia identidad y puede acceder a los atributos y métodos definidos en la clase Persona.  
    - En este ejemplo, hemos definido una clase "Persona" con un método especial "__init__" que se llama automáticamente cuando se crea una instancia de la clase. El método "__init__" se utiliza para inicializar los atributos del objeto. En este caso, el atributo "nombre" se inicializa con el valor pasado como argumento al crear la instancia "persona1". 

### Identificador 
- Al crear la instancia "persona1", se le asigna un identificador único que la distingue de otras instancias de la clase "Persona". Esto significa que "persona1" tiene su propia identidad y puede tener atributos y comportamientos diferentes a otras instancias de la clase "Persona". En resumen, al crear una instancia de una clase en Python, se le asigna una identidad única que permite que cada objeto tenga su propio estado y comportamiento. 
- Además, hemos definido un método "presentarse" que devuelve una cadena de texto con el nombre completo de la persona. Al llamar a este método a través de la instancia "persona1", se muestra el mensaje "Hola, mi nombre es Juan Pérez.", lo que demuestra que la instancia "persona1" tiene su propia identidad y puede acceder a los atributos y métodos definidos en la clase "Persona".  

### Direccion de memoria de las instancias
- lo que demuestra que cada instancia de la clase Persona tiene su propia identidad única. Al imprimir la dirección de memoria de cada instancia utilizando la función id(), se puede observar que persona1 y persona2 tienen direcciones de memoria diferentes, lo que indica que son objetos distintos en la memoria. Esto refuerza el concepto de que cada instancia de una clase en Python tiene su propia identidad y puede tener atributos y comportamientos diferentes a otras instancias de la misma clase. En resumen, la dirección de memoria de las instancias es una evidencia tangible de la identidad única de cada objeto creado a partir de una clase en Python.
    ```Python  
        print(f"Dirección de memoria de persona1: {id(persona1)}")
    ```

    - cuando se usa persona1, self hace referencia a persona1, lo que permite acceder a los atributos y métodos de esa instancia específica. De manera similar, cuando se usa persona2, self hace referencia a persona2, lo que permite acceder a los atributos y métodos de esa instancia específica. Esto demuestra que cada instancia de la clase Persona tiene su propia identidad única y puede interactuar con otras instancias de manera independiente. En resumen, el uso de self en los métodos de una clase en Python es fundamental para permitir que cada instancia tenga su propia identidad y pueda acceder a sus propios atributos y métodos.    
    - esto es por su direccion de memoria, lo que demuestra que cada instancia de la clase Persona tiene su propia identidad única. Al imprimir la dirección de memoria de cada instancia utilizando la función id(), se puede observar que persona1 y persona2 tienen direcciones de memoria diferentes, lo que indica que son objetos distintos en la memoria. Esto refuerza el concepto de que cada instancia de una clase en Python tiene su propia identidad y puede tener atributos y comportamientos diferentes a otras instancias de la misma clase. En resumen, la dirección de memoria de las instancias es una evidencia tangible de la identidad única de cada objeto creado a partir de una clase en Python.   

    - Al imprimir la dirección de memoria de self dentro del método presentarse, se puede observar que la dirección de memoria de self coincide con la dirección de memoria de la instancia que está llamando al método. Esto demuestra que self hace referencia a la instancia específica que está utilizando el método, lo que permite acceder a los atributos y métodos de esa instancia. En resumen, el uso de self en los métodos de una clase en Python es fundamental para permitir que cada instancia tenga su propia identidad y pueda acceder a sus propios atributos y métodos.
    ```Python  
        def presentarse(self):
        print(f'Dirección de memoria de self: {id(self)}') 
        return f"Hola, mi nombre es {self.nombre} {self.apellido}."
    ```

    - Imprime la dirección de memoria de self, lo que demuestra que cada instancia de la clase Persona tiene su propia identidad única. Al imprimir la dirección de memoria de cada instancia utilizando la función id(), se puede observar que persona1 y persona2 tienen direcciones de memoria diferentes, lo que indica que son objetos distintos en la memoria. Esto refuerza el concepto de que cada instancia de una clase en Python tiene su propia identidad y puede tener atributos y comportamientos diferentes a otras instancias de la misma clase. En resumen, la dirección de memoria de las instancias es una evidencia tangible de la identidad única de cada objeto creado a partir de una clase en Python.
    ```Python  
        def presentarse(self):
        print(f'Dirección de memoria de self: {id(self)}')   
        return f"Hola, mi nombre es {self.nombre} {self.apellido}."
    ```

### En python no existe el concepto de sobrecarga de métodos, pero se puede simular utilizando argumentos por defecto o *args y **kwargs. 
- Por ejemplo, podríamos modificar la clase Aritmetica para que el método sumar pueda aceptar un número variable de argumentos: 
    ```Python  
    class Aritmetica:
        def __init__(self, *operadores):
            self.operadores = operadores
        def sumar(self):
            return sum(self.operadores)
        def restar(self):
            resultado = self.operadores[0]    
            for operador in self.operadores[1:]:
                resultado -= operador
            return resultado
        def multiplicar(self):
            resultado = 1
            for operador in self.operadores:
             resultado *= operador
            return resultado
        def dividir(self):
            resultado = self.operadores[0]
            for operador in self.operadores[1:]:
                if operador == 0:
                    return 0
                resultado /= operador
            return resultado
    ```
- De esta manera, podríamos crear una instancia de Aritmetica con cualquier cantidad de operadores y el método sumar sumaría todos ellos.   
    ```Python  
    aritmetica2 = Aritmetica(1, 2, 3, 4)
    print(f"Suma: {aritmetica2.sumar()}")  # Salida: Suma: 10
    print(f"Resta: {aritmetica2.restar()}")  # Salida: Resta: -8
    print(f"Multiplicación: {aritmetica2.multiplicar()}")  # Salida: Multiplicación: 24
     print(f"División: {aritmetica2.dividir()}")  # Salida: División: 0.041666666666666664
    ```
    - En este ejemplo, el método sumar suma todos los operadores proporcionados, mientras que el método restar resta todos los operadores a partir del primero. 
    - El método multiplicar multiplica todos los operadores, y el método dividir divide el primer operador por cada uno de los siguientes, manejando el caso de división por cero.

### Encapsulamiento
- El encapsulamiento es un principio fundamental de la programación orientada a objetos que se refiere a la ocultación de los detalles internos de una clase y la exposición de una interfaz pública para interactuar con esa clase. Esto permite proteger los datos y métodos internos de una clase, evitando que sean accedidos o modificados directamente desde fuera de la clase.   
- En Python, el encapsulamiento se logra utilizando convenciones de nomenclatura para indicar que ciertos atributos o métodos son privados. Por ejemplo, se puede usar un guion bajo (_) antes del nombre de un atributo o método para indicar que es privado y no debe ser accedido directamente desde fuera de la clase. Sin embargo, es importante destacar que esto es solo una convención y no impide realmente el acceso a esos atributos o métodos.
- Para aplicar el encapsulamiento de manera efectiva, se pueden proporcionar métodos públicos (también conocidos como getters y setters) para acceder y modificar los atributos privados de una clase. Esto permite controlar cómo se accede a los datos internos de la clase y garantiza que se mantenga la integridad de esos datos.  

    - Atributos privados: Son aquellos que no deben ser accedidos directamente desde fuera de la clase. Se suelen nombrar con un guion bajo (_) al principio del nombre para indicar que son privados. Por ejemplo, _saldo en una clase CuentaBancaria. 
    - Atributos protegidos: Son aquellos que pueden ser accedidos desde dentro de la clase y sus subclases, pero no desde fuera de la clase. Se suelen nombrar con dos guiones bajos (__) al principio del nombre para indicar que son protegidos. Por ejemplo, __saldo en una clase CuentaBancaria.    
    - Métodos públicos: Son aquellos que pueden ser accedidos desde fuera de la clase. Se utilizan para interactuar con los atributos privados o protegidos de la clase. Por ejemplo, depositar, retirar y obtener_saldo en una clase CuentaBancaria.   
    - Metodo getter: Es un método público que se utiliza para obtener el valor de un atributo privado o protegido. Por ejemplo, get_saldo en una clase CuentaBancaria.
    - Metodo setter: Es un método público que se utiliza para establecer el valor de un atributo privado o protegido. Por ejemplo, depositar y retirar en una clase CuentaBancaria. 
    - get() es un método público que se utiliza para obtener el valor de un atributo privado o protegido. Por ejemplo, get_saldo en una clase CuentaBancaria.   
    - set() es un método público que se utiliza para establecer el valor de un atributo privado o protegido. Por ejemplo, set_saldo en una clase CuentaBancaria.    

### Aquí hay un ejemplo de cómo se puede implementar el encapsulamiento en Python:

```python
    class CuentaBancaria:
        def __init__(self, titular, saldo_inicial=0):
            self.titular = titular
            self._saldo = saldo_inicial  # Atributo privado

        def depositar(self, cantidad):
            if cantidad > 0:
                self._saldo += cantidad
                print(f"Depósito exitoso. Nuevo saldo: {self._saldo}")
            else:
                print("La cantidad a depositar debe ser positiva.")

        def retirar(self, cantidad):
            if 0 < cantidad <= self._saldo:
                self._saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: {self._saldo}")
            else:
                print("Cantidad inválida o saldo insuficiente.")

        def obtener_saldo(self):
            return self._saldo
```
-  Uso de la clase CuentaBancaria
    ```python
    cuenta = CuentaBancaria("Juan Pérez", 1000)
    cuenta.depositar(500)  # Depósito exitoso. Nuevo saldo: 1500
    cuenta.retirar(200)    # Retiro exitoso. Nuevo saldo: 1300
    cuenta.obtener_saldo()  # Devuelve 1300
    ```
    - En este ejemplo, el atributo _saldo es privado y no debe ser accedido directamente desde fuera de la clase. En su lugar, se proporcionan métodos públicos como depositar, retirar y obtener_saldo para interactuar con el saldo de la cuenta bancaria. Esto permite controlar cómo se accede y modifica el saldo, protegiendo los datos internos de la clase. 

    - Es importante destacar que, aunque el encapsulamiento es una buena práctica para proteger los datos y mantener la integridad de una clase, en Python no hay una forma estricta de hacer que un atributo o método sea completamente privado. Por lo tanto, es responsabilidad del programador seguir las convenciones de nomenclatura y respetar la intención de encapsulamiento al diseñar sus clases.    

### Definicion de clase coche con atributos privados y métodos públicos
```python
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca  # Atributo publico
        self._modelo = modelo  # Atributo protegido
        self.__color = color  # Atributo privado

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self._modelo

    def get_color(self):
        return self.__color
    
# Uso de la clase Coche
coche1 = Coche("Toyota", "Corolla", "Rojo")
# No podemos acceder directamente a los atributos protegidos o privados desde fuera de la clase
coche1.marca = "Honda"  # Esto es posible porque marca es un atributo público
coche1._modelo = "Civic"  # Esto no es recomendable porque _modelo es un atributo protegido
coche1.__color = "Azul"  # Esto no es posible porque __color es un atributo privado

# pero podemos usar los métodos públicos para obtener su valor.
print(coche1.get_marca())  # Devuelve "Toyota"
print(coche1.get_modelo())  # Devuelve "Corolla"
print(coche1.get_color())   # Devuelve "Rojo"
```

## Property de una clase coche con atributos privados y métodos públicos para acceder a ellos
- una forma más elegante de implementar getters y setters en Python es utilizando la función property, que permite definir métodos para acceder y modificar los atributos de una clase de manera más sencilla y legible.
- property es una función incorporada en Python que se utiliza para crear propiedades de clase. Permite definir métodos para acceder y modificar los atributos de una clase de manera más sencilla y legible, sin necesidad de escribir métodos getter y setter explícitos. 
- un decorador es una función que se utiliza para modificar el comportamiento de otra función o método. En el caso de property, se utilizan decoradores para definir los métodos getter y setter de una propiedad.
- El decorador @property se utiliza para definir el método getter de una propiedad, mientras que el decorador @<nombre_de_la_propiedad>.setter se utiliza para definir el método setter de la misma propiedad. Esto permite acceder a los atributos de la clase como si fueran propiedades, sin necesidad de llamar a métodos explícitos para obtener o establecer su valor.    
```python

class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca  # Atributo protegido
        self._modelo = modelo  # Atributo protegido
        self._color = color  # Atributo protegido

    @property               # Decorador para el método getter de la propiedad marca
    def marca(self):
        return self._marca
    
    @marca.setter           # Decorador para el método setter de la propiedad marca
    def marca(self, marca):
        self._marca = marca
    
    @property               # Decorador para el método getter de la propiedad modelo
    def modelo(self):
        return self._modelo
    
    @modelo.setter          # Decorador para el método setter de la propiedad modelo
    def modelo(self, modelo):
        self._modelo = modelo
    
    @property               # Decorador para el método getter de la propiedad color
    def color(self):
        return self._color
    
    @color.setter       # Decorador para el método setter de la propiedad color
    def color(self, color):
        self._color = color
```
- Uso de la clase Coche
```python
if __name__ == "__main__":
    coche1 = Coche("Toyota", "Corolla", "Rojo")
    print(coche1.marca)  # Imprime: Toyota, 
```
- gracias al método getter definido con el decorador @property, lo que permite acceder al valor de la propiedad marca de manera sencilla. 
- Esto es posible gracias al método getter definido con el decorador @property, lo que permite acceder al valor de la 
- propiedad marca de manera sencilla. Al utilizar el decorador @property, podemos acceder a la propiedad marca como si fuera un atributo normal, sin necesidad de llamar a un método explícito para obtener su valor. Esto hace que el código sea más limpio y fácil de leer.   
```python
    print(coche1.modelo)  # Imprime: Corolla
    print(coche1.color)  # Imprime: Rojo

    coche1.marca = "Honda"   
```
- Esto es posible gracias al método setter definido con el decorador @marca.setter,lo que permite modificar el valor de la propiedad marca de manera sencilla. ya que el método setter se ha definido utilizando el decorador @marca.setter, podemos asignar un nuevo valor a la propiedad marca directamente, sin necesidad de llamar a un método explícito para establecer su valor. Esto hace que el código sea más limpio y fácil de leer.

## Atributos dinámicos de clase
- En Python, es posible agregar atributos a una clase de forma dinámica, es decir, sin necesidad de definirlos previamente en la clase. Esto se puede hacer utilizando el método `setattr()` o simplemente asignando un valor a un nuevo atributo.  
- Aquí hay un ejemplo de cómo agregar atributos dinámicos a una clase:
```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
# Crear una instancia de la clase Persona
persona1 = Persona("Juan")
# Agregar un atributo dinámico a la instancia persona1
persona1.edad = 30
print(f"{persona1.nombre} tiene {persona1.edad} años.")
# Agregar un atributo dinámico a la clase Persona   
setattr(Persona, 'nacionalidad', 'Desconocida')
```
- setattr() es una función incorporada en Python que se utiliza para establecer un atributo de un objeto. En este caso, estamos utilizando setattr() para agregar un nuevo atributo llamado 'nacionalidad' a la clase Persona y asignarle el valor 'Desconocida'. Esto significa que todas las instancias de la clase Persona tendrán acceso a este nuevo atributo.  
- Ahora todas las instancias de la clase Persona tendrán el atributo nacionalidad   
```python
persona2 = Persona("María")
print(f"{persona2.nombre} es de nacionalidad {persona2.nacionalidad}.") 
```
- En este ejemplo, hemos creado una clase `Persona` con un atributo `nombre`. Luego, hemos agregado un atributo dinámico `edad` a la instancia `persona1` y un atributo dinámico `nacionalidad` a la clase `Persona`. Esto demuestra cómo se pueden agregar atributos de forma dinámica tanto a instancias como a la clase en sí.   
- Es importante tener en cuenta que el uso de atributos dinámicos puede hacer que el código sea menos predecible y más difícil de mantener, por lo que se recomienda usarlos con precaución.    

## Decoradores de clase
- Los decoradores de clase son una forma de modificar o extender el comportamiento de una clase sin necesidad de modificar su código fuente. En Python, los decoradores de clase se pueden implementar utilizando la sintaxis de decoradores, que es similar a la de los decoradores de funciones.
### `__dict__` y `__slots__`
- En Python, `__dict__` es un atributo especial que almacena los atributos de una instancia de clase como un diccionario. Esto permite que los atributos se agreguen dinámicamente a las instancias de clase.
- `__slots__` es una declaración que se utiliza para limitar los atributos que una instancia de clase puede tener, lo que puede mejorar el rendimiento y reducir el uso de memoria.

- Ejemplo `__dict__`
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)
# Acceder a los atributos utilizando __dict__
print(persona1.__dict__)  # Esto mostrará {'nombre': 'Juan', 'edad': 30}
# Agregar un nuevo atributo dinámico
persona1.nacionalidad = "Desconocida"
print(persona1.__dict__)  # Esto mostrará {'nombre': 'Juan', 'edad': 30, 'nacionalidad': 'Desconocida'}
```
- Aquí hay un ejemplo de cómo usar un decorador de clase para agregar un método a una clase existente:
```python
def agregar_metodo(cls):
    def nuevo_metodo(self):
        return f"Hola, soy un método agregado dinámicamente a la clase {cls.__name__}"
    cls.nuevo_metodo = nuevo_metodo
    return cls  

@agregar_metodo
class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre

# Crear una instancia de MiClase
objeto = MiClase("Ejemplo")

# Llamar al método agregado dinámicamente
print(objeto.nuevo_metodo())
```
- En este ejemplo, hemos definido un decorador de clase llamado `agregar_metodo` que toma una clase como argumento y agrega un nuevo método llamado `nuevo_metodo` a esa clase. Luego, hemos aplicado el decorador a la clase `MiClase`, lo que permite que todas las instancias de `MiClase` tengan acceso al nuevo método. Al crear una instancia de `MiClase` y llamar al método agregado, podemos ver el resultado.  

- Los decoradores de clase son una herramienta poderosa para modificar el comportamiento de las clases de manera flexible y reutilizable, y se utilizan comúnmente en frameworks y bibliotecas para agregar funcionalidades adicionales a las clases sin necesidad de modificar su código fuente.  

- Aquí hay un ejemplo de cómo usar `__dict__` y `__slots__` en una clase:
```python
class Persona:
    __slots__ = ['nombre', 'edad']  # Limitar los atributos a 'nombre' y 'edad'
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad    
# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)
# Acceder a los atributos utilizando __dict__
print(persona1.__dict__)  # Esto generará un error porque __slots__ limita los atributos
```
# Agregar un nuevo atributo dinámico (esto también generará un error debido a __slots__)
```python
persona1.nacionalidad = "Desconocida"  # Esto generará un error debido a __slots__
```
- En este ejemplo, hemos definido una clase `Persona` con `__slots__` que limita los atributos a `nombre` y `edad`. Al intentar acceder a `__dict__` o agregar un nuevo atributo dinámico, se generará un error debido a la restricción impuesta por `__slots__`. Esto demuestra cómo `__slots__` puede mejorar el rendimiento al limitar los atributos de una clase, pero también limita la flexibilidad de agregar atributos dinámicos.   
- En resumen, `__dict__` permite almacenar atributos dinámicos en una instancia de clase, mientras que `__slots__` limita los atributos que una instancia puede tener, lo que puede mejorar el rendimiento pero reduce la flexibilidad. Es importante elegir entre estas opciones según las necesidades específicas de tu aplicación.   

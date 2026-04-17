# Herencia y conceptos de POO

Este archivo resume los conceptos que estás viendo en Python con ejemplos sencillos y una explicación más clara de cada uno.

## 1. Herencia

La herencia permite crear una clase nueva a partir de otra clase ya existente. La clase nueva recibe atributos y métodos de la clase padre, y además puede agregar cosas nuevas.
La clase nueva, llamada clase derivada o subclase, hereda atributos y métodos de la clase existente, llamada clase base o superclase. 

### Idea simple
- La clase padre es el molde general.
- La clase hija reutiliza ese molde y lo especializa.

### Ejemplo 1
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Sonido genérico"


class Perro(Animal):
    pass

perro = Perro("Rex")
print(perro.nombre)
print(perro.hacer_sonido())
```

### Qué pasa aquí
- `Perro` hereda de `Animal`.
- `Perro` tiene acceso al atributo `nombre`.
- `Perro` también puede usar `hacer_sonido()`.

### Ejemplo 2
```python
class Animal:       # Clase base o superclase
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def hacer_sonido(self) -> str:  # Método que puede ser sobrescrito por las clases derivadas
        return "Sonido genérico"
    
class Perro(Animal):        # Clase derivada o subclase que hereda de Animal
    def hacer_sonido(self) -> str:   # Sobrescribimos el método hacer_sonido para proporcionar una implementación específica para Perro
        return "Guau"   
    
class Gato(Animal):         # Otra clase derivada que hereda de Animal
    def hacer_sonido(self) -> str:   # Sobrescribimos el método hacer_sonido para proporcionar una implementación específica para Gato
        return "Miau"
    
# Creando instancias de las clases derivadas
perro = Perro("Rex")
gato = Gato("Mittens")
# Llamando al método hacer_sonido en las instancias de las clases derivadas
print(f"{perro.nombre} dice: {perro.hacer_sonido()}")
print(f"{gato.nombre} dice: {gato.hacer_sonido()}")
```
### Qué pasa aquí
- En este ejemplo, la clase Animal es la clase base que tiene un método hacer_sonido. Las clases Perro y Gato son clases derivadas que heredan de Animal y sobrescriben el método hacer_sonido para proporcionar sonidos específicos para cada tipo de animal. Al crear instancias de Perro y Gato y llamar al método hacer_sonido, obtenemos los sonidos correspondientes a cada animal.   
- La herencia también permite la creación de jerarquías de clases, donde una clase derivada puede a su vez ser la clase base para otra clase derivada. Esto facilita la organización del código y la reutilización de funcionalidades comunes entre diferentes clases.  
- En resumen, la herencia es una característica poderosa de la programación orientada a objetos que permite crear nuevas clases basadas en clases existentes, promoviendo la reutilización de código y facilitando la creación de jerarquías de clases. 

## 2. Sobreescritura de métodos

Sobreescribir significa redefinir un método heredado en la clase hija para que haga algo diferente.

La sobreescritura de métodos es una característica de la herencia que permite a una clase derivada proporcionar una implementación específica de un método que ya está definido en su clase base. Esto es útil cuando la clase derivada necesita un comportamiento diferente para ese método en comparación con la clase base.

Para sobrescribir un método, simplemente se define un método con el mismo nombre en la clase derivada. Cuando se llama al método en una instancia de la clase derivada, se ejecutará la implementación de ese método en la clase derivada en lugar de la implementación en la clase base.

### Ejemplo 1
```python
class Animal:
    def hacer_sonido(self):
        return "Sonido genérico"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"


gato = Gato()
print(gato.hacer_sonido())
```

### Qué pasa aquí
- `Gato` hereda de `Animal`.
- Pero `Gato` cambia el comportamiento de `hacer_sonido()`.
- Cuando llamas `gato.hacer_sonido()`, se usa el método de `Gato`, no el de `Animal`.

### Ejemplo 2
```python
class Vehiculo:       # Clase base o superclase
    def __init__(self, marca: str) -> None:
        self._marca = marca

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca: str) -> None:
        self._marca = marca

    def tipo_vehiculo(self) -> str:  # Método que puede ser sobrescrito por las clases derivadas
        return "Vehículo genérico"  
class Coche(Vehiculo):        # Clase derivada o subclase que hereda de Vehiculo
    def tipo_vehiculo(self) -> str:   # Sobrescribimos el método tipo_vehiculo para proporcionar una implementación específica para Coche
        return "Coche"
class Moto(Vehiculo):         # Otra clase derivada que hereda de Vehiculo
    def tipo_vehiculo(self) -> str:   # Sobrescribimos el método tipo_vehiculo para proporcionar una implementación específica para Moto
        return "Moto"
# Creando instancias de las clases derivadas
coche = Coche("Toyota")
moto = Moto("Honda")
# Llamando al método tipo_vehiculo en las instancias de las clases derivadas
print(f"{coche.marca} es un: {coche.tipo_vehiculo()}")
print(f"{moto.marca} es una: {moto.tipo_vehiculo()}")
```

### Qué pasa aquí
- En este ejemplo, la clase Vehiculo es la clase base que tiene un método tipo_vehiculo. Las clases Coche y Moto son clases derivadas que heredan de Vehiculo y sobrescriben el método tipo_vehiculo para proporcionar tipos específicos de vehículos. Al crear instancias de Coche y Moto y llamar al método tipo_vehiculo, obtenemos los tipos correspondientes a cada vehículo.  
- La sobreescritura de métodos es una característica importante de la herencia que permite a las clases derivadas personalizar el comportamiento de los métodos heredados, lo que facilita la creación de clases más específicas y adaptadas a sus necesidades. 

### Diferencia entre crear y sobreescribir un método
- Crear un método nuevo: agregas una función que no existía en la clase padre.
- Sobreescribir un método: usas el mismo nombre de un método ya existente en la clase padre y cambias su lógica.

## 3. Polimorfismo

El polimorfismo significa que diferentes clases pueden responder al mismo método de formas distintas.

El polimorfismo es un concepto fundamental en la programación orientada a objetos que permite a objetos de diferentes clases ser tratados como objetos de una clase común. En el contexto de la herencia, el polimorfismo se refiere a la capacidad de una clase derivada para ser tratada como una instancia de su clase base, lo que permite que el mismo código funcione con objetos de diferentes clases derivadas sin necesidad de conocer su tipo específico.

En Python, el polimorfismo se logra a través de la herencia y la sobrescritura de métodos. Cuando una clase derivada sobrescribe un método de la clase base, se puede llamar a ese método en una instancia de la clase derivada, y se ejecutará la implementación específica de esa clase derivada, incluso si el objeto se trata como una instancia de la clase base.

### Idea simple
Tú llamas al mismo método, pero cada objeto hace algo diferente.

### Ejemplo 1
```python
class Animal:
    def hacer_sonido(self):
        return "Sonido genérico"


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"


animales = [Perro("Rex"), Gato("Luna")]

for animal in animales:
    print(animal.hacer_sonido())
```

### Qué demuestra este ejemplo
- El mismo método `hacer_sonido()` se llama para varios objetos.
- Cada clase devuelve un resultado distinto.
- Eso es polimorfismo.

### Ejemplo 2
```python
class Empleado:       # Clase base o superclase
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def calcular_salario(self) -> float:  # Método que puede ser sobrescrito por las clases derivadas
        return 0.0
class EmpleadoTiempoCompleto(Empleado):        # Clase derivada o subclase que hereda de Empleado
    def calcular_salario(self) -> float:   # Sobrescribimos el método calcular_salario para proporcionar una implementación específica para EmpleadoTiempoCompleto
        return 3000.0
class EmpleadoTiempoParcial(Empleado):         # Otra clase derivada que hereda de Empleado
    def calcular_salario(self) -> float:   # Sobrescribimos el método calcular_salario para proporcionar una implementación específica para EmpleadoTiempoParcial
        return 1500.0
# Creando instancias de las clases derivadas
empleado_completo = EmpleadoTiempoCompleto("Alice")
empleado_parcial = EmpleadoTiempoParcial("Bob")
# Llamando al método calcular_salario en las instancias de las clases derivadas
print(f"{empleado_completo.nombre} gana: {empleado_completo.calcular_salario()}")
print(f"{empleado_parcial.nombre} gana: {empleado_parcial.calcular_salario()}")

```

### Qué demuestra este ejemplo
- En este ejemplo, la clase Empleado es la clase base que tiene un método calcular_salario. Las clases EmpleadoTiempoCompleto y EmpleadoTiempoParcial son clases derivadas que heredan de Empleado y sobrescriben el método calcular_salario para proporcionar cálculos específicos de salario para empleados a tiempo completo y a tiempo parcial, respectivamente. Al crear instancias de ambas clases derivadas y llamar al método calcular_salario, obtenemos los salarios correspondientes a cada tipo de empleado, demostrando el polimorfismo en la herencia.
- El polimorfismo en la herencia permite que el mismo código funcione con objetos de diferentes clases derivadas sin necesidad de conocer su tipo específico, lo que facilita la flexibilidad y la reutilización del código en la programación orientada a objetos. 

### Relación con la sobreescritura
La sobreescritura es una forma de lograr polimorfismo.

## 4. Encapsulamiento

El encapsulamiento consiste en proteger los datos de una clase y controlar cómo se accede a ellos.

En Python, normalmente se usan atributos con `_` para indicar que son internos y propiedades para acceder de forma controlada.

### Ejemplo
```python
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
```

### Qué pasa aquí
- `_nombre` es un atributo interno.
- `nombre` se maneja mediante `property`.
- Así puedes controlar lectura y escritura.

## 5. Abstracción

La abstracción consiste en mostrar solo lo importante y ocultar los detalles internos.

### Idea simple
El usuario de la clase usa métodos claros sin preocuparse por la lógica interna.

### Ejemplo
```python
class Calculadora:
    def sumar(self, a, b):
        return a + b


calc = Calculadora()
print(calc.sumar(5, 3))
```

### Qué abstrae este ejemplo
- Tú solo llamas `sumar()`.
- No necesitas saber cómo se hace la suma internamente.

## 6. Resumen rápido

| Concepto | Qué hace | Idea clave |
|---|---|---|
| Herencia | Reutiliza atributos y métodos de otra clase | Una clase hija nace de una clase padre |
| Sobreescritura | Cambia un método heredado | Mismo nombre, distinta lógica |
| Polimorfismo | Usa el mismo método en clases distintas | Un mismo llamado, distintos resultados |
| Encapsulamiento | Protege datos internos | Acceso controlado con atributos y propiedades |
| Abstracción | Oculta detalles internos | Usas lo importante, no todo el proceso |

## 7. Relación entre ellos

- La herencia permite compartir código entre clases.
- La sobreescritura permite personalizar ese código.
- El polimorfismo aparece cuando distintas clases responden de forma diferente al mismo método.
- El encapsulamiento protege los datos.
- La abstracción simplifica el uso de las clases.

## 8. Duck Typing en la herencia
El duck typing es un concepto en la programación orientada a objetos que se refiere a la capacidad de un objeto para ser tratado como un tipo específico si tiene los métodos y atributos necesarios, independientemente de su clase real. En otras palabras, si un objeto "camina como un pato y suena como un pato", entonces puede ser tratado como un pato, incluso si no es una instancia de la clase pato.
En el contexto de la herencia, el duck typing permite que objetos de diferentes clases sean tratados de manera similar si implementan los mismos métodos o atributos, sin necesidad de que esas clases estén relacionadas a través de la herencia. Esto promueve la flexibilidad y la reutilización del código, ya que no es necesario que las clases compartan una jerarquía de herencia para ser utilizadas de manera intercambiable.


### Ejemplo
```python
class Pato:       # Clase que representa un pato
    def hacer_sonido(self) -> str:
        return "Quack"

class Persona:    # Clase que representa una persona
    def hacer_sonido(self) -> str:
        return "Hola, soy una persona"

# Función que utiliza duck typing
def hacer_sonido(objeto):
    return objeto.hacer_sonido()

# Creando instancias de las clases
pato = Pato()
persona = Persona()

# Llamando a la función con objetos de diferentes clases
print(hacer_sonido(pato))     # Output: Quack
print(hacer_sonido(persona))  # Output: Hola, soy una persona
```

### Qué pasa aquí
- En este ejemplo, la función hacer_sonido acepta cualquier objeto que tenga un método hacer_sonido, independientemente de su clase. Tanto el objeto pato como el objeto persona pueden ser pasados a la función hacer_sonido, y se ejecutará el método hacer_sonido correspondiente a cada objeto, demostrando el concepto de duck typing en la herencia.
- El duck typing en la herencia permite que objetos de diferentes clases sean tratados de manera similar si implementan los mismos métodos o atributos, lo que promueve la flexibilidad y la reutilización del código en la programación orientada a objetos.   

## 9. Clase object en la herencia
- En Python, todas las clases heredan de una clase base llamada object. Esto significa que cualquier clase que definamos en Python es una subclase de object, ya sea que lo especifiquemos explícitamente o no. La clase object proporciona un conjunto de métodos y atributos básicos que están disponibles para todas las clases en Python, lo que permite la reutilización de código y la consistencia en el comportamiento de los objetos.
La clase object incluye métodos como `__str__`, `__repr__`, `__eq__`, `__hash__`, entre otros, que pueden ser sobrescritos por las clases derivadas para proporcionar una implementación específica. Además, la clase object también proporciona un método `__init__` que se puede utilizar para inicializar los atributos de una clase derivada.

- `__init__` es un método especial en Python que se llama automáticamente cuando se crea una nueva instancia de una clase. Este método se utiliza para inicializar los atributos de la instancia con valores específicos. Cuando definimos una clase, podemos sobrescribir el método `__init__` para proporcionar una implementación personalizada que se ejecute al crear una instancia de esa clase.
- `__str__` es otro método especial en Python que se utiliza para definir la representación en forma de cadena de un objeto. Cuando se llama a str() en una instancia de una clase, se ejecuta el método `__str__` para obtener una representación legible del objeto. Al sobrescribir el método `__str__`, podemos personalizar cómo se muestra un objeto cuando se convierte a una cadena.
- `__repr__` es un método especial en Python que se utiliza para definir la representación oficial de un objeto. Cuando se llama a repr() en una instancia de una clase, se ejecuta el método `__repr__` para obtener una representación detallada del objeto que puede ser utilizada para recrear el objeto. Al sobrescribir el método `__repr__`, podemos proporcionar una representación más informativa y útil de un objeto.
- `__eq__` es un método especial en Python que se utiliza para definir la igualdad entre objetos. Cuando se compara dos objetos utilizando el operador ==, se ejecuta el método `__eq__` para determinar si los objetos son considerados iguales. Al sobrescribir el método `__eq__`, podemos personalizar cómo se comparan los objetos y qué criterios se utilizan para determinar su igualdad.
- `__hash__` es un método especial en Python que se utiliza para definir el valor hash de un objeto. El valor hash es un número entero que se utiliza para identificar de manera única a un objeto en estructuras de datos como conjuntos y diccionarios. Al sobrescribir el método `__hash__`, podemos personalizar cómo se calcula el valor hash de un objeto, lo que puede ser útil para garantizar la consistencia y la eficiencia en el uso de objetos como claves en diccionarios o elementos en conjuntos.
En resumen, la clase object es la clase base de todas las clases en Python, y proporciona un conjunto de métodos y atributos básicos que están disponibles para todas las clases. Al sobrescribir métodos como `__init__`, `__str__`, `__repr__`, `__eq__`, y `__hash__`, podemos personalizar el comportamiento de nuestras clases derivadas y aprovechar la funcionalidad proporcionada por la clase object en la herencia.   

### Ejemplo
```python
class Persona:       # Clase que hereda de object
    def __init__(self, nombre: str, edad: int) -> None:  # Sobrescribimos el método __init__ para inicializar los atributos de la clase Persona
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad: int) -> None:
        self._edad = edad

    def __str__(self) -> str:  # Sobrescribimos el método __str__ para proporcionar una representación legible de la clase Persona
        return f"Persona(nombre={self._nombre}, edad={self._edad})"
    
    def __repr__(self) -> str:  # Sobrescribimos el método __repr__ para proporcionar una representación detallada de la clase Persona
        return f"Persona(nombre='{self._nombre}', edad={self._edad})"
    
    def __eq__(self, other) -> bool:  # Sobrescribimos el método __eq__ para definir la igualdad entre objetos de la clase Persona
        if isinstance(other, Persona):
            return self._nombre == other._nombre and self._edad == other._edad
        return False
    
    def __hash__(self) -> int:  # Sobrescribimos el método __hash__ para definir el valor hash de un objeto de la clase Persona
        return hash((self._nombre, self._edad))
    
# Creando instancias de la clase Persona
persona1 = Persona("Alice", 30)
persona2 = Persona("Bob", 25)
persona3 = Persona("Alice", 30)
# Imprimiendo las representaciones de las instancias de la clase Persona
print(str(persona1))  # Output: Persona(nombre=Alice, edad=30)
print(persona1)       # Output: Persona(nombre=Alice, edad=30) - Esto también llama al método __str__
print(repr(persona1)) # Output: Persona(nombre='Alice', edad=30)
# Comparando las instancias de la clase Persona
print(persona1 == persona2)  # Output: False
print(persona1 == persona3)  # Output: True
# Obteniendo el valor hash de las instancias de la clase Persona    
print(hash(persona1))  # Output: Un valor hash único para persona1
print(hash(persona2))  # Output: Un valor hash único para persona2  
print(hash(persona3))  # Output: El mismo valor hash que persona1, ya que tienen los mismos atributos
```
### Qué pasa aquí
- En este ejemplo, la clase Persona hereda de object y sobrescribe los métodos `__init__`, `__str__`, `__repr__`, `__eq__`, y `__hash__` para proporcionar una implementación personalizada. Al crear instancias de la clase Persona y llamar a estos métodos, podemos ver cómo se personaliza el comportamiento de la clase derivada utilizando la funcionalidad proporcionada por la clase object en la herencia. 

## 10. palabra clave super() en la herencia
La palabra clave super() en Python se utiliza para llamar a métodos de la clase base desde una clase derivada. Esto es especialmente útil cuando queremos extender o modificar el comportamiento de un método heredado sin tener que reescribir completamente la implementación de la clase base. La función super() devuelve un objeto temporal que permite acceder a los métodos de la clase base, lo que facilita la reutilización del código y la mantenibilidad de las clases derivadas.
- La sintaxis básica para usar super() es la siguiente:
```python
class ClaseDerivada(ClaseBase):
    def metodo(self):
        super().metodo()  # Llamada al método de la clase base
 ```
- En este ejemplo, ClaseDerivada hereda de ClaseBase y sobrescribe el método
- metodo. Dentro de la implementación del método en ClaseDerivada, se llama a super().metodo() para ejecutar la implementación del método en ClaseBase antes de agregar cualquier funcionalidad adicional específica de ClaseDerivada.

### Ejemplo
```python
class Animal:       # Clase base o superclase
    def __init__(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def hacer_sonido(self) -> str:  # Método que puede ser sobrescrito por las clases derivadas
        return "Sonido genérico"
class Perro(Animal):        # Clase derivada o subclase que hereda de Animal
    def hacer_sonido(self) -> str:   # Sobrescribimos el método hacer_sonido para proporcionar una implementación específica para Perro
        sonido_base = super().hacer_sonido()  # Llamada al método de la clase base
        return f"{sonido_base} - Guau"
# Creando una instancia de la clase Perro
perro = Perro("Rex")
# Llamando al método hacer_sonido en la instancia de la clase Perro
print(f"{perro.nombre} dice: {perro.hacer_sonido()}")  # Output: Rex dice: Sonido genérico - Guau   
```

### Qué pasa aquí
- En este ejemplo, la clase Perro hereda de la clase Animal y sobrescribe el método hacer_sonido. Dentro de la implementación del método hacer_sonido en la clase Perro, se llama a super().hacer_sonido() para obtener el sonido genérico definido en la clase base Animal, y luego se agrega el sonido específico de un perro ("Guau") a ese resultado. Al crear una instancia de la clase Perro y llamar al método hacer_sonido, obtenemos una combinación del sonido genérico y el sonido específico del perro, demostrando cómo se puede usar super() para extender el comportamiento de un método heredado en una clase derivada.
- La palabra clave super() es una herramienta poderosa en la herencia que permite a las clases derivadas reutilizar y extender el comportamiento de los métodos de la clase base, lo que facilita la creación de clases más específicas y adaptadas a sus necesidades sin tener que reescribir completamente la implementación de la clase base.    

## 11. Aplicación a tu archivo

En tu archivo [S06__01_Herencia.py](S06__01_Herencia.py), ya tienes ejemplos de:
- Herencia con `Animal`, `Perro` y `Gato`.
- Sobreescritura con `hacer_sonido()`.
- Polimorfismo con `EmpleadoTiempoCompleto` y `EmpleadoTiempoParcial` usando `calcular_salario()`.

Si quieres, el siguiente paso puede ser convertir este material en una guía todavía más limpia, con un solo ejemplo por concepto y mejor formato de estudio.
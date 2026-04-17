# Atributos dinámicos de clase
# En Python, es posible agregar atributos a una clase de forma dinámica, es decir, sin necesidad de definirlos previamente en la clase. Esto se puede hacer utilizando el método `setattr()` o simplemente asignando un valor a un nuevo atributo.  
# Aquí hay un ejemplo de cómo agregar atributos dinámicos a una clase:
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
# setattr() es una función incorporada en Python que se utiliza para establecer un atributo de un objeto. En este caso, estamos utilizando setattr() para agregar un nuevo atributo llamado 'nacionalidad' a la clase Persona y asignarle el valor 'Desconocida'. Esto significa que todas las instancias de la clase Persona tendrán acceso a este nuevo atributo.  
# Ahora todas las instancias de la clase Persona tendrán el atributo nacionalidad   
persona2 = Persona("María")
print(f"{persona2.nombre} es de nacionalidad {persona2.nacionalidad}.") 
# En este ejemplo, hemos creado una clase `Persona` con un atributo `nombre`. Luego, hemos agregado un atributo dinámico `edad` a la instancia `persona1` y un atributo dinámico `nacionalidad` a la clase `Persona`. Esto demuestra cómo se pueden agregar atributos de forma dinámica tanto a instancias como a la clase en sí.   
# Es importante tener en cuenta que el uso de atributos dinámicos puede hacer que el código sea menos predecible y más difícil de mantener, por lo que se recomienda usarlos con precaución.    

# decoradores de clase
# Los decoradores de clase son una forma de modificar o extender el comportamiento de una clase sin necesidad de modificar su código fuente. En Python, los decoradores de clase se pueden implementar utilizando la sintaxis de decoradores, que es similar a la de los decoradores de funciones.

# __dict__ y __slots__
# En Python, `__dict__` es un atributo especial que almacena los atributos de una instancia de clase como un diccionario. Esto permite que los atributos se agreguen dinámicamente a las instancias de clase. Por otro lado, `__slots__` es una declaración que se utiliza para limitar los atributos que una instancia de clase puede tener, lo que puede mejorar el rendimiento y reducir el uso de memoria.
# Aquí hay un ejemplo de cómo usar `__dict__` y `__slots__` en una clase:
class Persona:
    __slots__ = ['nombre', 'edad']  # Limitar los atributos a 'nombre' y 'edad'
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad    
# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)
# Acceder a los atributos utilizando __dict__
try:
    print(persona1.__dict__)  # Esto generará un error porque __slots__ limita los atributos
except AttributeError as error:
    print(f"Error al acceder a __dict__: {error}")
# Agregar un nuevo atributo dinámico (esto también generará un error debido a __slots__)
try:
    persona1.nacionalidad = "Desconocida"  # Esto generará un error debido a __slots__
except AttributeError as error:
    print(f"Error al agregar 'nacionalidad': {error}")
# En este ejemplo, hemos definido una clase `Persona` con `__slots__` que limita los atributos a `nombre` y `edad`. Al intentar acceder a `__dict__` o agregar un nuevo atributo dinámico, se generará un error debido a la restricción impuesta por `__slots__`. Esto demuestra cómo `__slots__` puede mejorar el rendimiento al limitar los atributos de una clase, pero también limita la flexibilidad de agregar atributos dinámicos.   
# En resumen, `__dict__` permite almacenar atributos dinámicos en una instancia de clase, mientras que `__slots__` limita los atributos que una instancia puede tener, lo que puede mejorar el rendimiento pero reduce la flexibilidad. Es importante elegir entre estas opciones según las necesidades específicas de tu aplicación.   

#ejemplo __dict__ 
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


# Aquí hay un ejemplo de cómo usar un decorador de clase para agregar un método a una clase existente:
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
# En este ejemplo, hemos definido un decorador de clase llamado `agregar_metodo` que toma una clase como argumento y agrega un nuevo método llamado `nuevo_metodo` a esa clase. Luego, hemos aplicado el decorador a la clase `MiClase`, lo que permite que todas las instancias de `MiClase` tengan acceso al nuevo método. Al crear una instancia de `MiClase` y llamar al método agregado, podemos ver el resultado.  
# Los decoradores de clase son una herramienta poderosa para modificar el comportamiento de las clases de manera flexible y reutilizable, y se utilizan comúnmente en frameworks y bibliotecas para agregar funcionalidades adicionales a las clases sin necesidad de modificar su código fuente.   

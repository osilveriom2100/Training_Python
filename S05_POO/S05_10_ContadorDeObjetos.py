# Contador de objetos
class Persona:
    contador_personas= 0

    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        Persona.contador_personas += 1
        self._id = Persona.contador_personas

    def mostrar_informacion(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, ID: {self._id}")

    @staticmethod
    def mostrar_contador():
        print(f"Total de personas creadas: {Persona.contador_personas}")

    @classmethod
    def get_contador(cls):
        return cls.contador_personas
    
persona1 = Persona("Juan", 30)
persona1.mostrar_informacion()
persona2 = Persona("Maria", 25)
persona2.mostrar_informacion()
Persona.mostrar_contador()
print(f"Contador desde el método de clase: {Persona.get_contador()}")
print(f"Contador desde la instancia: {persona1.get_contador()}")
# El código define una clase Persona con un contador de personas creado como una variable de clase. Cada vez que se crea una nueva instancia de Persona, el contador se incrementa automáticamente. La clase también incluye métodos para mostrar la información de la persona, mostrar el contador total de personas creadas y obtener el valor actual del contador a través de un método de clase. Al final del código, se crean dos instancias de Persona, se muestra su información y se muestra el contador total utilizando tanto el método estático como el método de clase. 

# Contexto dinámico de la clase, el contador se incrementa cada vez que se crea una nueva instancia de Persona. El método estático mostrar_contador() permite mostrar el número total de personas creadas, mientras que el método de clase get_contador() devuelve el valor actual del contador.
# contexto estatico de la clase, el contador_personas es una variable de clase que se comparte entre todas las instancias de la clase Persona. Cada vez que se crea una nueva instancia, el contador se incrementa, lo que permite llevar un registro del número total de personas creadas.
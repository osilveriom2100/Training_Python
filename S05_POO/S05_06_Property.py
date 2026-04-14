# Property de una clase coche con atributos privados y métodos públicos para acceder a ellos
# una forma más elegante de implementar getters y setters en Python es utilizando la función property, que permite definir métodos para acceder y modificar los atributos de una clase de manera más sencilla y legible.
# property es una función incorporada en Python que se utiliza para crear propiedades de clase. Permite definir métodos para acceder y modificar los atributos de una clase de manera más sencilla y legible, sin necesidad de escribir métodos getter y setter explícitos. 
# un decorador es una función que se utiliza para modificar el comportamiento de otra función o método. En el caso de property, se utilizan decoradores para definir los métodos getter y setter de una propiedad.
# El decorador @property se utiliza para definir el método getter de una propiedad, mientras que el decorador @<nombre_de_la_propiedad>.setter se utiliza para definir el método setter de la misma propiedad. Esto permite acceder a los atributos de la clase como si fueran propiedades, sin necesidad de llamar a métodos explícitos para obtener o establecer su valor.    

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

# Uso de la clase Coche
if __name__ == "__main__":
    coche1 = Coche("Toyota", "Corolla", "Rojo")
    print(coche1.marca)  # Imprime: Toyota, 
    #gracias al método getter definido con el decorador @property, lo que permite acceder al valor de la propiedad marca 
    # de manera sencilla. 
    # Esto es posible gracias al método getter definido con el decorador @property, lo que permite acceder al valor de la 
    # propiedad marca de manera sencilla. Al utilizar el decorador @property, podemos acceder a la propiedad marca como si 
    # fuera un atributo normal, sin necesidad de llamar a un método explícito para obtener su valor. Esto hace que el código 
    # sea más limpio y fácil de leer.   
    print(coche1.modelo)  # Imprime: Corolla
    print(coche1.color)  # Imprime: Rojo

    coche1.marca = "Honda"      
    # Esto es posible gracias al método setter definido con el decorador @marca.setter, 
    # lo que permite modificar el valor de la propiedad marca de manera sencilla. ya que el método setter se ha definido 
    # utilizando el decorador @marca.setter, podemos asignar un nuevo valor a la propiedad marca directamente, sin necesidad 
    # de llamar a un método explícito para establecer su valor. Esto hace que el código sea más limpio y fácil de leer.
    coche1.modelo = "Civic"
    coche1.color = "Azul"

    print(coche1.marca)  # Imprime: Honda
    print(coche1.modelo)  # Imprime: Civic
    print(coche1.color)  # Imprime: Azul
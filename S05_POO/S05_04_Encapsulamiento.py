# Encapsulamiento
# El encapsulamiento es un principio fundamental de la programación orientada a objetos que se refiere a la ocultación de los detalles internos de una clase y la exposición de una interfaz pública para interactuar con esa clase. Esto permite proteger los datos y métodos internos de una clase, evitando que sean accedidos o modificados directamente desde fuera de la clase.   
# En Python, el encapsulamiento se logra utilizando convenciones de nomenclatura para indicar que ciertos atributos o métodos son privados. Por ejemplo, se puede usar un guion bajo (_) antes del nombre de un atributo o método para indicar que es privado y no debe ser accedido directamente desde fuera de la clase. Sin embargo, es importante destacar que esto es solo una convención y no impide realmente el acceso a esos atributos o métodos.
# Para aplicar el encapsulamiento de manera efectiva, se pueden proporcionar métodos públicos (también conocidos como getters y setters) para acceder y modificar los atributos privados de una clase. Esto permite controlar cómo se accede a los datos internos de la clase y garantiza que se mantenga la integridad de esos datos.  
# Atributos privados: Son aquellos que no deben ser accedidos directamente desde fuera de la clase. Se suelen nombrar con un guion bajo (_) al principio del nombre para indicar que son privados. Por ejemplo, _saldo en una clase CuentaBancaria. 
# Atributos protegidos: Son aquellos que pueden ser accedidos desde dentro de la clase y sus subclases, pero no desde fuera de la clase. Se suelen nombrar con dos guiones bajos (__) al principio del nombre para indicar que son protegidos. Por ejemplo, __saldo en una clase CuentaBancaria.    
# Métodos públicos: Son aquellos que pueden ser accedidos desde fuera de la clase. Se utilizan para interactuar con los atributos privados o protegidos de la clase. Por ejemplo, depositar, retirar y obtener_saldo en una clase CuentaBancaria. 
# Metodo getter: Es un método público que se utiliza para obtener el valor de un atributo privado o protegido. Por ejemplo, get_saldo en una clase CuentaBancaria.
# get() es un método público que se utiliza para obtener el valor de un atributo privado o protegido. Por ejemplo, get_saldo en una clase CuentaBancaria.   
# set() es un método público que se utiliza para establecer el valor de un atributo privado o protegido. Por ejemplo, set_saldo en una clase CuentaBancaria.    
# Metodo setter: Es un método público que se utiliza para establecer el valor de un atributo privado o protegido. Por ejemplo, depositar y retirar en una clase CuentaBancaria. 



# Aquí hay un ejemplo de cómo se puede implementar el encapsulamiento en Python:
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
# Uso de la clase CuentaBancaria
cuenta = CuentaBancaria("Juan Pérez", 1000)
cuenta.depositar(500)  # Depósito exitoso. Nuevo saldo: 1500
cuenta.retirar(200)    # Retiro exitoso. Nuevo saldo: 1300
cuenta.obtener_saldo()  # Devuelve 1300
# En este ejemplo, el atributo _saldo es privado y no debe ser accedido directamente desde fuera de la clase. En su lugar, se proporcionan métodos públicos como depositar, retirar y obtener_saldo para interactuar con el saldo de la cuenta bancaria. Esto permite controlar cómo se accede y modifica el saldo, protegiendo los datos internos de la clase. 
# Es importante destacar que, aunque el encapsulamiento es una buena práctica para proteger los datos y mantener la integridad de una clase, en Python no hay una forma estricta de hacer que un atributo o método sea completamente privado. Por lo tanto, es responsabilidad del programador seguir las convenciones de nomenclatura y respetar la intención de encapsulamiento al diseñar sus clases.    

# Definicion de clase coche con atributos privados y métodos públicos
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
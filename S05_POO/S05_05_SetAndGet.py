# clase coche con atributos privados y métodos públicos para acceder a ellos
class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca  # Atributo protegido
        self._modelo = modelo  # Atributo protegido
        self._color = color  # Atributo protegido

    def set_marca(self, marca):
        self._marca = marca

    def get_marca(self):
        return self._marca
    
    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_modelo(self):
        return self._modelo
    
    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color
    
# Uso de la clase Coche
if __name__ == "__main__":
    coche1 = Coche("Toyota", "Corolla", "Rojo")
    print(coche1.get_marca())  # Imprime: Toyota
    print(coche1.get_modelo())  # Imprime: Corolla
    print(coche1.get_color())  # Imprime: Rojo

    coche1.set_marca("Honda")
    coche1.set_modelo("Civic")
    coche1.set_color("Azul")

    print(coche1.get_marca())  # Imprime: Honda
    print(coche1.get_modelo())  # Imprime: Civic
    print(coche1.get_color())  # Imprime: Azul
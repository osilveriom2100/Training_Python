# Clase de aritmetica con métodos getter y setter
class Aritmetica:
    def __init__(self, operador1=None, operador2=None):
        self._operador1 = operador1
        self._operador2 = operador2

    @property
    def operador1(self):
        return self._operador1

    @operador1.setter
    def operador1(self, operador1):
        self._operador1 = operador1

    @property
    def operador2(self):
        return self._operador1

    @operador2.setter
    def operador2(self, operador2):
        self._operador2 = operador2

    def sumar(self):
        return self._operador1 + self._operador2
    
    def restar(self):
        return self._operador1 - self._operador2
    
    def multiplicar(self):
        return self._operador1 * self._operador2
    
    def dividir(self):
        if self._operador2 == 0:
            return 0
        else:
            return self._operador1 / self._operador2
        
if __name__ == "__main__":
    aritmetica1 = Aritmetica()
    aritmetica1.operador1 = 2
    aritmetica1.operador2 = 2

    print(f"Suma: {aritmetica1.sumar()}")
    print(f"Resta: {aritmetica1.restar()}")
    print(f"Multiplicación: {aritmetica1.multiplicar()}")
    print(f"División: {aritmetica1.dividir()}")

from S05_POO.S05_14_Herencia.monitor import Monitor
from S05_POO.S05_14_Herencia.teclado import Teclado
from S05_POO.S05_14_Herencia.raton import Raton

class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre: str = None, monitor: Monitor = None, teclado : Teclado = None, raton: Raton = None)-> None:
        Computadora.contador_computadoras += 1
        self._id_computador = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor
    
    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado
    
    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton
    
    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f"ID {self._id_computador}, nombre: {self._nombre}, monitor: {self._monitor}, teclado: {self._teclado}, raton: {self._raton}"
    
if __name__ == '__main__':
    raton1= Raton()
    raton1.tipo_entrada = "BB"
    raton1.marca = "Dell"
    print(str(raton1))
    teclado1 = Teclado()
    teclado1.tipo_entrada = "C"
    teclado1.marca = "Samsung"
    print(str(teclado1))
    monitor1 = Monitor()
    monitor1.marca = "Dell"
    monitor1.tamanio = "24 pulgadas"
    print(str(monitor1))
    computadora1 = Computadora()
    computadora1.raton = raton1
    computadora1.teclado = teclado1
    computadora1.monitor = monitor1
    computadora1.nombre = "HP"
    print(computadora1)
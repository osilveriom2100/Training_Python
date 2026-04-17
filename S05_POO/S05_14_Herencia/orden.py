from S05_POO.S05_14_Herencia.computadora import Computadora
from S05_POO.S05_14_Herencia.monitor import Monitor
from S05_POO.S05_14_Herencia.teclado import Teclado
from S05_POO.S05_14_Herencia.raton import Raton 

class Orden:
    contador_ordenes = 0
    def __init__(self, computadoras: list[Computadora] | Computadora | None = None):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        if computadoras is None:
            self._computadoras = []
        elif isinstance(computadoras, Computadora):
            self._computadoras = [computadoras]
        else:
            self._computadoras = list(computadoras)

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += str(computadora) + '\n'
        return f"Orden: {self._id_orden} \nComputadoras: \n{computadoras_str}"
    
if __name__ == '__main__':
    orden1 = Orden()
    monitor1 = Monitor('Dell', '24 pulgadas')
    teclado1 = Teclado('Samsung', 'C')
    raton1 = Raton('Dell', 'BB')
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    monitor2 = Monitor('Lenovo', '27 pulgadas')
    teclado2 = Teclado('USB', 'Logitech')
    raton2 = Raton('Logitech', 'USB')
    computadora2 = Computadora('Dell', monitor2, teclado2, raton2)
    orden1.agregar_computadora(computadora1)
    orden1.agregar_computadora(computadora2)
    print(orden1)
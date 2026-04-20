class Monitor:
    contador_monitores = 0
    def __init__(self, marca: str = None, tamanio: str = None) -> None:
        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._tamanio = tamanio
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamanio(self):
        return self._tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

    def __str__(self):
        return f"ID {self._id_monitor} marca: {self._marca} tamaño: {self._tamanio}"
    
if __name__ == '__main__':
    monitor_1 = Monitor()
    monitor_1.marca = 'Dell'
    monitor_1.tamanio = '15 pulgadas'
    print(monitor_1)
    monitor_2 = Monitor('HP', '20 pulgadas')
    print(monitor_2)
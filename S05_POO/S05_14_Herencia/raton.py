
from S05_POO.S05_14_Herencia.dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca: str = None, tipo_entrada: str = None)-> None:
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f"ID {self._id_raton} marca: {self._marca} tipo de entrada {self._tipo_entrada}"
    
if __name__ == '__main__':
    raton_1 = Raton()
    raton_1.marca = 'Dell'
    raton_1.tipo_entrada = 'USB_c'
    print(raton_1)
    raton_2 = Raton('HP', 'USB')
    print(raton_2)

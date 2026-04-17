
from S05_POO.S05_14_Herencia.dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca: str = None, tipo_entrada: str = None):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f"ID {self._id_teclado} marca: {self._marca} tipo de entrada {self._tipo_entrada}"
    
if __name__ == '__main__':
    teclado_1 = Teclado()
    teclado_1.marca = 'Dell'
    teclado_1.tipo_entrada = 'USB_c'
    print(teclado_1)
    teclado_2 = Teclado('HP', 'USB')
    print(teclado_2)
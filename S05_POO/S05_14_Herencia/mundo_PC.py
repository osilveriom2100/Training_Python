from S05_POO.S05_14_Herencia.computadora import Computadora
from S05_POO.S05_14_Herencia.monitor import Monitor
from S05_POO.S05_14_Herencia.teclado import Teclado
from S05_POO.S05_14_Herencia.raton import Raton
from S05_POO.S05_14_Herencia.orden import Orden

def main():
    raton1= Raton()
    raton1.tipo_entrada = "BB"
    raton1.marca = "Dell"
    raton2= Raton()
    raton2.tipo_entrada = "USB"
    raton2.marca = "Logitech"
    teclado1 = Teclado()
    teclado1.tipo_entrada = "C"
    teclado1.marca = "Samsung"
    print(str(raton1))
    print(str(raton2))
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
    print(str(computadora1))   
    computadora2 = Computadora()
    computadora2.raton = raton2
    computadora2.teclado = teclado1
    computadora2.monitor = monitor1
    computadora2.nombre = "Lenovo"
    print(str(computadora2))
    orden1 = Orden()
    orden1.agregar_computadora(computadora1)
    orden1.agregar_computadora(computadora2)
    print(orden1)

if __name__ == "__main__":
    main()
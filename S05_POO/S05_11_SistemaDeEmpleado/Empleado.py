class Empleado:
    contador_de_empleado = 0
    def __init__(self, nombre=None, departamento=None):
        self._nombre = nombre
        self._departamento = departamento
        Empleado.contador_de_empleado += 1

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento
    
    @classmethod
    def total_empleados(cls):
        return cls.contador_de_empleado
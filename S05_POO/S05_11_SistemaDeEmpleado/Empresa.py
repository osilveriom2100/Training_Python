from .Empleado import Empleado

class Empresa:
    def __init__(self, nombre=None, empleados=None):
        self._nombre = nombre
        self._empleados = []

    def contratar_empleado(self, empleado):
        self._empleados.append(empleado)

    def mostrar_emplados(self):
        for persona in self._empleados:
            print(persona.nombre)
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def get_numero_empleado_por_departamento(self, departamento=None):
        if departamento is None:
            return 0
        count = 0
        for empleado in self._empleados:
            if empleado.departamento == departamento:
                count += 1
        return count

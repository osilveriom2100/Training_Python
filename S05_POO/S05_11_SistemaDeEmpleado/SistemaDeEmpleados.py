from .Empleado import Empleado
from .Empresa import Empresa

# Sistema de agregacion de empleados a una empresa
if __name__ == "__main__":
    empleado1 = Empleado("Juan", "Salud")
    empleado2 = Empleado("Luis", "Docente")
    empleado3 = Empleado("Victor", "Salud")
    empleado4 = Empleado("Fer", "Ingeniero")

    print(empleado1.departamento)
    empresa1 = Empresa("Empresa 1")
    empresa1.contratar_empleado(empleado1)
    empresa1.contratar_empleado(empleado2)
    empresa1.contratar_empleado(empleado3)
    empresa1.contratar_empleado(empleado4)
    print(f"Empleados en la empresa {empresa1.nombre}:")
    empresa1.mostrar_emplados()
    print(f"Empleados en el departamento de Salud: {empresa1.get_numero_empleado_por_departamento('Salud')}")
    print(f"Total de empleados: {Empleado.total_empleados()}")

# Atributos de clase e instancia
# Atributo de clase: Compartido por todas las instancias de la clase. Se define dentro de la clase pero fuera de cualquier método.
# Atributo de instancia: Específico para cada instancia de la clase. Se define dentro del método __init__ y se accede a través de self.

class Persona:
    # Atributo de clase
    especie = "Humano"

    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad

# Crear instancias de Persona
persona1 = Persona("Alice", 30)
persona2 = Persona("Bob", 25)
# Acceder a atributos de clase
print(f"{persona1.nombre} es un {persona1.especie}.")
print(f"{persona2.nombre} es un {persona2.especie}.")
# Modificar el atributo de clase
Persona.especie = "Humanoide"
print(f"{persona1.nombre} ahora es un {persona1.especie}.")
print(f"{persona2.nombre} ahora es un {persona2.especie}.")
# Acceder a atributos de instancia
print(f"{persona1.nombre} tiene {persona1.edad} años.")
print(f"{persona2.nombre} tiene {persona2.edad} años.")
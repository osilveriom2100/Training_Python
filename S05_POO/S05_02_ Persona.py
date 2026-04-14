# Clases y Objetos en Python

# Ejemplo de una clase en Python:
class Persona:
    def __init__(self, nombre, apellido):   
        self.nombre = nombre                
        self.apellido = apellido   

    def presentarse(self):
        print(f'Dirección de memoria de self: {id(self)}')  
        return f"Hola, mi nombre es {self.nombre} {self.apellido}."
    
    def presentarse_con_id(self):
        print(f'Dirección de memoria de self: {id(self)}')
        return f"Hola, mi nombre es {self.nombre} {self.apellido}."
    
if __name__ == "__main__":
    persona1 = Persona("Juan", "Pérez")
    print(persona1.presentarse())  
    print(persona1.presentarse_con_id())
    
    persona2 = Persona("María", "Gómez")
    print(persona2.presentarse())  
    print(persona2.presentarse_con_id())

    print(f"Dirección de memoria de persona1: {id(persona1)}")
    print(f"Dirección de memoria de persona2: {id(persona2)}")


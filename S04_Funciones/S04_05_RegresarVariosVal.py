print("Return varios valores en una funcion")

# Definir una funcion que retorna varios valores
def persona_mayusculas(nombre, apellido, edad):
    print('Regresa varios valores como una tupla')
    return nombre.upper(), apellido.upper(), edad


# Llamar a la funcion y almacenar los valores retornados en variables
nombre_mayus, apellido_mayus, edad = persona_mayusculas("Juan", "Perez", 30)    
print(f"Nombre: {nombre_mayus}, Apellido: {apellido_mayus}, Edad: {edad}")

# Otra forma de llamar a la funcion y almacenar los valores retornados en una tupla
persona_info = persona_mayusculas("Maria", "Gomez", 25)
print(f'la variable persona_info es de tipo: {type(persona_info)}')
print(f"Nombre: {persona_info[0]}, Apellido: {persona_info[1]}, Edad: {persona_info[2]}")


print("funcion con argumentos nombrados")

def imprimir_info(nombre, apellido='', edad=0):
    print(f"Nombre: {nombre}", end=", ")
    print(f"Apellido: {apellido}", end=", ")
    print(f"Edad: {edad}")

# llamar a la funcion con argumentos por posicion
imprimir_info("Juan", "Perez", 30)
# llamar a la funcion con argumentos nombrados
imprimir_info(nombre="Maria", apellido="Gomez", edad=25)
# llamar a la funcion con argumentos nombrados en diferente orden
imprimir_info(edad=40, nombre="Carlos", apellido="Lopez")
# Argumentos con valores por defecto
imprimir_info(nombre="Ana")
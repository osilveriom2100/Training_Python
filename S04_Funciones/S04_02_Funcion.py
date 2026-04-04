# Defenir funcion
def saludar():
    print("Hola, bienvenido a Python")
# Llamar a la funcion
saludar()

# funcion con parametros
def saludar(mensaje):
    print(mensaje)

saludar("Hola, Funcion con parametros")

# funcion con parametros opcionales, se le asigna un valor por defecto al parametro  
def saludar(mensaje="Hola, No agrege un mensaje"):
    print(mensaje)
saludar()
saludar("Hola, Funcion con parametro opcional")

# funcion con retorno
def sumar(a, b):
    return a + b
resultado = sumar(5, 3)
print("El resultado de la suma es:", resultado)

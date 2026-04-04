print(f'Obtener coordenadas de los tres ejes en un espacio tridimensional')

def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z

# llamar a la funcion
resultado = obtener_coordenadas()
print(f'Las coordenadas son: {resultado}')

# unpacking de tuplas
x1, y1, z1 = resultado
print(f'Coordenada x= {x1}, Coordenada y= {y1}, Coordenada z= {z1}')
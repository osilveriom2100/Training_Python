## Playlist canceciones

# crearomos lista vacia
lista_de_reproduccion = []

# Agregar lista
lista_de_reproduccion.append('Hotel california - Eagles')
lista_de_reproduccion.append('Staying  Alive - Bee Gees')
lista_de_reproduccion.append('Dream on - Aerosmith')

# 
numero_de_canciones = int(input("Cuanas cancionesquieres"))
for i in range(numero_de_canciones):
    lista_de_reproduccion.append(input('Agrega la cancion'))


# Ordenar listaen orden alfabetico
lista_de_reproduccion.sort()

# Mostrar lista de eproduccion 
print(f'Lista de reproduccion')
print(f'{lista_de_reproduccion}')

# Lista
for cancion in lista_de_reproduccion:
    print(f'{cancion}')
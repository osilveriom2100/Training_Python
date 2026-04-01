print("Manejo de tuplas")

mi_tupla = (1,2,3,4,5)
print(mi_tupla)

# Iterar tupla
for elemento in mi_tupla:
    print(elemento, end=' ')

# unpacking, asignar cada elemento de la tupla a una variable
a, b, c, d, e = mi_tupla
print(f'\na: {a}, b: {b}, c: {c}, d: {d}, e: {e}')

productos = ('Salon', 'carro', 20, True)
lugar_de_casa, tipo_de_transporte, numero_de_habitantes, tiene_garaje = productos
print(f'Lugar de casa: {lugar_de_casa}, tipo de transporte: {tipo_de_transporte}, numero de habitantes: {numero_de_habitantes}, tiene garaje: {tiene_garaje}')

# los argumentos variables se pueden usar para pasar un número variable de argumentos a una función
# se pueden usar para pasar un número variable de argumentos a una función
# hay dos formas de usar los argumentos variables:
# *args: se usa para pasar un número variable de argumentos posicionales a una función , recibe una tupla con los argumentos pasados
# **kwargs: se usa para pasar un número variable de argumentos con nombre a una función, recibe un diccionario con los argumentos pasados   
# se pueden usar ambos argumentos variables en la misma función, pero *args debe ir antes de **kwargs
# kwargs significa keyword arguments, es decir argumentos con nombre 
# ejemplo de uso de *args
def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'superheroe: {superheroe} - nombre: {nombre} - superpoderes: {args}')

# se pueden pasar cualquier número de argumentos posicionales a la función
superheroe_superpoderes('superman', 'clark kent', 'vuelo', 'super fuerza', 'visión de rayos x')

# ejemplo de uso *arg como primero argumento variable
def superheroe_superpoderes(*args, nombre):
    print(f'superpoderes: {args} - nombre: {nombre}')
    for superpoder in args:
        print(f'superpoder: {superpoder}')
# se pueden pasar cualquier número de argumentos posicionales a la función, pero el argumento con nombre debe ir al final 
# y se debe especificar el nombre del argumento con nombre al llamar a la función ya que es un argumento con nombre
# en caso de usar *args como primer argumento variable, se deben pasar los argumentos posicionales antes del argumento con nombre
superheroe_superpoderes('vuelo', 'super fuerza', 'visión de rayos x', nombre='clark kent')

# ejemplo de uso de **kwargs
def superheroe_superpoderes(nombre, **kwargs):
    print(f'superheroe: {nombre} - superpoderes: {kwargs}')
    for superpoder, descripcion in kwargs.items():
        print(f'superpoder: {superpoder} - descripcion: {descripcion}')

# se pueden pasar cualquier número de argumentos con nombre a la función, pero el argumento con nombre debe ir al principio
# y se debe especificar el nombre del argumento con nombre al llamar a la función ya que es un argumento con nombre
superheroe_superpoderes(nombre='clark kent', vuelo='puede volar a gran velocidad', super_fuerza='tiene una fuerza sobrehumana', vision_rayos_x='puede ver a través de objetos sólidos')



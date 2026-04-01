print("Agenda de contactos")

agenda = {} # creamos un diccionario vacio para almacenar los contactos
print(f'Agenda de contactos: {agenda}')

while True:
    try:
        numero_contantos = int(input('Cuantos contactos deseas agregar?: '))
        if numero_contantos < 0:
            print('Error: no puedes ingresar un numero negativo.')
            continue
        break
    except ValueError:
        print('Error: debes ingresar un numero entero.')

for i in range(numero_contantos):
    nombre = input('Ingresa el nombre del contacto: ')
    if nombre in agenda:    # verificamos si el contacto ya existe en la agenda utilizando la clave del diccionario
        print(f'El contacto {nombre} ya existe')
    else:
        telefono = input('Ingresa el telefono del contacto: ')
        email = input('Ingresa el email del contacto: ')
        agenda[nombre] = {'telefono': telefono, 'email': email}

print(f'Agenda de contactos: {agenda}')

# para eliminar un contacto de la agenda, podemos utilizar la clave del diccionario para eliminar el par clave-valor asociado a ese contacto
nombre_eliminar = input('Ingresa el nombre del contacto a eliminar: ')
if nombre_eliminar in agenda:
    del agenda[nombre_eliminar] # eliminamos el contacto utilizando la clave del diccionario
    print(f'El contacto {nombre_eliminar} ha sido eliminado.')
else:    print(f'El contacto {nombre_eliminar} no existe en la agenda.')


# para accedar al telefono o email de un contacto especifico, podemos utilizar la clave del diccionario para obtener el valor asociado a esa clave
nombre_contacto = input('Ingresa el nombre del contacto para obtener su informacion: ')
if nombre_contacto in agenda:
    print(f'Telefono: {agenda[nombre_contacto]["telefono"]}')
    print(f'Email: {agenda.get(nombre_contacto).get("email")}')

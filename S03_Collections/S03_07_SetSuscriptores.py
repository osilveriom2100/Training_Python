print('lista de suscriptores')

suscriptores = set() # creamos un conjunto vacio para almacenar los suscriptores
print(f'lista de suscriptores: {suscriptores}')

numero_suscriptores = int(input('Cuantos suscriptores deas agregar?'))

for _ in range(numero_suscriptores):
    correo = input('Ingresa el correo del suscriptor')
    if correo in suscriptores:
        print(f'el suscriptor {correo} ya existe')
    else:
        suscriptores.add(correo)
        print(f'suscriptor {correo} agregado a la lista')

print(f'lista de suscriptores: {suscriptores}')

eliminar_suscriptor = input('Ingresa el correo del suscriptor a eliminar')

if eliminar_suscriptor in suscriptores:
    suscriptores.remove(eliminar_suscriptor)
    print(f'suscriptor {eliminar_suscriptor} eliminado de la lista')
else:
    print(f'El suscriptor {eliminar_suscriptor} no existe')



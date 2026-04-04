inventario = [{'ID': 1, 'Nombre': 'Playera', 'Precio': 100.0, 'Cantidad': 20},
            {'ID': 2, 'Nombre': 'Pantalon', 'Precio': 158.0, 'Cantidad': 10},
            {'ID': 3, 'Nombre': 'Sudadera', 'Precio': 230.0, 'Cantidad': 30}]

def menu():
    print(' ##### Menu #####')
    print('\t 1. Mostrar inventario')
    print('\t 2. Agregar nuevo inventario')
    print('\t 3. Buscar producto')
    print('\t 4. Salir')

def formatear_producto(producto):
    return f"ID: {producto['ID']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Cantidad: {producto['Cantidad']}"

def mostrar_inventario():
    print('Inventario:')
    for producto in inventario:
        print(formatear_producto(producto))

def agregar_inventario():
    try:
        nombre_producto = input('Ingresa el nombre del producto: ')
        if any(producto['Nombre'] == nombre_producto for producto in inventario):
            print('Error: El nombre del producto ya existe en el inventario.')
            return
        id_producto = len(inventario) + 1
        precio_producto = float(input('Ingresa el precio del producto: '))
        cantidad_producto = int(input('Ingresa la cantidad del producto: '))
        nuevo_producto = {'ID': id_producto, 'Nombre': nombre_producto, 'Precio': precio_producto, 'Cantidad': cantidad_producto}
        inventario.append(nuevo_producto)
        print('Producto agregado al inventario.')
    except ValueError:
        print('Error: Debes ingresar un valor numérico válido para Precio y Cantidad.')

def buscar_producto_id():
    try:
        id_producto = int(input('Ingresa el ID del producto a buscar: '))
        for producto in inventario:
            if producto['ID'] == id_producto:
                print(f'Producto encontrado: {formatear_producto(producto)}')
                return
        print('Producto no encontrado en el inventario.')
    except ValueError:
        print('Error: Debes ingresar un número entero válido para el ID del producto.')

# programa principal
if __name__ == "__main__":
    while True:
        menu()
        try:
            opcion = int(input('Selecciona la opcion: '))
            if opcion <= 0:
                print('Opcion no encontrada selecciona otra')
                continue
        except ValueError:
            print('Error: debes ingresar un numero entero.')
            continue

        match opcion:
            case 1:
                mostrar_inventario()
            case 2:
                agregar_inventario()
            case 3:
                buscar_producto_id()
            case 4:
                print('Saliendo del programa...')
                break   
            case _ :
                print("Opcion invalida")
    


# def mostar_inventario():
#     for persona in inventario:
#         print(f'ID: {persona['ID']}, Nombre: {persona['Nombre']} Precio: {persona['Precio']},  Cantidad: {persona['Cantidad']}')

# def agregar_inventario():
#     nombre = input('Nombre: ')
#     for persona in inventario:
#         if nombre.lower() in persona['Nombre'].lower():
#             print('El Objeto ya existe')
#             return
#     precio = float(input('Precio: '))
#     cantidad = int(input('Cantidad: '))
#     inventario.append({'ID': len(inventario) + 1, 'Nombre': nombre, 'Precio': precio, 'Cantidad': cantidad})

# def buscar_producto_id():
#     id = int(input('Cual ID te interasa: '))
#     for val in inventario:
#         if id == val['ID']:
#             print(f'ID: {val['ID']}, Nombre: {val['Nombre']} Precio: {val['Precio']},  Cantidad: {val['Cantidad']}')
#             return
#     print('No se encontro')

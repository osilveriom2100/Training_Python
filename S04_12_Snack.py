inventario = [{'ID': 1, 'Nombre': 'Playera', 'Precio': 100.0, 'Cantidad': 20},
            {'ID': 2, 'Nombre': 'Pantalon', 'Precio': 158.0, 'Cantidad': 10},
            {'ID': 3, 'Nombre': 'Sudadera', 'Precio': 230.0, 'Cantidad': 30}]
compra = []

def menu():
    print(' ##### Menu #####')
    print('\t 1. Mostrar snacks disponibles')
    print('\t 2. Comprar snack')
    print('\t 3. Mostrar snacks comprados')
    print('\t 4. Salir')

def formatear_producto(producto):
    return f"ID: {producto['ID']} -> {producto['Nombre']} -> {producto['Precio']}"

def mostrar_snacks():
    print('Snack disponibles:')
    for producto in inventario:
        print(formatear_producto(producto))

def comprar_snack():
    try:
        id_producto = int(input('Ingresa el Id del producto: '))
        producto_seleccionado = None
        for producto in inventario:
            if producto['ID'] == id_producto:
                producto_seleccionado = producto
                break

        if producto_seleccionado is None:
            print('Error: El ID del producto no existe en el inventario.')
            return

        compra.append(producto_seleccionado)
        print('Producto agregado a la compra.')

        inventario.remove(producto_seleccionado)
    except ValueError:
        print('Error: Debes ingresar un ID de producto entero válido.')

def mostrar_ticket():
    print('Snack comprados:')
    total = 0
    for producto in compra:
        total = total + producto['Precio']
        print(f'-{producto["Nombre"]} -> {producto["Precio"]}')
    print(f'Total a pagar: {total}')

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
                mostrar_snacks()
            case 2:
                comprar_snack()
            case 3:
                mostrar_ticket()
            case 4:
                print('Saliendo del programa...')
                break   
            case _ :
                print("Opcion invalida")
    
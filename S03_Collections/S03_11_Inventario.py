print("Inventario de productos")

inventario = [] # creamos una lista vacia para almacenar los productos

while True:
    try:
        numero_productos = int(input('Cuantos productos deseas agregar?: '))
        if numero_productos < 0:
            print('Error: no puedes ingresar un numero negativo.')
            continue
        break
    except ValueError:
        print('Error: debes ingresar un numero entero.')

for i in range(numero_productos):
    nombre = input('Ingresa el nombre del producto: ')
    
    if any(elemento['nombre'] == nombre for elemento in inventario):    # verificamos si el producto ya existe 
        #en el inventario utilizando una comprension de listas para verificar si algun diccionario en la lista 
        # de inventario tiene el mismo nombre que el producto que se esta intentando agregar
        print(f'El producto {nombre} ya existe')
    else:
        precio = float(input('Ingresa el precio del producto: '))
        cantidad = int(input('Ingresa la cantidad del producto: '))
        inventario.append({'id': len(inventario) + 1, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}) # agregamos 
        # un diccionario con el nombre y precio del producto a la lista de inventario

print(f'Inventario de productos: {inventario}')

# id del producto a impimir
id_producto = int(input('Ingresa el id del producto para obtener su informacion: '))
producto_encontrado = False

for producto in inventario:
    print(f'Producto: {producto}')
    if producto['id'] == id_producto:
        print(f'Producto encontrado: {producto}')
        producto_encontrado = True
        break
if not producto_encontrado:
    print(f'No se encontro un producto con el id {id_producto}')

# para eliminar un producto del inventario, podemos utilizar el id del producto para eliminar el diccionario 
# asociado a ese producto de la lista de inventario
id_producto_eliminar = int(input('Ingresa el id del producto a eliminar: '))
producto_eliminar = None
for producto in inventario:
    if producto['id'] == id_producto_eliminar:
        producto_eliminar = producto
        break

if producto_eliminar:
    inventario.remove(producto_eliminar) # eliminamos el producto utilizando el metodo remove de la lista
    print(f'El producto con id {id_producto_eliminar} ha sido eliminado.')
else:
    print(f'No se encontro un producto con el id {id_producto_eliminar} para eliminar.')

print(f'Inventario de productos actualizado: {inventario}')
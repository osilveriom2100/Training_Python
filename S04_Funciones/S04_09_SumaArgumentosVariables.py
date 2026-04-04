print("suma de argumentos variables")

def suma(*args):
    total = 0
    for numero in args:
        total += numero
    return total # sum(args), se puede hacer de esta forma directamente

resultado = suma(4,5,6,8,7)
print(f"La suma de argumentos: {resultado}")
    
print("Detalles de una persona")

def descripcion(nombre, **kwargs):
    print(f'{nombre}:', end ='')
    for tipo, detalle in kwargs.items():
        print(f'es {tipo}: {detalle}', end=', ')
    print()
descripcion("victor", estatura = "media", piel="morena", cabello = "lacio")    

## funcion par
print('Saber is un numero es para o impar, de una lista de numeros')

def par_impar(*args):
    valor = False
    if any(val % 2 == 0 for val in args):
        valor = True
    return valor

print(f'El numero dos es: par :{par_impar(2)}')


print('Calculadora')

def suma():
    a = solicitud() 
    b = solicitud()
    print(f'La suma de {a} + {b} = {a+b}')

def resta():
    a = solicitud() 
    b = solicitud()
    print(f'La resta de {a} - {b} = {a-b}')

def multiplicar():
    a = solicitud()
    b = solicitud()
    print(f'La multiplicacion de {a} * {b} = {a*b}')

def division():
    a = solicitud() 
    while True:
        b = solicitud()
        if b != 0:
            break
        print('No se puede dividir entre cero')
    print(f'La division de {a} / {b} = {a/b}')


def menu():
    print(''' Caluculadora con funciones
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Division
            5. Salir
''')
    
def solicitud():
    while True:
        try:
            numero = float(input(' Introduce el numero a usar: '))
            return numero
        except ValueError:
            print('Introduce un numero')

# Programa inicial
if __name__ == '__main__':
    while True:
        menu()
        try:
            opcion = int(input('Selecciona una opcion: '))
        except  ValueError:
            print('Introduce un numero')
            continue
        match opcion:
            case 1:
                suma()
            case 2:
                resta()
            case 3:
                multiplicar()
            case 4:
                division()
            case 5:
                print('Saliendo del programa...')
                break    
            case _:
                print('Opcion no encontrada')
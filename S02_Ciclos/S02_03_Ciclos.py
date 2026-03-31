# Los ciclos de control so estructuras que repiten una seria de instrucciones hasta que se cumple una condicion especifica
# En python existen dos tipos de estructuras; while and for

# Ciclo while repite una serie de instrucciones mientras la condion a evaluar sea verdadera

# Sintaxis ciclo while
#while condicion:
    #Bloque de codigo a ejecutar

#Ejemplo ciclo while
# imprime de 1 a 3
contador = 1
while contador <= 3:
    print(contador)
    contador +=1

## imprimir del 1 al 5
conta = 1
while conta <= 5:
    print(conta, end=' ')
    conta +=1

## Ciclos for
# El ciclo for itera o recorre una secuencia de valores, por ejemplo los caracteres de una cadena, una lista, etc.
# y ejectura un bloque de codigo por cada elemento de la secuencia

# sintaxis ciclo for
# for variable in secuencia
#   Bloque de codigo a ejecutar

#Ejemplo ciclo for
cadena = 'Hola Mundo'
for letra in cadena:
    print(letra, end= ' ')

frutas = ['limon', 'platano', 'melon']
for fruta in frutas:
    print(fruta)

numero = 1
suma = 1
while numero <= 5:
    suma += suma
    print(f'suma: {suma}')
    numero += 1

## 
opcion = 0
while opcion != 3:
    print(" ** Sistema de administracion de cuentas ** ")
    print("""Menu:
        1. Crear cuenta
        2. Eliminar cuenta
        3. Salir """)

    opcion = int(input("Escoje una opcion: "))
    if opcion == 1:
        print("Crenado cuenta")
    elif opcion == 2:
        print("Eliminar cunenta")
    elif opcion == 3:
        print("Salir")
    else:
        print("Opcion no encontrada")
else:
    print("Terminando proceso")

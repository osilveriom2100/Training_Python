# Operadores en python
## Operadores aritméticos
### Pertenecen a esta categoría los operadores de suma, resta, multiplicación, división, módulo, potencia y división entera.
##### Suma
a = 10
b = 5
suma = a + b
print("La suma de a y b es:", suma)
#### Resta
resta = a - b
print("La resta de a y b es:", resta)
#### Multiplicación
multiplicacion = a * b
print("La multiplicación de a y b es:", multiplicacion)
#### División
division = a / b
print("La división de a y b es:", division)
#### Módulo
modulo = a % b
print("El módulo de a y b es:", modulo)
#### Potencia
potencia = a ** b
print("La potencia de a elevado a b es:", potencia)
#### División entera
division_entera = a // b
print("La división entera de a y b es:", division_entera)

## Operadores de asignación
### son los operadores que se utilizan para asignar un valor a una variable. El operador de asignación más común es el signo igual (=), pero también existen otros operadores de asignación compuestos como +=, -=, *=, /=, %=, **=, //=.
x = 10
#### Asignación simple
print("El valor de x es:", x)
#### Asignación compuesta
#### El operador de asignación compuesta += suma el valor de la variable a la derecha del operador al valor de la variable a la izquierda del operador y asigna el resultado a la variable a la izquierda del operador.
x += 5
print("El valor de x después de la asignación compuesta es:", x)
#### El operador de asignación compuesta -= resta el valor de la variable a la derecha del operador al valor de la variable a la izquierda del operador y asigna el resultado a la variable a la izquierda del operador.
x *= 2
print("El valor de x después de la asignación compuesta es:", x)
#### El operador de asignación compuesta /= divide el valor de la variable a la izquierda del operador por el valor de la variable a la derecha del operador y asigna el resultado a la variable a la izquierda del operador.
x /= 4
print("El valor de x después de la asignación compuesta es:", x)    
#### El operador de asignación compuesta %= calcula el módulo del valor de la variable a la izquierda del operador por el valor de la variable a la derecha del operador y asigna el resultado a la variable a la izquierda del operador.
x %= 3
print("El valor de x después de la asignación compuesta es:", x)
#### El operador de asignación compuesta **= calcula la potencia del valor de la variable a la izquierda del operador por el valor de la variable a la derecha del operador y asigna el resultado a la variable a la izquierda del operador.
x **= 2
print("El valor de x después de la asignación compuesta es:", x)
#### El operador de asignación compuesta //= calcula la división entera del valor de la variable a la izquierda del operador por el valor de la variable a la derecha del operador y asigna el resultado a la variable a la izquierda del operador.
x //= 2 
print("El valor de x después de la asignación compuesta es:", x)
#### El operador de asignación compuesta =+ asigna el valor de la variable a la derecha del operador a la variable a la izquierda del operador, pero no realiza ninguna operación matemática. Es decir, x =+ 5 es equivalente a x = 5, no a x += 5.
x =+ 5
print("El valor de x después de la asignación compuesta es:", x)
#### El operador de asignación compuesta =- asigna el valor de la variable a la derecha del operador a la variable a la izquierda del operador, pero no realiza ninguna operación matemática. Es decir, x =- 5 es equivalente a x = 5, no a x -= 5.
x =- 5
print("El valor de x después de la asignación compuesta es:", x)

## Operadores de comparación
### son los operadores que se utilizan para comparar dos valores y devolver un valor booleano (True o False) dependiendo del resultado de la comparación. Los operadores de comparación más comunes son ==, !=, >, <, >=, <=.
a = 10
b = 5
#### Igualdad
print("¿a es igual a b?", a == b)
#### Desigualdad
print("¿a es diferente de b?", a != b)
#### Mayor que
print("¿a es mayor que b?", a > b)
#### Menor que
print("¿a es menor que b?", a < b)
#### Mayor o igual que
print("¿a es mayor o igual que b?", a >= b)
#### Menor o igual que
print("¿a es menor o igual que b?", a <= b)

## Operadores lógicos
### son los operadores que se utilizan para combinar expresiones booleanas y devolver un valor booleano dependiendo del resultado de la combinación. Los operadores lógicos más comunes son and, or, not.
a = True
b = False
#### AND
print("¿a AND b?", a and b)
#### OR
print("¿a OR b?", a or b)
#### NOT
print("¿NOT a?", not a)
print("¿NOT b?", not b)
## Operadores de identidad
### son los operadores que se utilizan para comparar la identidad de dos objetos y devolver un valor booleano dependiendo del resultado de la comparación. Los operadores de identidad más comunes son is y is not.
a = [1, 2, 3]
b = [1, 2, 3]
#### IS
print("¿a es b?", a is b)
#### IS NOT
print("¿a no es b?", a is not b)
## Operadores de pertenencia
### son los operadores que se utilizan para comprobar si un valor pertenece a una secuencia (como una lista, una tupla o un conjunto) y devolver un valor booleano dependiendo del resultado de la comprobación. Los operadores de pertenencia más comunes son in y not in.
a = [1, 2, 3]
#### IN
print("¿2 está en a?", 2 in a)
#### NOT IN
print("¿4 no está en a?", 4 not in a)

## Operadores de bit a bit
### son los operadores que se utilizan para realizar operaciones a nivel de bits en números enteros. Los operadores de bit a bit más comunes son &, |, ^, ~, <<, >>.
a = 5  # En binario: 0101
b = 3  # En binario: 0011
#### AND bit a bit
print("a AND b (bit a bit):", a & b)  # Resultado en binario: 0001 (1 en decimal)
#### OR bit a bit
print("a OR b (bit a bit):", a | b)  # Resultado en binario: 0111 (7 en decimal)
#### XOR bit a bit
print("a XOR b (bit a bit):", a ^ b)  # Resultado en binario: 0110 (6 en decimal)
#### NOT bit a bit
print("NOT a (bit a bit):", ~a)  # Resultado en binario: 1010 (-6 en decimal)
#### Desplazamiento a la izquierda
print("a desplazado a la izquierda por 1 (bit a bit):", a << 1)  # Resultado en binario: 1010 (10 en decimal)
#### Desplazamiento a la derecha
print("a desplazado a la derecha por 1 (bit a bit):", a >> 1)  # Resultado en binario: 0010 (2 en decimal)
## operadores de membresía
### son los operadores que se utilizan para comprobar si un valor pertenece a una secuencia (como una lista, una tupla o un conjunto) y devolver un valor booleano dependiendo del resultado de la comprobación. Los operadores de membresía más comunes son in y not in.
a = [1, 2, 3]
#### IN
print("¿2 está en a?", 2 in a)
#### NOT IN
print("¿4 no está en a?", 4 not in a)


# Operadores de comparación
# son operadores que se utilizan para comparar dos valores y devolver un resultado booleano (True o False) dependiendo de si la comparación es verdadera o falsa.
# ==, !=, >, <, >=, <=
x = 10
y = 5
# Comparación de igualdad
print(f"¿x es igual a y? {x == y}")
# Comparación de desigualdad
print(f"¿x es diferente de y? {x != y}")
# Comparación de mayor que
print(f"¿x es mayor que y? {x > y}")
# Comparación de menor que
print(f"¿x es menor que y? {x < y}")
# Comparación de mayor o igual que
print(f"¿x es mayor o igual que y? {x >= y}")
# Comparación de menor o igual que
print(f"¿x es menor o igual que y? {x <= y}")
# Comparación de cadenas
str1 = "Hola"
str2 = "Mundo"
print(f"¿str1 es igual a str2? {str1 == str2}")
print(f"¿str1 es diferente de str2? {str1 != str2}")
print(f"¿str1 es mayor que str2? {str1 > str2}")
print(f"¿str1 es menor que str2? {str1 < str2}")
print(f"¿str1 es mayor o igual que str2? {str1 >= str2}")
print(f"¿str1 es menor o igual que str2? {str1 <= str2}")
# Comparación de listas
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"¿list1 es igual a list2? {list1 == list2}")
print(f"¿list1 es diferente de list2? {list1 != list2}")
print(f"¿list1 es mayor que list2? {list1 > list2}")    
print(f"¿list1 es menor que list2? {list1 < list2}")
print(f"¿list1 es mayor o igual que list2? {list1 >= list2}")
print(f"¿list1 es menor o igual que list2? {list1 <= list2}")

# Operadores de relación
# son operadores que se utilizan para comparar dos valores y devolver un resultado booleano (True o False) dependiendo de si la relación es verdadera o falsa.
# is, is not, in, not in
a = [1, 2, 3]
b = a
c = [1, 2, 3]
# Comparación de identidad
print(f"¿a es b? {a is b}")
print(f"¿a es c? {a is c}") 
print(f"¿a no es b? {a is not b}")
print(f"¿a no es c? {a is not c}")
# Comparación de pertenencia
print(f"¿1 está en a? {1 in a}")
print(f"¿4 está en a? {4 in a}")
print(f"¿1 no está en a? {1 not in a}")
print(f"¿4 no está en a? {4 not in a}")

# Operadores logicos
# son operadores que se utilizan para combinar dos o más expresiones booleanas y devolver un resultado booleano (True o False) dependiendo de si la combinación es verdadera o falsa.
# and, or, not
p = True
q = False
# Operador lógico AND
print(f"p AND q: {p and q}")
# Operador lógico OR
print(f"p OR q: {p or q}")
# Operador lógico NOT, se utiliza para negar el valor de una expresión booleana, es decir, 
# si la expresión es verdadera, el operador NOT la convierte en falsa, y si la expresión es falsa, 
# el operador NOT la convierte en verdadera.
print(f"NOT p: {not p}")
print(f"NOT q: {not q}")

# revisar si una variable es cadena vacía
s = ""
print(f"¿s es una cadena vacía? {not s}") # una cadena vacía se considera falsa en un contexto booleano, por lo que not s devuelve True
# revisar si una variable no tiene un valor asignado (es decir, es None)
r = None
print(f"¿r es None? {r is None}")
# None es diferente de una cadena vacía, un número cero o una lista vacía, 
# ya que None representa la ausencia de un valor, mientras que los otros representan valores específicos.
print(f"¿r es una cadena vacía? {r == ''}")


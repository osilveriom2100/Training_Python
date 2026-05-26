# Función zip
# La función zip combina múltiples iterables en uno solo, creando pares de elementos correspondientes.
# Sintaxis: zip(iterable1, iterable2, ...)
# Ejemplo:
nombres = ['Alice', 'Bob', 'Charlie']
edades = [25, 30, 35]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")

# Output:
# Alice tiene 25 años.
# Bob tiene 30 años.
# Charlie tiene 35 años.
# La función zip también se puede usar para crear diccionarios a partir de dos listas:
diccionario = dict(zip(nombres, edades))
print(diccionario)  # Output: {'Alice': 25, 'Bob': 30, 'Charlie': 35}
# Si las listas tienen diferente longitud, zip se detendrá al final de la lista más corta:
nombres2 = ['Alice', 'Bob']
edades2 = [25, 30, 35]
for nombre, edad in zip(nombres2, edades2):
    print(f"{nombre} tiene {edad} años.")
# Output:
# Alice tiene 25 años.
# Bob tiene 30 años.
# Para evitar esto, se puede usar itertools.zip_longest:
from itertools import zip_longest
for nombre, edad in zip_longest(nombres2, edades2):
    print(f"{nombre} tiene {edad} años.")
# Output:
# Alice tiene 25 años.
# Bob tiene 30 años.
# None tiene None años.

# Función split
# La función split se utiliza para dividir una cadena en una lista de subcadenas, utilizando un separador específico.
# Sintaxis: cadena.split(separador, maxsplit)
# Ejemplo:
frase = "Hola, ¿cómo estás?"
palabras = frase.split()  # Por defecto, el separador es cualquier espacio en blanco
print(palabras)  # Output: ['Hola,', '¿cómo', 'estás?']
# Usando un separador específico:
frase2 = "manzana,banana,naranja"
frutas = frase2.split(',')  # Separador es la coma
print(frutas)  # Output: ['manzana', 'banana', 'naranja']
# El parámetro maxsplit limita el número de divisiones:
frase3 = "uno dos tres cuatro cinco"
partes = frase3.split(' ', 2)  # Solo se dividirá en dos partes
print(partes)  # Output: ['uno', 'dos', 'tres cuatro cinco']

# funcion find
# La función find se utiliza para buscar la posición de una subcadena dentro de una cadena.
# Sintaxis: cadena.find(subcadena, inicio, fin)
# Ejemplo:
texto = "Hola, ¿cómo estás?"
posicion = texto.find('cómo')
print(posicion)  # Output: 6
# Si la subcadena no se encuentra, find devuelve -1:
posicion2 = texto.find('adiós')
print(posicion2)  # Output: -1
# También se pueden especificar los parámetros inicio y fin para limitar la búsqueda:
posicion3 = texto.find('o', 5)  # Buscar 'o' a partir de la posición 5
print(posicion3)  # Output: 8   

# funcion replace
# La función replace se utiliza para reemplazar todas las ocurrencias de una subcadena por otra en una cadena.
# Sintaxis: cadena.replace(subcadena_vieja, subcadena_nueva, count)
# Ejemplo:
texto2 = "Hola, ¿cómo estás? Hola!"
nuevo_texto = texto2.replace('Hola', 'Adiós')
print(nuevo_texto)  # Output: "Adiós, ¿cómo estás? Adiós!"
# El parámetro count limita el número de reemplazos:
nuevo_texto2 = texto2.replace('Hola', 'Adiós', 1)
print(nuevo_texto2)  # Output: "Adiós, ¿cómo estás? Hola!"  

# función join
# La función join se utiliza para unir una lista de cadenas en una sola cadena, utilizando un separador específico.
# Sintaxis: separador.join(iterable)
# Ejemplo:
frutas2 = ['manzana', 'banana', 'naranja']
cadena_frutas = ', '.join(frutas2)  # El separador es una coma seguida de un espacio
print(cadena_frutas)  # Output: "manzana, banana, naranja"
# También se puede usar un separador diferente:
cadena_frutas2 = ' - '.join(frutas2)  # El separador es un guion seguido de un espacio
print(cadena_frutas2)  # Output: "manzana - banana - naranja"
# Si la lista contiene elementos que no son cadenas, se producirá un error:
# frutas3 = ['manzana', 42, 'naranja']
# cadena_frutas3 = ', '.join(frutas3)  # Esto generará un error porque 42 no es una cadena

# funcion strip
# La función strip se utiliza para eliminar los caracteres de espacio en blanco (u otros caracteres especificados) al principio y al final de una cadena.
# Sintaxis: cadena.strip(caracteres)
# Ejemplo:
texto3 = "   Hola, ¿cómo estás?   "
texto_limpio = texto3.strip()  # Elimina los espacios en blanco al principio y al final
print(texto_limpio)  # Output: "Hola, ¿cómo estás?" 
# También se pueden especificar otros caracteres a eliminar:
texto4 = "###Hola, ¿cómo estás?###"
texto_limpio2 = texto4.strip('#')  # Elimina los caracteres '#' al principio y al final
print(texto_limpio2)  # Output: "Hola, ¿cómo estás?"
# Si se desea eliminar solo los espacios en blanco al principio o al final, se pueden usar lstrip o rstrip:
texto5 = "   Hola, ¿cómo estás?   " 
texto_limpio3 = texto5.lstrip()  # Elimina los espacios en blanco al principio
print(texto_limpio3)  # Output: "Hola, ¿cómo estás?   "
texto_limpio4 = texto5.rstrip()  # Elimina los espacios en blanco al final
print(texto_limpio4)  # Output: "   Hola, ¿cómo estás?"

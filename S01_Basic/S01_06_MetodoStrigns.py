mensaje = "aprendiendo metodos de strings"
# longitud de la cadena
tamanio = len(mensaje)
print(f"Longitud del mensaje: {tamanio}")
# convertir a mayusculas
mensaje_mayus = mensaje.upper()
print(f"Mensaje en mayusculas: {mensaje_mayus}")
# convertir a minusculas
mensaje_minus = mensaje.lower()
print(f"Mensaje en minusculas: {mensaje_minus}")

animal = "Gato"
# cadenas inmutables
# animal[0] = "P" # esto generaria un error porque las cadenas son inmutables
animal = "P" + animal[1:] 
print(f"Animal modificado: {animal}")
plural = f"{animal}s"
print(f"Plural del animal: {plural}")

# Slicing de cadenas
mensaje = "Programacion"
# texto[inicio:fin:paso] #inicio es el indice de inicio, fin es el indice de fin (no incluido) y paso es el salto entre caracteres
subcadena = mensaje[0:10] # obtiene los primeros 10 caracteres
print(f"Subcadena: {subcadena}")
subcadena2 = mensaje[11:] # obtiene desde el indice 11 hasta el final
print(f"Subcadena 2: {subcadena2}")
subcadena3 = mensaje[::2] # obtiene cada segundo caracter
print(f"Subcadena 3: {subcadena3}")
subcadena4 = mensaje[-4:] # obtiene los ultimos 4 caracteres
print(f"Ultimo 4 caracteres: {subcadena4}")
subcadena5 = mensaje[-1] # obtiene el ultimo caracter
print(f"Ultimo caracter: {subcadena5}")
subcadena6 = mensaje[::-1] # obtiene la cadena en orden inverso
print(f"Mensaje en orden inverso: {subcadena6}")
subcadena6 = mensaje[-1:-6:-1] # obtiene los ultimos 5 caracteres en orden inverso
print(f"Ultimos 5 caracteres en orden inverso: {subcadena6}")
subcadena7 = mensaje[5:0:-1] # obtiene los primeros 5 caracteres en orden inverso
print(f"Primeros 5 caracteres en orden inverso: {subcadena7}")
subcadena8 = mensaje[5:0:-2] # obtiene los primeros 5 caracteres en orden inverso saltando uno
print(f"Primeros 5 caracteres en orden inverso saltando uno: {subcadena8}")

mensaje = "Hola Mundo, Hola Python, Hola Programacion"
# reamplazar caracteres
# text.replace("cadenas", "nuevas_cadenas", count) # reemplaza las ocurrencias de "cadenas" por "nuevas_cadenas", count es opcional y limita el numero de reemplazos
mensaje_reemplazado = mensaje.replace("Hola", "Adios") # reemplaza todas las ocurrencias de "Hola" por "Adios"
print(f"Mensaje con 'Hola' reemplazada por 'Adios': {mensaje_reemplazado}")
mensaje_reemplazado2 = mensaje.replace("Hola", "Adios", 1) # solo reemplaza la primera ocurrencia de "Hola"
print(f"Mensaje con la primera 'Hola' reemplazada por 'Adios': {mensaje_reemplazado2}")


# contar ocurrencias
# text.count("cadena") # cuenta el numero de ocurrencias de "cadena" en el texto
contador_hola = mensaje.count("Hola")
print(f"Numero de ocurrencias de 'Hola': {contador_hola}")

# dividir una cadena en una lista de subcadenas
# text.split(separador, maxsplit) # divide el texto en una lista de subcadenas usando el separador, maxsplit es opcional y limita el numero de divisiones
palabras = mensaje.split() # divide el mensaje en una lista de palabras usando el espacio como separador
print(f"Lista de palabras: {palabras}")

palabras = mensaje.split(", ") # divide el mensaje en una lista de palabras usando ", "como separador
print(f"Lista de palabras: {palabras}")

# dividir una cadena en una lista de subcadenas usando un separador diferente
palabras2 = mensaje.split(" ") # divide el mensaje en una lista de palabras usando " " como separador
print(f"Lista de palabras usando espacio como separador: {palabras2}")

# eliminar espacios en blanco, tabulaciones y saltos de linea al inicio y al final de la cadena
# text.strip() # elimina los espacios en blanco, tabulaciones y saltos de linea
mensaje_sin_espacios = mensaje.strip()
print(f"Mensaje sin espacios: {mensaje_sin_espacios}")

# encontrar la posicion de una subcadena
# text.find("cadena") # devuelve el indice de la primera ocurrencia de "cadena", o -1 si no se encuentra
indice_hola = mensaje.find("Hola")
print(f"Indice de la primera ocurrencia de 'Hola': {indice_hola}")
indice_hola2 = mensaje.find("Hola", indice_hola + 1) # busca la siguiente ocurrencia de "Hola" a partir del indice encontrado anteriormente
print(f"Indice de la segunda ocurrencia de 'Hola': {indice_hola2}")

# verificar si una subcadena esta presente
# text.__contains__("cadena") # devuelve True si "cadena" esta presente en el texto
esta_presente = mensaje.__contains__("Hola")
print(f"¿Está presente 'Hola' en el mensaje? {esta_presente}")
# verificar si una subcadena esta presente usando el operador in
esta_presente_in = "Hola" in mensaje
print(f"¿Está presente 'Hola' en el mensaje usando 'in'? {esta_presente_in}")
# verificar si una subcadena no esta presente usando el operador not in
no_esta_presente_in = "Adios" not in mensaje
print(f"¿No está presente 'Adios' en el mensaje usando 'not in'? {no_esta_presente_in}")
# verificar si una subcadena esta presente usando el metodo find
esta_presente_find = mensaje.find("Hola") != -1
print(f"¿Está presente 'Hola' en el mensaje usando 'find'? {esta_presente_find}")
# verificar si una subcadena no esta presente usando el metodo find
no_esta_presente_find = mensaje.find("Adios") == -1
print(f"¿No está presente 'Adios' en el mensaje usando 'find'? {no_esta_presente_find}")
# verificar si una subcadena esta presente usando el metodo count
esta_presente_count = mensaje.count("Hola") > 0
print(f"¿Está presente 'Hola' en el mensaje usando 'count'? {esta_presente_count}")

# aperaciones de cadenas
# text.startswith("cadena") # devuelve True si el texto comienza con "cadena"
comienza_con_hola = mensaje.startswith("Hola")
print(f"¿El mensaje comienza con 'Hola'? {comienza_con_hola}")
# text.endswith("cadena") # devuelve True si el texto termina con "cadena"
termina_con_programacion = mensaje.endswith("Programacion")
print(f"¿El mensaje termina con 'Programacion'? {termina_con_programacion}")
# text.isalpha() # devuelve True si el texto solo contiene letras
solo_letras = mensaje.isalpha()
print(f"¿El mensaje solo contiene letras? {solo_letras}")
# text.isdigit() # devuelve True si el texto solo contiene numeros
solo_numeros = mensaje.isdigit()
print(f"¿El mensaje solo contiene números? {solo_numeros}")
# text.isalnum() # devuelve True si el texto solo contiene letras y numeros
solo_letras_numeros = mensaje.isalnum()
print(f"¿El mensaje solo contiene letras y números? {solo_letras_numeros}")
# text.isspace() # devuelve True si el texto solo contiene espacios
solo_espacios = mensaje.isspace()
print(f"¿El mensaje solo contiene espacios? {solo_espacios}")
# text.islower() # devuelve True si el texto solo contiene letras minusculas
solo_minusculas = mensaje.islower()
print(f"¿El mensaje solo contiene letras minusculas? {solo_minusculas}")
# text.isupper() # devuelve True si el texto solo contiene letras mayusculas
solo_mayusculas = mensaje.isupper()
print(f"¿El mensaje solo contiene letras mayusculas? {solo_mayusculas}")

### 
mensaje = "Hola"
# multiplicacion de cadenas
# text * n # devuelve el texto repetido n veces
mensaje_multiplicado = mensaje * 3
print(f"Mensaje multiplicado por 3: {mensaje_multiplicado}")
# cadena * 0 # devuelve una cadena vacia
mensaje_vacio = mensaje * 0
print(f"Mensaje multiplicado por 0: '{mensaje_vacio}'")
# pratones
patron = "abc"
patron_repetido = patron * 5
print(f"Patrón repetido 5 veces: {patron_repetido}")
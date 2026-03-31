# correo
nombre = "Victor Silva Gonzalez"
empresa = "Google Mexico"
dominio = ".com.mx"

nombre_minuscula = nombre.lower().strip() # strip elimina los espacios al inicio y al final de la cadena
primer_espacio = nombre_minuscula.find(" ")
nombre_usuario = nombre_minuscula[0:primer_espacio]
segundo_espacio = nombre_minuscula.find(" ", +  primer_espacio + 1)
apellido_paterno = nombre_minuscula[primer_espacio + 1: segundo_espacio]
empresa_sin_espacios = empresa.replace(" ", "").lower()

email = f"{nombre_usuario}.{apellido_paterno}@{empresa_sin_espacios}{dominio}"
print(f"Correo electrónico generado: {email}")

# segunda solucion
nombre_minuscula = nombre.lower().strip()
palabras = nombre_minuscula.split() # split divide la cadena en una lista de palabras usando el espacio como separador
nombre_usuario = palabras[0]
apellido_paterno = palabras[1]
empresa_sin_espacios = empresa.replace(" ", "").lower()

email = f"{nombre_usuario}.{apellido_paterno}@{empresa_sin_espacios}{dominio}"
print(f"Correo electrónico generado: {email}")

# tercera solucion
palabras = nombre.lower().strip().replace(" ", ".", 1).split() # replace reemplaza el primer espacio por un punto, luego split divide la cadena en una lista de palabras usando el espacio como separador
empresa_sin_espacios = empresa.replace(" ", "").lower()
email = f"{palabras[0]}@{empresa_sin_espacios}{dominio}"
print(f"Correo electrónico generado: {email}")

# cuarta solucion
palabras = nombre.lower().strip().split() # split divide la cadena en una lista de palabras usando el espacio como separador
empresa_sin_espacios = empresa.replace(" ", "").lower() 
email = f"{palabras[0]}.{palabras[1]}@{empresa_sin_espacios}{dominio}"
print(f"Correo electrónico generado: {email}")
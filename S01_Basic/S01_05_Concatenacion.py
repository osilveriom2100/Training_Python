# concatenacion de cadenas

# usando el operador +
nombre = "Juan"
apellido = "Perez"
nombre_completo = nombre + " " + apellido
print("usando + :" + nombre_completo)

# usando el metodo print
edad = 30
print("Usando comas:", "Nombre:", nombre_completo, ", Edad:", edad)

# usando f-strings
ciudad = "Madrid"
pais = "España"
profesion = "Ingeniero"
print(f"Usando f-strings: {nombre_completo} es un {profesion} de {ciudad}, {pais}.")
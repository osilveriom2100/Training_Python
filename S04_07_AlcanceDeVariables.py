# Las varaibles definidas dentro de una función solo existen dentro de esa función, es decir, no pueden ser accedidas desde fuera de la función. Esto se conoce como alcance de variables o scope.
# Por ejemplo, si se define una variable dentro de una función, esa variable solo existirá dentro de esa función y no podrá ser accedida desde fuera de la función. Si se intenta acceder a esa variable desde fuera de la función, se obtendrá un error de NameError indicando que la variable no está definida.
# Sin embargo, si se define una variable fuera de una función, esa variable puede ser accedida desde dentro de la función, siempre y cuando no se intente modificar esa variable dentro de la función. Si se intenta modificar esa variable dentro de la función, se creará una nueva variable local con el mismo nombre, lo que puede causar confusión y errores en el código. Por lo tanto, es importante tener cuidado al usar variables con el mismo nombre tanto dentro como fuera de las funciones para evitar problemas de alcance de variables. 
# Ejemplo de alcance de variables

print(' Alcance de variables ')
# variable global
contador_global = 0

def incrementar_contador():
    # variable local
    contador_local = 0
    contador_local += 1
    print(f'Contador local: {contador_local}')
    # se puede acceder a la variable global dentro de la funcion, pero para modificarla, se debe usar la palabra clave global   
    global contador_global
    contador_global += 1
    print(f'Contador global: {contador_global}')

while contador_global < 5:
    # llamar a la funcion varias veces
    incrementar_contador()

print(f'Contador global despues de llamar a la funcion: {contador_global}')
# intentar acceder a la variable local fuera de la funcion
try:
    print(contador_local) # esto generara un error de NameError porque contador_local no esta definida fuera de la funcion incrementar_contador()   
except NameError as e:
    print(f'Error: {e}')

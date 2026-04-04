# Los modulos en Python son archivos que contienen definiciones y declaraciones de funciones, clases y variables.
# Los modulos permiten organizar el codigo en partes mas pequeñas y reutilizables, lo que facilita el mantenimiento y la legibilidad del codigo.
# Para crear un modulo, simplemente se crea un archivo con extension .py y se definen las funciones, clases y variables que se quieran incluir en el modulo.
# Para usar un modulo en otro archivo, se puede importar el modulo usando la palabra clave import seguida del nombre del modulo.
# Por ejemplo, si se tiene un archivo llamado S04_M01_Modulo_Sumar.py que contiene la funcion sumar, se puede importar el modulo en otro archivo usando import S04_M01_Modulo_Sumar, y luego usar la funcion sumar del modulo usando S04_M01_Modulo_Sumar.sumar().  


# funcion con retorno
def sumar(a, b):
    return a + b

# Este es el archivo S04_M01_Modulo_Sumar.py
# En este archivo se define la funcion sumar que se usara en cualquier otro archivo que importe este modulo

# para probar la funcion sumar, se puede ejecutar este archivo directamente
if __name__ == "__main__":
    resultado = sumar(5, 3)
    print("El resultado de la suma es:", resultado)

# __name__ es una variable especial en Python que se asigna automáticamente 
# a "__main__" cuando el archivo se ejecuta directamente, y a el nombre del modulo cuando 
# se importa. Esto permite que el bloque de codigo dentro del if __name__ == "__main__": 
# solo se ejecute cuando el archivo se ejecuta directamente, y no cuando se importa como 
# un modulo. 

# Cuando se importa este modulo en otro archivo, el bloque de codigo de prueba no se ejecutara, 
# lo que permite que la funcion sumar se use sin ejecutar el codigo de prueba cada vez que se importe el modulo.
# y la variable __name__ se asignara al nombre del modulo, lo que permite que el bloque de codigo de prueba no se ejecute.  
# ejemplo: si se importa este modulo en el archivo S04_03_Modulos.py, 
# la variable __name__ se asignara a "S04_M01_Modulo_Sumar", lo que hara que el bloque de codigo de prueba no se ejecute.   


# De esta manera, se puede probar la funcion sumar ejecutando este archivo directamente, y 
# al mismo tiempo, se puede importar esta funcion en otros archivos sin que se ejecute el 
# bloque de codigo de prueba.

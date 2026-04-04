# Este es el archivo S04_03_Modulos.py
# En este archivo se muestra como importar un modulo y usar una funcion definida en ese modulo
#import S04_M01_Modulo_Sumar
# Importar una funcion especifica del modulo
from S04_M01_Modulo_Sumar import sumar

# Usar la funcion sumar del modulo S04_M01_Modulo_Sumar
resultado = sumar(5, 3)
print("El resultado de la suma es:", resultado)
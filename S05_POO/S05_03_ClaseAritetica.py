# Clase de aritmetica

class Aritmetica:
    def __init__(self, operador1, operador2):
        self.operador1 = operador1
        self.operador2 = operador2

    def sumar(self):
        return self.operador1 + self.operador2
    
    def restar(self):
        return self.operador1 - self.operador2
    
    def multiplicar(self):
        return self.operador1 * self.operador2
    
    def dividir(self):
        if self.operador2 == 0:
            return 0
        else:
            return self.operador1 / self.operador2
        
if __name__ == "__main__":
    aritmetica1 = Aritmetica(10, 5)
    
    print(f"Suma: {aritmetica1.sumar()}")
    print(f"Resta: {aritmetica1.restar()}")
    print(f"Multiplicación: {aritmetica1.multiplicar()}")
    print(f"División: {aritmetica1.dividir()}")

# En python no existe el concepto de sobrecarga de métodos, pero se puede simular utilizando argumentos por defecto o *args y **kwargs. 
# Por ejemplo, podríamos modificar la clase Aritmetica para que el método sumar pueda aceptar un número variable de argumentos: 
# class Aritmetica:
#     def __init__(self, *operadores):
#         self.operadores = operadores
#     def sumar(self):
#         return sum(self.operadores)
#     def restar(self):
#         resultado = self.operadores[0]    
#         for operador in self.operadores[1:]:
#             resultado -= operador
#         return resultado
#    def multiplicar(self):
#         resultado = 1
#         for operador in self.operadores:
#             resultado *= operador
#         return resultado
#     def dividir(self):
#         resultado = self.operadores[0]
#         for operador in self.operadores[1:]:
#             if operador == 0:
#                 return 0
#             resultado /= operador
#         return resultado

# De esta manera, podríamos crear una instancia de Aritmetica con cualquier cantidad de operadores y el método sumar sumaría todos ellos.   
# aritmetica2 = Aritmetica(1, 2, 3, 4)
# print(f"Suma: {aritmetica2.sumar()}")  # Salida: Suma: 10
# print(f"Resta: {aritmetica2.restar()}")  # Salida: Resta: -8
# print(f"Multiplicación: {aritmetica2.multiplicar()}")  # Salida: Multiplicación: 24
# print(f"División: {aritmetica2.dividir()}")  # Salida: División: 0.041666666666666664


# En este ejemplo, el método sumar suma todos los operadores proporcionados, mientras que el método restar resta todos los operadores a partir del primero. 
# El método multiplicar multiplica todos los operadores, y el método dividir divide el primer operador por cada uno de los siguientes, manejando el caso de división por cero.


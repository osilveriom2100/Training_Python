# Generacion de ticket de venta
objeto1 = float(input("Ingrese el precio del primer objeto: "))
objeto2 = float(input("Ingrese el precio del segundo objeto: "))
objeto3 = float(input("Ingrese el precio del tercer objeto: "))
descuento = float(input("Ingrese el porcentaje de descuento a aplicar (si no hay, ingrese 0): "))
descuento_total = (descuento / 100) * (objeto1 + objeto2 + objeto3) # se calcula el descuento total
objeto1 -= (descuento / 100) * objeto1 # se aplica el descuento a cada objeto
objeto2 -= (descuento / 100) * objeto2
objeto3 -= (descuento / 100) * objeto3

total = objeto1 + objeto2 + objeto3 + 0.16 * (objeto1 + objeto2 + objeto3) # se agrega el 16% de IVA al total
print(f"El total a pagar por los tres objetos es: {total:.2f}") # se muestra el total con dos decimales
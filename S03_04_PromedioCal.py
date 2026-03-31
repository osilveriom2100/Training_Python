# Prodemedio de calificaciones con listas

# lista vacia
calificaciones = []

no_calificaciones = int(input("cuantas calificaciones tienes? "))
for calificcacion in range(no_calificaciones):
    calificcacion = float(input(f"ingresa la calificacion {calificcacion + 1}: "))
    calificaciones.append(calificcacion)
    
# calcualar promedio
promedio = sum(calificaciones) / len(calificaciones)
print(f'calficacion promdio es: {promedio:.2f}')

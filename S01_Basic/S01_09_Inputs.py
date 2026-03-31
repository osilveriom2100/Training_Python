# entrada en python
# input() -> devuelve un string
name = input("What is your name? ")
print(f"Hello, {name}!")

# input() también puede convertir la entrada a otros tipos de datos, como int o float
age = int(input("How old are you? "))
print(f"You are {age} years old, type of age: {type(age)}")
height = float(input("What is your height in meters? "))
print(f"You are {height} meters tall, type of height: {type(height)}")

# también podemos usar input() para obtener valores booleanos, aunque esto requiere un poco más de trabajo
is_student = input("Are you a student? (yes/no) ").lower().strip() == "yes"
print(f"Are you a student? {is_student}, type of is_student: {type(is_student)}")

# Sistema de empleados
print("\tSistema de empleados")
nombre_empleado = input("Ingrese el nombre del empleado: ")
edad_empleado = int(input("Ingrese la edad del empleado: "))
salario_empleado = float(input("Ingrese el salario del empleado: "))
es_jefe_departamento = input("es jefe de departamento (si/no)? ").lower().strip() == "si"
print(f"Empleado: {nombre_empleado}, Edad: {edad_empleado}, Salario: {salario_empleado:.2f}, Jefe de departamento: {es_jefe_departamento}")


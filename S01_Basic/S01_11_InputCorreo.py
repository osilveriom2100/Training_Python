# Generar correo electrónico a partir del nombre y apellido del usuario
nombre = input("Ingrese su nombre o nombres: ").strip()
apellido = input("Ingrese su apellido o apellidos: ").strip()
empresa = input("Ingrese el nombre de su empresa: ").strip()
extension = input("Ingrese la extensión de su correo (ejemplo: .com, .net, .org): ").strip()
correo = f"{nombre.lower().replace(' ', '.')}.{apellido.lower().replace(' ', '.')}@mx.{empresa.lower().replace(' ', '')}{extension}"
print(f"Correo electrónico generado: {correo}")

correo = f"{nombre.lower().replace(' ', '.')}.{apellido.lower().split()[0]}@{empresa.lower().replace(' ', '')}.{extension}.mx"
print(f"Correo electrónico generado: {correo}")
try:
    from .Biblioteca import Biblioteca
    from .Libro import Libro
except ImportError:
    from Biblioteca import Biblioteca
    from Libro import Libro

if __name__ == "__main__":
    libro1 = Libro("El Quijote", "Miguel de Cervantes", "Novela")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela")
    libro3 = Libro("La casa de los espíritus", "Isabel Allende", "Novela")
    libro4 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela")
    libro5 = Libro("El otoño del patriarca", "Gabriel García Márquez", "Novela")

    biblioteca1 = Biblioteca("Biblioteca Central")
    biblioteca1.agregar_libro(libro1)
    biblioteca1.agregar_libro(libro2)
    biblioteca1.agregar_libro(libro3)
    biblioteca1.agregar_libro(libro4)
    biblioteca1.agregar_libro(libro5)

    print(f"Libros en la biblioteca {biblioteca1.nombre}:")
    biblioteca1.mostrar_libros()
    print(f"Buscando libros del autor Gabriel García Márquez:")
    biblioteca1.buscar_libro_por_autor("Gabriel García Márquez")
    print(f"Buscando libros del género Novela:")
    biblioteca1.buscar_libro_por_genero("Novela")
    print(f"Mostrando información de un libro específico:")
    biblioteca1.mostrar_libro(libro1)


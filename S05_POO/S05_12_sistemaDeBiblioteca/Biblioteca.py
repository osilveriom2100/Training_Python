from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from S05_POO.S05_12_sistemaDeBiblioteca.Libro import Libro


class Biblioteca:
    def __init__(self, nombre: str | None = None, libro: Libro | None = None) -> None:
        self._nombre = nombre
        self._libros: list[Libro] = []
        if libro is not None:
            self._libros.append(libro)

    @property
    def nombre(self) -> str | None:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str | None) -> None:
        self._nombre = nombre

    def agregar_libro(self, libro: Libro) -> None:
        self._libros.append(libro)
    
    def buscar_libro_por_autor(self, autor: str) -> None:
        for autor_lib in self._libros:
            if autor_lib.autor == autor:
                print(f"El libro del autor {autor} es: {autor_lib.titulo}") 

    def buscar_libro_por_genero(self, genero: str) -> None:
        for genero_lib in self._libros:
            if genero_lib.genero == genero:
                print(f"El libro del genero {genero} es: {genero_lib.titulo}") 

    def mostrar_libros(self) -> None:
        for libro in self._libros:
            print(f'libro: {libro.titulo}, autor: {libro.autor}, genero {libro.genero}')

    def mostrar_libro(self, libro: Libro) -> None:
        if libro in self._libros:
            print(f'libro: {libro.titulo}, autor: {libro.autor}, genero {libro.genero}')
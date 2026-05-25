#-Ejercicio 1: Sistema de Gestión de LIBROS.


class Libro:
    def __init__(self, titulo, autor, isbn):
        if not (titulo and autor and isbn):
            raise ValueError("Titulo, autor e ISBN no pueden quedar vacios")
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.isbn = isbn.strip()
        self.disponible = True
        self.prestado_a = None

    def prestar(self, dni):
        if not self.disponible:
            raise ValueError(f"El libro '{self.titulo}' ya esta prestado")
        self.disponible = False
        self.prestado_a = dni

    def devolver(self):
        self.disponible = True
        self.prestado_a = None

    def __str__(self):
        estado = "Disponible" if self.disponible else f"Prestado (DNI: {self.prestado_a})"
        return f"[{self.isbn}] {self.titulo} - {self.autor} - {estado}"


class Miembro:
    def __init__(self, nombre, dni):
        if not (nombre and dni):
            raise ValueError("Nombre y DNI no pueden quedar vacios")
        self.nombre = nombre.strip()
        self.dni = dni.strip()
        self.libros = []

    def agregar_libro(self, isbn):
        self.libros.append(isbn)

    def quitar_libro(self, isbn):
        if isbn not in self.libros:
            raise ValueError(f"El miembro {self.nombre} no tiene ese libro")
        self.libros.remove(isbn)

    def __str__(self):
        if self.libros:
            return f"{self.nombre} (DNI: {self.dni}) - Libros: {', '.join(self.libros)}"
        return f"{self.nombre} (DNI: {self.dni}) - Sin libros"


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.miembros = {}

    def agregar_libro(self, titulo, autor, isbn):
        if isbn in self.libros:
            raise ValueError("Ya existe ese ISBN")
        self.libros[isbn] = Libro(titulo, autor, isbn)
        print(f"Libro agregado: {self.libros[isbn]}")

    def agregar_miembro(self, nombre, dni):
        if dni in self.miembros:
            raise ValueError("Ya existe ese DNI")
        self.miembros[dni] = Miembro(nombre, dni)
        print(f"Miembro agregado: {self.miembros[dni]}")

    def prestar_libro(self, isbn, dni):
        libro = self.libros.get(isbn)
        miembro = self.miembros.get(dni)
        if not libro:
            raise ValueError("No se encontro el libro")
        if not miembro:
            raise ValueError("No se encontro el miembro")
        libro.prestar(dni)
        miembro.agregar_libro(isbn)
        print(f"Libro '{libro.titulo}' prestado a {miembro.nombre}")

    def devolver_libro(self, isbn, dni):
        libro = self.libros.get(isbn)
        miembro = self.miembros.get(dni)
        if not libro:
            raise ValueError("No se encontro el libro")
        if not miembro:
            raise ValueError("No se encontro el miembro")
        miembro.quitar_libro(isbn)
        libro.devolver()
        print(f"Libro '{libro.titulo}' devuelto por {miembro.nombre}")

    def estado_libros(self):
        print("\nEstado de libros")
        if not self.libros:
            print("No hay libros registrados")
        else:
            for libro in self.libros.values():
                print(libro)
        print()

    def estado_miembros(self):
        print("\nEstado de miembros")
        if not self.miembros:
            print("No hay miembros registrados")
        else:
            for miembro in self.miembros.values():
                print(miembro)
        print()


def mostrar_menu():
    print("1. Agregar libro")
    print("2. Agregar miembro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Ver estado de libros")
    print("6. Ver estado de miembros")
    print("0. Salir")


def pedir_dato(texto):
    while True:
        valor = input(f"{texto}: ").strip()
        if valor:
            return valor
        print("No puede quedar vacio")


def main():
    biblioteca = Biblioteca()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()
        if opcion == "1":
            try:
                titulo = pedir_dato("Titulo")
                autor = pedir_dato("Autor")
                isbn = pedir_dato("ISBN")
                biblioteca.agregar_libro(titulo, autor, isbn)
            except ValueError as e:
                print("Error:", e)
        elif opcion == "2":
            try:
                nombre = pedir_dato("Nombre")
                dni = pedir_dato("DNI")
                biblioteca.agregar_miembro(nombre, dni)
            except ValueError as e:
                print("Error:", e)
        elif opcion == "3":
            try:
                isbn = pedir_dato("ISBN del libro")
                dni = pedir_dato("DNI del miembro")
                biblioteca.prestar_libro(isbn, dni)
            except ValueError as e:
                print("Error:", e)
        elif opcion == "4":
            try:
                isbn = pedir_dato("ISBN del libro")
                dni = pedir_dato("DNI del miembro")
                biblioteca.devolver_libro(isbn, dni)
            except ValueError as e:
                print("Error:", e)
        elif opcion == "5":
            biblioteca.estado_libros()
        elif opcion == "6":
            biblioteca.estado_miembros()
        elif opcion == "0":
            break
        else:
            print("Opcion invalida")
        input("Presiona Enter para continuar")


if __name__ == "__main__":
    main()  
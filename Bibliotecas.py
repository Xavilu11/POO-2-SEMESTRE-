class Biblioteca:
    def __init__(self):
        self.libros = []
        self.prestamos = {}
        self.historial = []

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if libro['autor'] == autor]

    def listar_libros_prestados(self, id_usuario):
        return self.prestamos.get(id_usuario, [])

    def mostrar_historial(self):
        for entrada in self.historial:
            print(entrada)

    def agregar_libro(self, titulo, autor):
        self.libros.append({'titulo': titulo, 'autor': autor})

    def prestar_libro(self, id_usuario, titulo):
        for libro in self.libros:
            if libro['titulo'] == titulo:
                if id_usuario not in self.prestamos:
                    self.prestamos[id_usuario] = []
                self.prestamos[id_usuario].append(titulo)
                self.historial.append(f"{id_usuario} prestó {titulo}")
                self.libros.remove(libro)
                return f"Libro '{titulo}' prestado a {id_usuario}."
        return f"Libro '{titulo}' no encontrado."

def menu():
    biblio = Biblioteca()

    # Agregar algunos datos de ejemplo
    biblio.agregar_libro('Cien años de soledad', 'García Márquez')
    biblio.agregar_libro('El amor en los tiempos del cólera', 'García Márquez')
    biblio.agregar_libro('Crónica de una muerte anunciada', 'García Márquez')

    usuario_carlos = 'C456'
    biblio.prestamos[usuario_carlos] = ['Cien años de soledad', 'Crónica de una muerte anunciada']
    biblio.historial.append('Carlos prestó Cien años de soledad')
    biblio.historial.append('Carlos prestó Crónica de una muerte anunciada')

    while True:
        print("\nMenú de opciones:")
        print("1. Buscar libros por autor")
        print("2. Listar libros prestados a un usuario")
        print("3. Mostrar historial de préstamos")
        print("4. Agregar libro")
        print("5. Prestar libro")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            autor = input("Ingrese el nombre del autor: ")
            print(f"\nLibros de {autor}:")
            for libro in biblio.buscar_por_autor(autor):
                print(f" - {libro['titulo']}")
        elif opcion == '2':
            id_usuario = input("Ingrese el ID del usuario: ")
            print(f"\nLibros prestados a {id_usuario}:")
            for libro in biblio.listar_libros_prestados(id_usuario):
                print(f" - {libro}")
        elif opcion == '3':
            print("\nHistorial completo:")
            biblio.mostrar_historial()
        elif opcion == '4':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            biblio.agregar_libro(titulo, autor)
            print(f"Libro '{titulo}' agregado con éxito.")
        elif opcion == '5':
            id_usuario = input("Ingrese el ID del usuario: ")
            titulo = input("Ingrese el título del libro: ")
            print(biblio.prestar_libro(id_usuario, titulo))
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    biblio = Biblioteca()

    # Agregar algunos datos de ejemplo
    biblio.agregar_libro('Cien años de soledad', 'García Márquez')
    biblio.agregar_libro('El amor en los tiempos del cólera', 'García Márquez')
    biblio.agregar_libro('Crónica de una muerte anunciada', 'García Márquez')

    usuario_carlos = 'C456'
    biblio.prestamos[usuario_carlos] = ['Cien años de soledad', 'Crónica de una muerte anunciada']
    biblio.historial.append('Carlos prestó Cien años de soledad')
    biblio.historial.append('Carlos prestó Crónica de una muerte anunciada')

    # Búsquedas
    print("\nLibros de García Márquez:")
    for libro in biblio.buscar_por_autor("García Márquez"):
        print(f" - {libro['titulo']}")

    # Listar préstamos
    print("\nLibros prestados a Carlos:")
    for libro in biblio.listar_libros_prestados("C456"):
        print(f" - {libro}")

    # Mostrar historial
    print("\nHistorial completo:")
    biblio.mostrar_historial()

    # Iniciar menú interactivo
    menu()
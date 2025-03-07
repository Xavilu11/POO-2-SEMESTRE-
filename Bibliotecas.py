class Biblioteca:
    def __init__(self):
        self.libros = []
        self.prestamos = {}
        self.historial = []
        self.usuarios = {}

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
                self.historial.append(f"{self.usuarios[id_usuario]} ({id_usuario}) prestó '{titulo}'")
                self.libros.remove(libro)
                return f"Libro '{titulo}' prestado a {self.usuarios[id_usuario]} ({id_usuario})."
        return f"Libro '{titulo}' no encontrado."

    def agregar_usuario(self, id_usuario, nombre):
        if id_usuario not in self.usuarios:
            self.usuarios[id_usuario] = nombre
            return f"Usuario '{nombre}' agregado con éxito."
        else:
            return f"Usuario con ID '{id_usuario}' ya existe."

def menu():
    biblio = Biblioteca()

    # Agregar algunos datos de ejemplo
    biblio.agregar_libro('Cien años de soledad', 'García Márquez')
    biblio.agregar_libro('El amor en los tiempos del cólera', 'García Márquez')
    biblio.agregar_libro('Crónica de una muerte anunciada', 'García Márquez')
    biblio.agregar_libro('Huasipungo', 'Jorge Icaza')
    biblio.agregar_libro('Los Sangurimas', 'José de La Cuadra')
    biblio.agregar_libro('Las Catilinarias', 'Juan Montalvo')
    biblio.agregar_libro('Cumandá', 'Juan León Mera')
    biblio.agregar_libro('La tigra', 'José de La Cuadra')
    biblio.agregar_libro('A la Costa', 'Luis Alfredo Martínez')
    biblio.agregar_libro('Polvo y Ceniza', 'Eliecér Cárdenas')
    biblio.agregar_libro('El Chulla Romero y Flores', 'Jorge Icaza')

    # Agregar un usuario y prestar libros
    biblio.agregar_usuario('U001', 'Juan Pérez')
    biblio.prestar_libro('U001', 'Cien años de soledad')
    biblio.prestar_libro('U001', 'Huasipungo')

    while True:
        print("\nMenú de opciones:")
        print("1. Buscar libros por autor")
        print("2. Listar libros prestados a un usuario")
        print("3. Mostrar historial de préstamos")
        print("4. Agregar libro")
        print("5. Prestar libro")
        print("6. Agregar usuario")
        print("7. Mostrar todos los libros")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            autor = input("Ingrese el nombre del autor: ")
            libros = biblio.buscar_por_autor(autor)
            if libros:
                print(f"\nLibros de {autor}:")
                for libro in libros:
                    print(f" - {libro['titulo']}")
            else:
                print(f"\nNo se encontraron libros de {autor}.")
        elif opcion == '2':
            id_usuario = input("Ingrese el ID del usuario: ")
            nombre_usuario = biblio.usuarios.get(id_usuario, "Desconocido")
            libros_prestados = biblio.listar_libros_prestados(id_usuario)
            if libros_prestados:
                print(f"\nLibros prestados a {nombre_usuario} ({id_usuario}):")
                for libro in libros_prestados:
                    print(f" - {libro}")
            else:
                print(f"\nNo se encontraron libros prestados a {nombre_usuario} ({id_usuario}).")
        elif opcion == '3':
            print("\nHistorial completo de préstamos:")
            biblio.mostrar_historial()
        elif opcion == '4':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            biblio.agregar_libro(titulo, autor)
            print(f"\nLibro '{titulo}' agregado con éxito.")
        elif opcion == '5':
            id_usuario = input("Ingrese el ID del usuario: ")
            titulo = input("Ingrese el título del libro: ")
            resultado = biblio.prestar_libro(id_usuario, titulo)
            print(f"\n{resultado}")
        elif opcion == '6':
            id_usuario = input("Ingrese el ID del usuario: ")
            nombre = input("Ingrese el nombre del usuario: ")
            resultado = biblio.agregar_usuario(id_usuario, nombre)
            print(f"\n{resultado}")
        elif opcion == '7':
            print("\nTodos los libros en la biblioteca:")
            if biblio.libros:
                for libro in biblio.libros:
                    print(f" - {libro['titulo']} por {libro['autor']}")
            else:
                print("No hay libros en la biblioteca.")
        elif opcion == '8':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    # Iniciar menú interactivo
    menu()
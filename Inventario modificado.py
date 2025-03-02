import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self, archivo='inventario_modificado.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()
    def cargar_inventario(self):
        "Carga los productos desde el archivo .txt al iniciar el programa."
        if not os.path.exists(self.archivo):
            print(f"El archivo {self.archivo} no existe. Se crea un nuevo archivo.")
            open(self.archivo, 'w').close()  # Crea el archivo si no existe
            return
        
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
            print("Inventario cargado con éxito.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        "Guarda los productos en el archivo."
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(str(producto) + '\n')
            print("Inventario guardado con éxito.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        "Agrega un nuevo producto en el inventario."
        if id_producto in self.productos:
            print(f"El producto con ID {id_producto} ya existe. Actualiza la cantidad.")
            self.productos[id_producto].set_cantidad(self.productos[id_producto].cantidad + cantidad)
        else:
            self.productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)
            print(f"Producto {nombre} agregado con éxito.")
        self.guardar_inventario()

    def eliminar_producto(self, id_producto):
        "Elimina un producto del inventario."
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado con éxito.")
            self.guardar_inventario()
        else:
            print(f"El producto con ID {id_producto} no se encuentra en el inventario.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        "Actualiza la cantidad o precio de un producto existente en el archivo."
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print(f"Producto con ID {id_producto} actualizado con éxito.")
            self.guardar_inventario()
        else:
            print(f"El producto con ID {id_producto} no se encuentra en el inventario.")

    def buscar_producto(self, nombre):
        "Busca y muestra productos por nombre."
        encontrados = [producto for producto in self.productos.values() if nombre.lower() in producto.get_nombre().lower()]
        if encontrados:
            print("Productos encontrados:")
            for producto in encontrados:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_inventario(self):
        "Muestra todos los productos en el inventario."
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.productos.values():
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

def menu():
    inventario = Inventario()
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Mostrar inventario")
        print("5. Buscar producto")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '3':
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")

            # Validación de entradas
            if cantidad:
                try:
                    cantidad = int(cantidad)
                except ValueError:
                    print("🚫 Error: La cantidad debe ser un número entero.")
                    cantidad = None
            else:
                cantidad = None

            if precio:
                try:
                    precio = float(precio)
                except ValueError:
                    print("🚫 Error: El precio debe ser un número decimal.")
                    precio = None
            else:
                precio = None

            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == '4':
            inventario.mostrar_inventario()
        elif opcion == '5':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("🚫 Error: El ID del producto ya existe. Por favor, elige un ID único.")
        else:
            self.productos.append(producto)
            print("✅ Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                print("🗑️ Producto eliminado exitosamente.")
                return
        print("🚫 Error: Producto no encontrado. Asegúrate de que el ID sea correcto.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("✅ Producto actualizado exitosamente.")
                return
        print("🚫 Error: Producto no encontrado. Asegúrate de que el ID sea correcto.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("🔍 Productos encontrados:")
            for producto in resultados:
                print(producto)
        else:
            print("🚫 No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            print("📦 Productos en el inventario:")
            for producto in self.productos:
                print(producto)
        else:
            print("🚫 El inventario está vacío.")


def menu():
    inventario = Inventario()
    print("👋 ¡Bienvenido al Sistema de Gestión de Inventarios!")
    print("Aquí puedes añadir, actualizar, eliminar y buscar productos en tu inventario.")
    
    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            id_producto = input("Ingrese el ID del producto (debe ser único): ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = input("Ingrese la cantidad del producto: ")
            precio = input("Ingrese el precio del producto: ")

            # Validación de entradas
            try:
                cantidad = int(cantidad)
                precio = float(precio)
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("🚫 Error: La cantidad debe ser un número entero y el precio debe ser un número decimal.")

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")

            # Validación de entradas
            if cantidad:
                try:
                    cantidad = int(cantidad)
                except ValueError:
                    print("🚫 Error: La cantidad debe ser un número entero.")
                    cantidad = None
            if precio:
                try:
                    precio = float(precio)
                except ValueError:
                    print("🚫 Error: El precio debe ser un número decimal.")
                    precio = None
        else:
                precio = None

            inventario.actualizar_producto(id_producto, cantidad, precio)

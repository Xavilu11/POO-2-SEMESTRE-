import os

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        "Carga los productos desde el archivo .txt al iniciar el programa."
        if not os.path.exists(self.archivo):
            print(f"El archivo {self.archivo} no existe. Se crea un producto nuevo.")
            open(self.archivo, 'w').close()  # Se crea el archivo si no existe
            return
        
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[nombre] = Producto(nombre, int(cantidad), float(precio))
            print("Inventario cargado con éxito.")
        except FileNotFoundError:
            print(f"Error: El archivo {self.archivo} no existe.")
        except PermissionError:
            print(f"Error: No existen permisos para leer el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        "Guarda los productos en el archivo."
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(str(producto) + '\n')
            print("Inventario guardado con éxito.")
        except PermissionError:
            print(f"Error: No existen permisos para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        "Agrega un nuevo producto en el inventario."
        if nombre in self.productos:
            print(f"El producto {nombre} ya existe. Actualiza la cantidad.")
            self.productos[nombre].cantidad += cantidad
        else:
            self.productos[nombre] = Producto(nombre, cantidad, precio)
            print(f"Producto {nombre} agregado con éxito.")
        self.guardar_inventario()

    def eliminar_producto(self, nombre):
        "Elimina un producto del inventario."
        if nombre in self.productos:
            del self.productos[nombre]
            print(f"Producto {nombre} eliminado con éxito.")
            self.guardar_inventario()
        else:
            print(f"El producto {nombre} no se encuentra en el inventario.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        "Actualiza la cantidad o precio de un producto existente en el archivo."
        if nombre in self.productos:
            if cantidad is not None:
                self.productos[nombre].cantidad = cantidad
            if precio is not None:
                self.productos[nombre].precio = precio
            print(f"Producto {nombre} actualizado con éxito.")
            self.guardar_inventario()
        else:
            print(f"El producto {nombre} no se encuentra en el inventario.")

    def mostrar_inventario(self):
        "Muestra todos los productos en el inventario."
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("Inventario:")
            for producto in self.productos.values():
                print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

# Detalle para uso
if __name__ == "__main__":
    inventario = Inventario()
    inventario.agregar_producto("Manzana", 10, 0.5)
    inventario.agregar_producto("Piñas", 5, 0.3)
    inventario.agregar_producto("Naranjas", 25, 0.25)
    inventario.mostrar_inventario()
    inventario.actualizar_producto("Manzana", cantidad=15)
    inventario.actualizar_producto("Piñas", precio=1.00)
    inventario.actualizar_producto("Naranjas", cantidad=25)
    inventario.mostrar_inventario()
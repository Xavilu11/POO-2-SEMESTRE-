import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        # Vamos a configurar nuestra ventana principal para la app.
        self.root = root
        self.root.title("Mi Lista de Tareas Pendientes")  # Un título más amigable jejeje
        # Aquí guardaremos todas nuestras tareas, como una lista de recordatorios
        self.tasks = []

        # Este es el espacio donde escribimos la nueva tarea y los botones para interactuar.
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        # Cada botón tiene un texto que le dice al usuario qué hace y una "orden" (función) que ejecutar.
        botones = [
            ("¡Añadir a la lista!", self.add_task),
            ("¡Listo, completada!", self.complete_task),
            ("Eliminar Tarea", self.delete_task)  # ¡Botón actualizado!
        ]
        for texto, accion in botones:
            tk.Button(root, text=texto, command=accion).pack(pady=5)

        # La caja donde veremos todas nuestras tareas, como una lista en papel.
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Atajos de teclado para los más rápidos
        # Enter para añadir, 'c' para completar, Suprimir para eliminar y Escape para cerrar.
        self.root.bind('<Return>', self.add_task)
        self.root.bind('<c>', self.complete_task)
        self.root.bind('<Delete>', self.delete_task)
        self.root.bind('<Escape>', self.root.quit)

    # Una pequeña ayuda para saber qué tarea eligió el usuario.
    def _obtener_indice_seleccionado(self):
        try:
            return self.task_listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("¡Ojo!", "Por favor, selecciona una tarea de la lista.")
            return None

    def add_task(self):
        # Cogemos lo que escribió el usuario en la caja de texto.
        nueva_tarea = self.task_entry.get()
        if nueva_tarea:
            # Si escribió algo, lo añadimos a nuestra lista de tareas
            self.tasks.append(nueva_tarea)
            # Y actualizamos la vista para que aparezca la nueva tarea.
            self.update_task_list()
            # Limpiamos la caja de texto para la siguiente tarea.
            self.task_entry.delete(0, tk.END)
        else:
            # Si intentó añadir sin escribir nada, le avisamos amablemente.
            messagebox.showwarning("¡Un momento!", "Escribe algo en la tarea antes de añadirla, ¿sí?")

    def complete_task(self):
        # Averiguamos qué tarea seleccionó el usuario.
        indice = self._obtener_indice_seleccionado()
        if indice is not None:
            # Si seleccionó una, la marcamos como completada añadiendo un "(¡Hecho!)" al final.
            self.tasks[indice] += " (¡Hecho!)"
            # Y volvemos a mostrar la lista actualizada.
            self.update_task_list()

    def delete_task(self):
        # Similar a completar, primero vemos qué tarea quiere eliminar.
        indice = self._obtener_indice_seleccionado()
        if indice is not None:
            # La eliminamos de nuestra lista
            del self.tasks[indice]
            # Refrescamos la lista en pantalla.
            self.update_task_list()

    def update_task_list(self):
        # Limpiamos la lista que se ve en la pantalla para volverla a dibujar.
        self.task_listbox.delete(0, tk.END)
        # Recorremos nuestra lista de tareas y las añadimos a la caja de texto.
        for tarea in self.tasks:
            self.task_listbox.insert(tk.END, tarea)

if __name__ == "__main__":
    # Aquí empieza todo... Creamos la ventana principal.
    ventana_principal = tk.Tk()
    # creamos nuestra aplicación de gestión de tareas dentro de esa ventana
    app = TaskManagerApp(ventana_principal)
    # y la mantenemos abierta esperando que el usuario interactúe.
    ventana_principal.mainloop()
import tkinter as tk
from tkinter import messagebox, END

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("800x400")

        # Campo de entrada para agregar tareas
        self.task_entry = tk.Entry(root, width=80)  # Ajustar el ancho del Entry
        self.task_entry.pack(pady=10)  # Usar pack para posicionar el Entry
        self.task_entry.bind("<Return>", self.add_task)  # Agregar tarea al presionar Enter

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=80, height=15)  # Reducir tamaño del Listbox
        self.task_listbox.pack(pady=10)

        # Marco para los botones
        self.button_frame = tk.Frame(root)  # Crear un marco para organizar los botones
        self.button_frame.pack(pady=10)

        # Botón para agregar tareas
        self.add_button = tk.Button(self.button_frame, text="Agregar Tarea", command=self.add_task)
        self.add_button.pack(side="left", padx=5)

        # Botón para eliminar tareas
        self.delete_button = tk.Button(self.button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side="left", padx=5)

    def add_task(self, event=None):
        "Agrega una nueva tarea a la lista."
        task = self.task_entry.get()
        if task.strip():  # Verificar que no esté vacío
            self.task_listbox.insert(END, task)
            self.task_entry.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def delete_task(self):
        "Elimina la tarea seleccionada de la lista."
        try:
            selected_task_index = self.task_listbox.curselection()
            if selected_task_index:
                self.task_listbox.delete(selected_task_index[0])
            else:
                messagebox.showwarning("Precaución", "Selecciona una tarea.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    TaskManagerApp(root)
    root.mainloop()
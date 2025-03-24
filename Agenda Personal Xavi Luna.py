import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal Xavi Luna")
        self.root.geometry("600x500")
        self.root.configure(bg='Lightblue')  # Fondo de la ventana principal

        # Estilo para los botones y otros widgets
        style = ttk.Style()
        style.configure('TButton', foreground='black')  # Color de texto de los botones
        style.configure('TFrame', background='Lightblue')  # Fondo de los Frames
        style.configure('TEntry', fieldbackground='white', background='white')  # Fondo de los Entry

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(self.root, style='TFrame')
        self.frame_lista.pack(pady=10)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Marco para entrada de datos
        self.frame_entrada = ttk.Frame(self.root, style='TFrame')  # Fondo del Frame igual al de la ventana
        self.frame_entrada.pack(pady=10, padx=10, fill='x')

        # Etiquetas y campos de entrada
        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.fecha_entry = DateEntry(self.frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.hora_entry = ttk.Entry(self.frame_entrada, style='TEntry')  # Fondo blanco para Entry
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.descripcion_entry = ttk.Entry(self.frame_entrada, style='TEntry')  # Fondo blanco para Entry
        self.descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

        # Marco para los botones
        self.frame_botones = ttk.Frame(self.root, style='TFrame')  # Fondo del Frame igual al de la ventana
        self.frame_botones.pack(pady=10, padx=10, fill='x')

        # Botones
        self.boton_agregar = ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento, style='TButton')
        self.boton_agregar.pack(side='left', padx=10, pady=5)

        self.boton_eliminar = ttk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento, style='TButton')
        self.boton_eliminar.pack(side='left', padx=10, pady=5)

        self.boton_salir = ttk.Button(self.frame_botones, text="Salir", command=self.root.quit, style='TButton')
        self.boton_salir.pack(side='left', padx=10, pady=5)

    def agregar_evento(self):
        "Agrega un nuevo evento a la lista."
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.fecha_entry.delete(0, 'end')
            self.hora_entry.delete(0, 'end')
            self.descripcion_entry.delete(0, 'end')
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        "Elimina el evento seleccionado de la lista."
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este evento?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
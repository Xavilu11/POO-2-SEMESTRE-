import tkinter as Datos_de_Nombres
from tkinter import messagebox
tk=Datos_de_Nombres
def agregar_nombre():
    nombre = entry.get()
    if nombre:
        listbox.insert(tk.END, nombre)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Un momento", "Ingrese un nombre.")
def eliminar_nombre():
    seleccion = listbox.curselection()
    if seleccion:
        listbox.delete(seleccion)
    else:
        messagebox.showwarning("Atención", "Elija un nombre de usuario para eliminar.")

# Crea la ventana principal
ventana = tk.Tk()
ventana.title("Datos de Nombres")
# Etiqueta campo de texto
tk.Label(ventana, text="Ingrese un nombre:").pack(pady=5)
entry = tk.Entry(ventana)
entry.pack(pady=5)

# Botón "Agregar"
tk.Button(ventana, text="Agregar", command=agregar_nombre).pack(pady=5)

# Listado de los nombres
listbox = tk.Listbox(ventana)
listbox.pack(pady=5)

# Botón "Eliminar"
tk.Button(ventana, text="Eliminar", command=eliminar_nombre).pack(pady=5)

# Inicia la aplicación
ventana.mainloop()
import tkinter as tk
from tkinter import messagebox

def estudiantes():
    def guardar():
        nombre= entry_nombre.get()
        apellido =entry_apellido.get()
        print("nombre:",nombre)
        print("apellido:",apellido)

    top = tk.Toplevel(root)
    top.title("agregar")

    label_nombre = tk.Label(top, text="Nombre:")
    label_nombre.pack(pady=5)
    entry_nombre = tk.Entry(top, width=30)
    entry_nombre.pack(pady=5)

    label_apellido = tk.Label(top, text="Apellido:")
    label_apellido.pack(pady=5)
    entry_apellido = tk.Entry(top, width=30)
    entry_apellido.pack(pady=5)

    button_guardar = tk.Button(top, text="Guardar", command=guardar)
    button_guardar.pack(y=10)

def cerrar():
    def alo():
        root.destroy()

root =tk.Tk()
root.title("menu")

button1 = tk.Button(root, text="Agregar Estudiante", command=estudiantes)
button1.pack(pady=10)

button2 = tk.Button(root,text="cerrar", command=cerrar)
button2.pack(pady=10)

root.mainloop()

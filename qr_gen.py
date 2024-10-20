import subprocess
import sys

# Function to install a package
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = ["tkinter", "qrcode"]

# Check and install missing packages
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install_package(package)

import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def create_qr_code():
    texto_usuario = text_entry.get()
    mostrar = mostrar_var.get()
    guardar = guardar_var.get()
    nombre_archivo = filename_entry.get()

    if not texto_usuario:
        messagebox.showwarning("Advertencia", "Por favor ingresa un texto.")
        return

    if guardar and not nombre_archivo:
        messagebox.showwarning("Advertencia", "Por favor ingresa un nombre para el archivo.")
        return

    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto_usuario)
    qr.make(fit=True)
    imagen_qr = qr.make_image(fill='black', back_color='white')

    if mostrar:
        # Mostrar la imagen en una nueva ventana
        img = ImageTk.PhotoImage(imagen_qr)
        img_label.config(image=img)
        img_label.image = img

    if guardar:
        imagen_qr.save(f"{nombre_archivo}.png")
        messagebox.showinfo("Información", f"El código QR ha sido guardado como '{nombre_archivo}.png'.")

def toggle_filename_entry():
    if guardar_var.get():
        filename_entry.config(state='normal')
    else:
        filename_entry.config(state='disabled')

# Configurar la ventana principal
root = tk.Tk()
root.title("Generador de Código QR")

# Campo de texto para el ingreso del texto
text_label = tk.Label(root, text="Ingresa el texto para el código QR:")
text_label.pack()
text_entry = tk.Entry(root, width=50)
text_entry.pack()

# Checkbox para mostrar el QR
mostrar_var = tk.BooleanVar()
mostrar_checkbox = tk.Checkbutton(root, text="Mostrar en pantalla", variable=mostrar_var)
mostrar_checkbox.pack()

# Checkbox para guardar el QR
guardar_var = tk.BooleanVar()
guardar_checkbox = tk.Checkbutton(root, text="Guardar como PNG", variable=guardar_var, command=toggle_filename_entry)
guardar_checkbox.pack()

# Campo de texto para el nombre del archivo (deshabilitado por defecto)
filename_entry = tk.Entry(root, width=30, state='disabled')
filename_entry.pack()

# Botón para crear el código QR
create_button = tk.Button(root, text="Create QR Code", command=create_qr_code)
create_button.pack()

# Etiqueta para mostrar la imagen del QR
img_label = tk.Label(root)
img_label.pack()

# Iniciar el bucle de la interfaz gráfica
root.mainloop()
